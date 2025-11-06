import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ------------------ Database Connection ------------------
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",           # Your MySQL username
            password="9897", # Your MySQL password
            database="flight_planner"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# ------------------ Fetch Routes ------------------
def fetch_routes():
    source = source_combo.get()
    destination = destination_combo.get()

    if not source or not destination:
        messagebox.showwarning("Input Error", "Please select both source and destination airports.")
        return

    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()

    try:
        query = """
        SELECT a1.name AS source, a2.name AS destination, r.distance, r.fuel_cost, r.flight_time,
               w1.weather_condition AS source_weather, w2.weather_condition AS dest_weather
        FROM routes r
        JOIN airports a1 ON r.source_id = a1.airport_id
        JOIN airports a2 ON r.destination_id = a2.airport_id
        JOIN weather w1 ON a1.airport_id = w1.airport_id
        JOIN weather w2 ON a2.airport_id = w2.airport_id
        WHERE a1.name = %s AND a2.name = %s;
        """
        cursor.execute(query, (source, destination))
        result = cursor.fetchone()

        while cursor.nextset():
            cursor.fetchall()

        if result:
            src, dest, dist, fuel, time, src_weather, dest_weather = result
            output_text.set(
                f"✈ {src} → {dest}\n\n"
                f"📏 Distance: {dist} km\n"
                f"⛽ Fuel Cost: ₹{fuel}\n"
                f"🕒 Flight Time: {time} mins\n\n"
                f"🌤 Weather:\n   - Source: {src_weather}\n   - Destination: {dest_weather}"
            )
        else:
            output_text.set("⚠ No direct route found between these airports.")

    except mysql.connector.Error as err:
        messagebox.showerror("Query Error", f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# ------------------ Load Airports ------------------
def load_airports():
    conn = connect_db()
    if conn is None:
        return []

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT name FROM airports ORDER BY name;")
        airports = [row[0] for row in cursor.fetchall()]
        while cursor.nextset():
            cursor.fetchall()
        return airports
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error fetching airports: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

# ------------------ GUI ------------------
root = tk.Tk()
root.title("✈ Flight Route Planner")
root.geometry("700x600")
root.config(bg="#F5FFFA")  # Soft Mint White

# Title
title = tk.Label(root, text="🌍 Flight Route Planner", 
                 font=("Helvetica", 22, "bold"), bg="#F5FFFA", fg="#008B8B")
title.pack(pady=20)

# Frame for input fields
frame = tk.Frame(root, bg="#E0FFFF", bd=2, relief="groove")
frame.pack(pady=20, padx=30, fill="x")

tk.Label(frame, text="Source Airport:", bg="#E0FFFF", font=("Arial", 13, "bold")).grid(row=0, column=0, padx=15, pady=15)
tk.Label(frame, text="Destination Airport:", bg="#E0FFFF", font=("Arial", 13, "bold")).grid(row=1, column=0, padx=15, pady=15)

airports = load_airports()

source_combo = ttk.Combobox(frame, values=airports, width=45, state="readonly", font=("Arial", 11))
destination_combo = ttk.Combobox(frame, values=airports, width=45, state="readonly", font=("Arial", 11))

source_combo.grid(row=0, column=1, padx=10, pady=10)
destination_combo.grid(row=1, column=1, padx=10, pady=10)

# Button styling
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 13, "bold"),
                padding=6,
                background="#20B2AA",
                foreground="white")

search_btn = tk.Button(root, text="🔍 Find Route", font=("Arial", 13, "bold"),
                       bg="#20B2AA", fg="white", activebackground="#008B8B",
                       activeforeground="white", cursor="hand2",
                       relief="raised", bd=3, command=fetch_routes)
search_btn.pack(pady=25)

# Output
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, font=("Consolas", 13),
                        bg="#F5FFFA", fg="#004B49", justify="left", wraplength=650)
output_label.pack(pady=20)

footer = tk.Label(root, text="Developed by Mansi Rathore 💻", 
                  font=("Arial", 10, "italic"), bg="#F5FFFA", fg="#006666")
footer.pack(side="bottom", pady=10)

root.mainloop()