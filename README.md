# Coding Challenge
Prompts included followed by any implementation notes.

- Used Python 3.10.4
- Dependencies install with `python -m pip install -r requirements-dev.txt`
- Tests available through pytest run `pytest` in root directory. 

## 1) Database design
### Prompt:
*Design a set of SQL tables for one of our articles. Use one of our articles from odometer.com to get an idea of what data points we need to render the article itself (disregard other elements such as header, footer, sidebars, etc). Please include comments for fields that might be unclear. MySQL is the ideal database to target, but if you're not familiar with it, others are also acceptable.*

### Notes:
- Implementation in: `./DatabaseDesign`
- Design shown in the .png image file.
- SQL db was designed with drawSQL targeting MySQL. The prompt states to design a set of tables so I placed more emphasis on the overall design rather than writing a SQL query script.
- SQL script is included to generate the tables if need be

## 2) API interaction
### Prompt:
*Using Python or PHP, send HTTP requests to the following fake API endpoint (http://jsonplaceholder.typicode.com ) and 1) get the 200 most recent TODOs, 2) create a TODO, and 3) delete a TODO given an ID.*

### Notes:
- Implementation in: `./APIInteraction/api.py`
- Has a driver with a command line menu
- Public API interface accepts a lot of invalid data and throws back no errors treating it as valid.

## 3) Algorithms
### Prompt:
*Write a Python or PHP script which prints all the permutations of a string in alphabetical order. We consider that digits < upper case letters < lower case letters. The sorting should be performed in ascending order. Your program should accept a file as its first argument. The file contains input strings, one per line. Print to stdout the permutations of the string separated by comma, in alphabetical order.*

### Notes:
- Implementation in: `./Algorithms/algorithms.py`
- Assumptions:
    - Special characters are not allowed
    - Use of Python's builtin sort method is allowed (otherwise a merge sort would have been used)
    - Argument is from command line
- Optimizations may be able to be made by sorting at the same time as generating permutations

