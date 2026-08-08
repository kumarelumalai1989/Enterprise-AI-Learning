# Package

## What is a package?
* A package is a directory/folder that groups related python modules together, making large applications easier to organize, maintain and scale.
* ```
   One Python file
      ↓
    Module
      ↓
    Many related Python files
      ↓
    Package
  ```
## Real Life Example
* Imagine a hospital
  ```
    Cardiology
    Neurology
    Dentistry
    Emergency
  ```
* Each department contains doctor.
  ```
     Hospital
        |
    Cardiology
        |
    Dr. Kumar
    Dr. Ravi

    Neurology
        |
    Dr. Priya
    Dr. John
  ``` 
  * Hospital = Project
    Department = Package
    Doctor = Module
## Module vs Package
* Module : Is a single file
  ```
  calculator.py
  ```
* Package : Is a collection of related files.
  ```
  utils/
  logger.py
  helper.py
  validator.py
  ```
## Enterprise AI Example
* Imagine Microsoft Copilot.
* Would microsoft keep everything in a single file?
  No. Probably something like this.
  ```
  EnterpriseAI/

  api/
      chat.py
      upload.py

  database/
      connection.py
      models.py

  services/
      embedding_service.py
      rag_service.py
      llm_service.py

  vectorstore/
      faiss.py
      pinecone.py

  utils/
      logger.py
      helper.py

  config/
      settings.py
  ```
* Now the project is organised.

## How Packages Work?
* Suppose we have package
  ```
  Utils\
  Maths_utils.py
  ``` 
  Inside Maths_utils.py file
  ```
  def square(n):
    return n*n
  ```
  Main File
  ```
  from Utils.Maths_utils import square

  print(square(5))
  ```
* Python first finds Utils -> Maths_utils -> square()

## What is __init__.py?
* Earlier versions of python required:
  ```
  Utils\

  __init__.py

  math_utils.py

  logger.py
  ```
* The __init__.py file told Python: This folder should be treated as a package.
* Nowadays (Python 3.3+), packages can often work without it bacause of namespace package.

## Why do we still use __init__.py?
1. Mark package initialization
   When the package is imported:
   ```
   </>
   import utils
   ```
   Python executes
   ```
   utils/__init__.py
   ```
2. Export selected functions
   * Suppose
    ```
    utils/
    math_utils.py
    string_utils.py
    ```
   * Instead of
    ```
    </>
    from utils.math_utils import add
    ```
   * you can expose add from __init__.py and write
    ```
    </>
    from utils import add
    ```
3. Run initialization code
   * Example:
    ```
    </>
    print('Loading Utilities...')
    ```
  * This runs once when the package is imported.

## How Python Imports a Package
* Suppose 
  ```
  </>
  from services.chat_service import generate_response
  ```
* Python does roughly this:
  ```
  Find services folder
         |
  Execute services/__init__.py (if present)
         |
  Find chat_service.py
         |
  Execute module
         |
  Return generate_response()
  ```

## Absolute Import
* Professional code usually prefers this.
  ```
  from service.chat_service import generate_response
  ```
* Easy to understand

## Relative Import
* Inside the same package.
  ```
  from .logger import log
  ```
  . means current package
* One level above
  ```
  from ..database.connection import connect
  ```
  .. means parent package

## Which Should We Use?
* For larger project, Prefer to use "Absolute Import" because it is easier to read and maintain
* Use relative imports only when they makge the package structure clearer.

## Advantages
1. Better organization
   * instead of 200 files
   * We have 10 packages and 20 files each
2. Easier Navigation
   * Need logging -> Go to 'utils/'
   * Need authentication -> Go to 'authentication/'
3. Better Team collaboration
   * Developer A -> 'services\'
   * Developer B -> 'authendication\'
   * Developer C -> 'api\'
4. Scalability
   * As a project grows, we can add new packages instead of dumping everything into a single folder.

## Can a Package Contain Another Package?
* yes.
* Example:
  ```
  services/
      llm/
        openai_service.py
        azure_service.py
      
      rag/
        retriever.py
        embedder.py
  ```
* Packages can be nested.