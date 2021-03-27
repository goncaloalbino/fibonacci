# Fibonacci Api

Fibonacci API:
 - `http://localhost:8000/fibonaccivalue` 
   - Methods available: 
     - `GET` Returns the value of a Fibonacci number for a given value. 
 - `http://localhost:8000/fibonaccivalues`
   - Methods available: 
     - `GET` Returns a list of numbers and the corresponding values from the Fibonacci sequence 
    from 1 to N with support to pagination.
 - `http://localhost:8000/blacklist`
   - Methods available: 
     - `POST` Blacklists a number. The number stops being showed on the Fibonacci results
     - `DELETE` Removes blacklisted number 

This readme explains how to start the application.

## Prepare the environment 

For this purpose all needed python packages listed on `requirements.txt` file have to be installed.
Start by creating an isolated environment and install all the dependencies.
Using `virtualenv` that can be done following the steps:
```sh
virtualenv --python=python3 venv
```
Start the new environment:
```sh
source ven/bin/activate
```
Install all the required dependencies, from the project root directory run:
```sh
pip install -r requirements.txt
```

## How to run the service
In a virtual environment with a Python 3.6+ interpreter and all the dependencies installed, from the project root, 
run the application: 
```pyhton
python fibonacci_app.py
```

## Test the endpoints
Endpoints are accessible on `http://localhost:8000/ui/`. From there is possible to check the 
endpoints description and test all its functionalities. 

To get a Fibonacci value: `http://localhost:8000/ui/#/default/api.fibonacci.fibonacci_value`
 - Parameters:
   - `number` Number from Fibonacci sequence. Only accepts values equal or higher than 1 
    
To get the Fibonacci values for a page: `http://localhost:8000/ui/#/default/api.fibonacci.fibonacci_values`
 - Parameters:
   - `page` Page number for paginate the resulting sequence. `Default` 1. 
   - `items_per_page` Number of items shown per page. `Default` 100. 
    
Blacklist number: `http://localhost:8000/ui/#/default/api.fibonacci.blacklist_add`
 - Parameters:
   - `number` Number to be blacklisted. Minimum 1.
    
Remove blacklist number: `http://localhost:8000/ui/#/default/api.fibonacci.blacklist_remove`
 - Parameters:
   - `number` Number to be removed from blacklist. Minimum 1.

## Running the unit tests

To run the developed unit tests, from the root directory, run:

```
python3 test/suite.py
```

## Codestyle
For codestyle verification, from the root directory, run:
```
flake8 --max-line-length 99 api/ fibonacci_app.py test/
```
