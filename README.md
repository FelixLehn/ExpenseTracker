# ExpenseTracker
This is a description of what the ExpenseTracker does.

## Description
To start the ExpenseTracker, go to the directoy src/main/python and run this code after installation of the requirements.txt: 

```python
python main.py
```

## UML Diagrams
The Diagrams can be found in here: 
https://github.com/FelixLehn/ExpenseTracker/tree/main/docs/UML

## DDD - Domain Driven Design
The DDD-Diagram and the descirption can be found in here: 
https://github.com/FelixLehn/ExpenseTracker/tree/main/docs/DDD

## Metrics
The metrics can be found in here: 
https://github.com/FelixLehn/ExpenseTracker/tree/main/docs/Sonarqube-Metriken

There are mainly Screenshots from the ExpenseTracker, before and after the final implementation. Another bigger project can also be found in this folder, a SonarQube Metric of an Anonymization Tool. 


## Clean Code Development:
The Clean Code Cheet Sheet with code snippets as example from the code can be found in here: 
https://github.com/FelixLehn/ExpenseTracker/tree/main/docs/Clean_Code_Development

## Build Management
The Build Management can be found in here: 
- build.py https://github.com/FelixLehn/ExpenseTracker/blob/main/build.py
- setup.py https://github.com/FelixLehn/ExpenseTracker/blob/main/setup.py
- pyproject.toml https://github.com/FelixLehn/ExpenseTracker/blob/main/pyproject.toml

It was created with the pybuilder. This is a powerful tool, which was created mainly for python and provides a build-automation.

In my build, there are several tasks to do:
- Checking the Python Version
- Checking the requirements
- Checking the Code Coverage
- Checking the Code against Code Style PEP8 
- Automating Unit-Tests

In my build, I set the coverage threshold and the parameter to not break the build by a not fullfilling coverage. The reason is, that in my code I don't fullfill the coverage of 75%. Thats because I don't intend to write tests for every code in my project. I think the most used and relevant functions should be tested. Of course it is recommended to test all the code, but in my opinion you need to do a trade-off between time and importance/usage. 


## Unit-Tests
The Unit-Tests can be found in here: 
https://github.com/FelixLehn/ExpenseTracker/tree/main/src/unittest/python

The Unit-Test package used in my code is the built-in module unittest. The modules for which a test-code is written are the 'budget.py', 'expense.py', 'help_functions.py' and 'viewer.py'. All of them except the 'help_functions.py' represent the core domains in the ExpenseTracker. The 'help_functions.py' represents functions which are often used in the whole application and are shared between the core domains. The tests get automatically started and are integrated in the build management. 

## Continous Delivery
The pipeline for the continoues delivery can be found in here: 
https://github.com/FelixLehn/ExpenseTracker/blob/main/.github/workflows/python-app.yml

The CD-pipeline is built with Github Actions. The tasks to be done are:
- set up ubuntu environment
- set up Python with Version 3.8
- installs or upgrades pip
- installs or upgrades flake8
- installs (if provided) the requirements.txt
- checks if there are syntax errors in python 
- runs the Unit-Tests 

## IDE
The IDE-Description can be found in here:
https://github.com/FelixLehn/ExpenseTracker/blob/main/docs/IDE

## DSL-Demo
The DSL-Demo can be found in here: https://github.com/FelixLehn/ExpenseTracker/blob/main/src/main/python/dsl_example.py
It uses the predefined Budget Class from the ExpenseTracker. 

## Functional Programming
The functional programming aspects and its examples can be found in here: 
https://github.com/FelixLehn/ExpenseTracker/blob/main/docs/Functional_Programming/FP_Aspects.md

