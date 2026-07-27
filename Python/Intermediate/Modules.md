# Python Modules

## What is module?
* A Python module is a `.py` file that contains reusable code such as functions, classes, variables, and constants.
* Every Python file is a module.
* Example: calculator.py this file itself a module.

## Why do we need modules?
* If we are developing the enterprise AI application. We wouldn't write all the code in a single file. Without modules:
```
# main.py

# Database code
# Authentication
# AI Model
# FastAPI
# Logging
# Utility functions
# Email
# Payment
# 5000 lines...
```
Question:
1. Can another developer understand this? No
2. Can you maintain it after one year? No

Instead we divide it.
```
project/

main.py
database.py
auth.py
logger.py
email_service.py
chat_service.py
```
Now every file has one responsibility. This is called 'Modular Programming'.

## Real-world Example
Imagine a Hospital. Would one doctor do everything?
        ```
        Heart Surgery
        Dental
        Eye Checkup
        ```
No. Each doctor is specialized.

Python modules follow the same idea.
        ```
        EnterpriseAI/
        main.py
        database.py
        chat_service.py
        embedding.py
        vector_store.py
        prompt_builder.py
        logger.py
        ```
Each module has one responsiblity.

## Modular Programming
* Every module should have one responsibility.
* Bad
  ```
  database.py

  Authentication
  Email
  Logging
  Payment
  ```
* Good
  ```
  database.py
    ↓
  Database only

  logger.py
    ↓
  Logging only

  payment.py
    ↓
  Payment only
  ```
* This follows the Single Responsibility Principle (SRP).

## How modules work?
Suppose we have
    ```
    # calculator.py

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b
    ```
Another file
    ```
    main.py

    import calculator
    print(calculator.add(2,3))
    ```
Output
    ```
    5
    ```
## How did Python know where calculator.add() is?
* When python sees:
```
import calculator
```
1. Finds calculator.py file
2. Execute the file
3. Create a module object
4. Makes its functions available

## What Happens Internally?
```
import calculator
     ↓
python finds calcultor.py file
     ↓
Read Source Code
     ↓
Compile to Bytecode (if needed)
     ↓
Execute Module
     ↓
Create Module Object
     ↓
Store in sys.modules
     ↓
Return Module
```
This is why importing many modules increases startup time.

## Different ways to import

### Method 1
```
import calculator
calculator.add(5,10)
```
Preferred when the module has many functions.

### Method 2
```
from calculator import add
print(add(5,10))
```
Imports only one function.

### Method 3
```
from calculator import *
```
Imports everything. Avoid this.
Because, we don't know where the functions came from.

### Method 4
```
import calculator as calc
print(calc.add(10,20))
```
* Alias privdes shoter name for module.
* Useful for longer module names.

## Built-in Modules
- math 
    ```
    import math
    print(math.sqrt(25)) --5.0
    ```
- random
    ```
    import random
    print(random.randint(1,10)) --7(Random every time.)
```
- datetime
    ```
    import datetime
    print(datetime.datetime.now()) --Current date and time.
    ```
- os
    ```
    import os
    print(os.getcwd()) --Current directory.
```

## Interview Questions:
### What is python module?
* A python module is a '.py' file containing reusable code such as functions, classes, variables.

### Why do we use modules?
* Instead of writing an entire application code into a single file, modules divide the application into a logical components.
* Benefits:
  -> Reusablity
  -> Maintainability
  -> Readability
  -> Easire Testing

### Difference between Module and Package?
Module
```
calculator.py
```
Package
```
utils/
math.py
date.py
string.py
```
A package is a collection of related modules.

### Can two files import each other?
* Yes. But this can create a circular import, where each module waits for the other to finish loading.
* It's generally considered poor design and should be avoided by restructuring the code.

### Where does Python search for modules?
Python searches:
```
Current directory
Standard library
Installed packages (site-packages)
Paths listed in sys.path
```

### Is a module loaded every time we import it?
* No. Python loads it once and caches it in memory.
* Future imports reuse the cached module.

### What is the difference between
import calculator
and
from calculator import add

Answer:
```
import calculator
↓
Imports entire module
Need
calculator.add()

-------------------
from calculator import add
↓
Imports only add()
Call directly
add()
```
### Why should we avoid
from module import *

Answer:
```
Because
* Namespace pollution
* Difficult to know where functions came from
* Possible naming conflicts
```

### Does importing the same module twice execute it twice?
* No. Python imports a module only once.
* Example: 
    ```
    import math
    import math
    ```
    The second import uses the cached module from 'sys.modules' instead of executing the file again. This is why importing the same module multiple times is not expensive.

## Can a module contain classes?
* Yes. A module can contain 
  Functions
  Classes
  Variables
  Constants
  Exceptions
* Example:
  ```
  PI = 3.14

  class Student:
    pass

  def add():
    pass
  ```
* Everything above exists inside one module.

## What is the difference between a built-in module and a third-party module?
* Built-in-module
  ```
  math
  random
  os
  datetime
  ```
* Third-party module
  Needs installation
  ```
  pip install numpy
  pip install pandas
  pip install fastapi
  ```
  These are installed from PyPI(Python package index).
    
## Common Mistakes:
* Writing the entire application in one file.
* Using
   ```
   from module import *
   ```
* Creating circular imports.
* Giving modules multiple responsibilities.
* Naming a module the same as a built-in module.
  ```
  Example:
  math.py
  random.py
  os.py

  If we are creating math.py 
  
  import math -> Python may import your file instead of the built-in math module, causing confusing errors.
  ```
## My Learning

Today I learned:

- Every Python file is a module.
- Modules improve code organization.
- Python loads modules only once and caches them in sys.modules.
- Avoid wildcard imports.
- Every module should have a single responsibility.