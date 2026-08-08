# if __name__ == "__main__"
* If this file/module is executing directly, execute the following code. 

## What is __name__?
1. __name__ is a special variable automatically created by python for every module.
2. Its value depends on how python file is being called.
   * If the Python module calculator.py is called directly: 'python calculator.py' then value of the __name__ variable is "__main__"
   * If the module calculator.py is imported by another file: then value of the __name__ variable is "calculator"

## What is __main__?
* When a Python file is executed directly, Python executes it as the special __main__ module.
* So
  ```
  __name__ == "__main__"
  ```
  This module is currently being used as the program's entry point.

## Why Is This Useful?
* Imagine your calculator.py contains:
  ```
  def add(a, b):
    return a + b

  print("Testing Calculator")
  print(add(3, 4))
  ```
* When you run:
  ```
  python calculator.py
  ```
  Output: Testing Calculator
          7
* Imagine main.py file:
  ```
   from calculator import add

   result = add(10, 20)
   print(result)

  ```
  1. Output: Testing Calculator
          7
          30
  2. Probably we don't want the "Testing Calcultor" and 7 instead we want only 30
  3. Problem is that python executes the top-level code in an imported module.
* To avoid this we have to write the calculator.py module by checking the __name__ variable.
  ```
  def add(a, b):
    return a + b
  
  if __name__ == "__main__":
    print("Testing Calculator")
    print(add(3, 4))
  ```

## Direct Execution
* To execute the testing code, we can use direct execution
  ```
  python calculator.py
  ```

## Importing a Module
* The testing code doesn't execute.
  ```
  from calculator import add
  ``` 

## Why do we use it?
* It allows us to execute a block of code only when the module is executed directly, while preventing that code from executing when the file is imported as a module. This is useful for keeping test, demo, or application-entry code separate from reusable functions and classes.

## Real-world AI Example
1. Imagine our Enterprise AI application:
  ```
    EnterpriseAI/

    main.py

    services/
        chat_service.py
        embedding_service.py
        search_service.py
  ```
2. chat_service.py:
```
def generate_response(question):
    return f"Response for: {question}"


if __name__ == "__main__":
    response = generate_response("What is RAG?")
    print(response)
```
* During development, we can test:
  ```
  python chat_service.py
  ```
  and get: Response for: What is RAG?
* But in main.py:
  ```
  from services.chat_service import generate_response

  response = generate_response("Explain RAG")
  print(response)
  ```
  The test code inside chat_service.py doesn't execute.

## Common Mistakes
* Don't write:
  ```
  if __name__ == "main"
  ```
* It must be:
  ```
  if __name__ == "__main__":
  ```
* There are two underscores on each side:
  ```
  __name__
  __main__
  ```
## Interview Questions

### Why does Python execute top-level code when a module is imported?

* When Python imports a module, it executes the module's top-level code to initialize the module and make its functions, classes, and variables available.
* Therefore, code that should run only during direct execution should be placed inside:
 `if __name__ == "__main__":`

### What is the difference between `__name__` and `__main__`?

* `__name__` is a special variable created by Python for each module.
* `"__main__"` is a special value assigned to `__name__` when that module is executed directly.
* Therefore:
    `if __name__ == "__main__":`
    checks whether the current module is being executed directly.

### Can __name__ have a value other than "__main__"?
* Yes. When a module is imported, __name__ generally contains the module's qualified name.
* For example:
  ```
  import calculator
  print(calculator.__name__)
  ```
  Output: calculator
* For a module inside a package:
  ```
  services/
    chat_service.py
  ```
  it can be: services.chat_service
* This is a useful detail for understanding packages.

Direct Execution
----------------

python calculator.py
        ↓
__name__ = "__main__"
        ↓
Condition = True
        ↓
Testing code executes

Import
------

main.py
   ↓
import calculator
   ↓
__name__ = "calculator"
   ↓
Condition = False
   ↓
Testing code does NOT execute

## My Learning

- `__name__` is a special variable created for every Python module.
- When a file is executed directly, `__name__` becomes `"__main__"`.
- When a file is imported, `__name__` becomes the module name.
- `if __name__ == "__main__":` prevents direct-execution code from running during import.
- This allows a Python file to be both reusable as a module and executable as a standalone program.