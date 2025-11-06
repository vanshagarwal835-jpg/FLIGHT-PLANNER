# Programming and SQL Interview Questions with Answers

## Programming Interview Questions & Answers

### Python Basics

1. **What is the difference between a list and a tuple in Python?**
   - Lists are mutable (can be changed after creation) while tuples are immutable (cannot be changed after creation)
   - Lists use square brackets [] while tuples use parentheses ()
   - Lists have more built-in methods than tuples
   - Tuples are generally faster for accessing elements

2. **Explain the concept of exception handling in Python with an example.**
   Exception handling in Python is managed using try, except, else, and finally blocks:
   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero")
   else:
       print("Division successful")
   finally:
       print("Execution completed")
   ```

3. **What is the purpose of `__init__` method in Python classes?**
   The `__init__` method is a special method that gets called when an object is instantiated from a class. It initializes the attributes of the class and is commonly referred to as a constructor.

4. **How does garbage collection work in Python?**
   Python uses reference counting and cyclic garbage collection. Reference counting tracks how many references point to an object, and when the count reaches zero, the object is deallocated. For cyclic references, Python has a separate garbage collector.

5. **What are decorators in Python and how are they used?**
   Decorators are functions that modify the behavior of other functions. They allow you to add functionality to existing functions without permanently modifying them:
   ```python
   def my_decorator(func):
       def wrapper():
           print("Before function")
           func()
           print("After function")
       return wrapper
   
   @my_decorator
   def say_hello():
       print("Hello!")
   ```

### Python Functions and Modules

6. **Explain the difference between local and global variables in Python.**
   Local variables are declared inside a function and can only be accessed within that function. Global variables are declared outside functions and can be accessed throughout the program.

7. **What is the difference between `==` and `is` operators in Python?**
   `==` compares the values of two objects, while `is` checks if both operands refer to the same object in memory.

8. **How do you handle errors in Python? Give an example using try-except blocks.**
   Errors are handled using try-except blocks:
   ```python
   try:
       num = int(input("Enter a number: "))
       result = 10 / num
   except ValueError:
       print("Invalid input! Please enter a number.")
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   ```

9. **What are lambda functions in Python? Provide an example.**
   Lambda functions are small anonymous functions defined with the lambda keyword:
   ```python
   multiply = lambda x, y: x * y
   print(multiply(5, 3))  # Output: 15
   ```

10. **Explain the use of `*args` and `**kwargs` in Python functions.**
    `*args` allows passing a variable number of non-keyword arguments to a function, while `**kwargs` allows passing a variable number of keyword arguments:
    ```python
    def example(*args, **kwargs):
        print(args)    # Tuple of positional arguments
        print(kwargs)  # Dictionary of keyword arguments
    ```

### Object-Oriented Programming

11. **What are the four pillars of Object-Oriented Programming?**
    - Encapsulation: Bundling data and methods together and restricting access to internal components
    - Inheritance: Creating new classes from existing ones to reuse code
    - Polymorphism: Ability of objects to take multiple forms
    - Abstraction: Hiding complex implementation details and showing only essential features

12. **Explain inheritance in Python with an example.**
    Inheritance allows a class to inherit attributes and methods from another class:
    ```python
    class Animal:
        def __init__(self, name):
            self.name = name
    
    class Dog(Animal):
        def bark(self):
            print(f"{self.name} is barking")
    
    dog = Dog("Buddy")
    dog.bark()  # Output: Buddy is barking
    ```

13. **What is polymorphism and how is it implemented in Python?**
    Polymorphism allows objects of different types to be treated as instances of the same type. In Python, it's implemented through method overriding and duck typing:
    ```python
    class Bird:
        def sound(self):
            pass
    
    class Sparrow(Bird):
        def sound(self):
            return "Chirp"
    
    class Crow(Bird):
        def sound(self):
            return "Caw"
    ```

14. **What is the difference between class variables and instance variables?**
    Class variables are shared among all instances of a class, while instance variables are unique to each instance:
    ```python
    class Student:
        school = "ABC High School"  # Class variable
        
        def __init__(self, name):
            self.name = name  # Instance variable
    ```

15. **Explain the concept of encapsulation in Python.**
    Encapsulation restricts direct access to some components of an object. In Python, this is achieved using private attributes (prefixed with underscore):
    ```python
    class BankAccount:
        def __init__(self, balance):
            self._balance = balance  # Protected attribute
        
        def get_balance(self):
            return self._balance
    ```

### File Handling and Libraries

16. **How do you read and write files in Python?**
    Reading files:
    ```python
    with open('file.txt', 'r') as f:
        content = f.read()
    ```
    Writing files:
    ```python
    with open('file.txt', 'w') as f:
        f.write("Hello World")
    ```

17. **What is the purpose of the `with` statement in Python?**
    The `with` statement ensures proper acquisition and release of resources. It automatically closes files even if an error occurs, eliminating the need for explicit close() calls.

18. **How do you handle JSON data in Python?**
    Using the json module:
    ```python
    import json
    
    # Convert Python object to JSON
    data = {"name": "John", "age": 30}
    json_string = json.dumps(data)
    
    # Convert JSON to Python object
    parsed_data = json.loads(json_string)
    ```

19. **Explain the use of the `requests` library in Python.**
    The requests library is used for making HTTP requests. It simplifies sending GET, POST, PUT, DELETE requests:
    ```python
    import requests
    response = requests.get('https://api.example.com/data')
    data = response.json()
    ```

20. **What is the difference between shallow copy and deep copy in Python?**
    Shallow copy creates a new object but references the same nested objects. Deep copy creates a new object and recursively copies all nested objects:
    ```python
    import copy
    list1 = [[1, 2], [3, 4]]
    list2 = copy.copy(list1)    # Shallow copy
    list3 = copy.deepcopy(list1)  # Deep copy
    ```

## SQL Interview Questions & Answers

### Basic SQL Queries

1. **What is the difference between `WHERE` and `HAVING` clauses?**
   WHERE filters rows before grouping, while HAVING filters groups after grouping. WHERE is used with SELECT, UPDATE, DELETE statements, while HAVING is used with GROUP BY.

2. **Explain the difference between `INNER JOIN` and `LEFT JOIN`.**
   INNER JOIN returns only matching rows from both tables. LEFT JOIN returns all rows from the left table and matching rows from the right table, with NULLs for non-matching rows.

3. **What is a primary key and a foreign key in SQL?**
   Primary key uniquely identifies each record in a table and cannot be NULL. Foreign key is a field in one table that refers to the primary key in another table, establishing a relationship between tables.

4. **How do you eliminate duplicate rows from a query result?**
   Using DISTINCT keyword:
   ```sql
   SELECT DISTINCT city FROM airports;
   ```

5. **What is the difference between `DELETE` and `TRUNCATE` commands?**
   DELETE removes rows based on a condition and can be rolled back. TRUNCATE removes all rows from a table and is faster but cannot be rolled back.

### Database Design and Concepts

6. **What are the different types of SQL constraints?**
   - PRIMARY KEY: Uniquely identifies each row
   - FOREIGN KEY: Establishes relationship between tables
   - UNIQUE: Ensures all values in a column are unique
   - NOT NULL: Prevents NULL values
   - CHECK: Ensures values meet a specific condition
   - DEFAULT: Provides a default value

7. **Explain normalization and its benefits.**
   Normalization organizes data to minimize redundancy and improve data integrity. Benefits include reduced storage space, improved data consistency, and easier maintenance.

8. **What is the difference between a clustered and a non-clustered index?**
   Clustered index determines the physical order of data in a table (only one per table). Non-clustered index creates a separate structure pointing to data locations (multiple per table).

9. **What is a transaction in SQL and what are ACID properties?**
   Transaction is a sequence of operations performed as a single unit. ACID properties:
   - Atomicity: All operations succeed or all fail
   - Consistency: Database remains in a consistent state
   - Isolation: Concurrent transactions don't interfere
   - Durability: Committed changes are permanent

10. **Explain the difference between CHAR and VARCHAR data types.**
    CHAR is fixed-length and pads with spaces, while VARCHAR is variable-length and only uses required space. CHAR is faster for fixed-length data, VARCHAR saves space for variable-length data.

### Advanced SQL Queries

11. **Write a query to find the second highest flight distance from the routes table.**
    ```sql
    SELECT MAX(distance) AS second_highest 
    FROM routes 
    WHERE distance < (SELECT MAX(distance) FROM routes);
    ```

12. **How would you optimize a slow-running SQL query?**
    - Use indexes appropriately
    - Avoid SELECT *
    - Use WHERE clauses to filter early
    - Avoid functions in WHERE clauses
    - Analyze query execution plans
    - Consider query rewriting

13. **What is the use of GROUP BY clause? Give an example.**
    GROUP BY groups rows with the same values and is often used with aggregate functions:
    ```sql
    SELECT source_id, COUNT(*) 
    FROM routes 
    GROUP BY source_id;
    ```

14. **Explain the difference between UNION and UNION ALL.**
    UNION combines result sets and removes duplicates, while UNION ALL combines result sets including duplicates. UNION ALL is faster since it doesn't remove duplicates.

15. **What are subqueries in SQL? Provide an example.**
    Subqueries are queries nested within another query:
    ```sql
    SELECT name 
    FROM airports 
    WHERE airport_id IN (SELECT source_id FROM routes WHERE distance > 1000);
    ```

### SQL Operations Specific to Flight Planner

16. **How would you write a query to find all airports in India from the airports table?**
    ```sql
    SELECT * FROM airports WHERE country = 'India';
    ```

17. **Write a query to find routes with flight time greater than 100 minutes.**
    ```sql
    SELECT * FROM routes WHERE flight_time > 100;
    ```

18. **How would you join the airports, routes, and weather tables to show complete flight information?**
    ```sql
    SELECT a1.name AS source, a2.name AS destination, r.distance, r.fuel_cost, r.flight_time,
           w1.weather_condition AS source_weather, w2.weather_condition AS dest_weather
    FROM routes r
    JOIN airports a1 ON r.source_id = a1.airport_id
    JOIN airports a2 ON r.destination_id = a2.airport_id
    JOIN weather w1 ON a1.airport_id = w1.airport_id
    JOIN weather w2 ON a2.airport_id = w2.airport_id;
    ```

19. **Write a query to calculate the average fuel cost for all routes originating from Delhi.**
    ```sql
    SELECT AVG(r.fuel_cost) AS avg_fuel_cost
    FROM routes r
    JOIN airports a ON r.source_id = a.airport_id
    WHERE a.name = 'Indira Gandhi International Airport';
    ```

20. **How would you update the weather condition for a specific airport?**
    ```sql
    UPDATE weather 
    SET weather_condition = 'Sunny' 
    WHERE airport_id = (SELECT airport_id FROM airports WHERE name = 'Chennai International Airport');
    ```