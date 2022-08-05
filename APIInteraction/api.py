from urllib.error import HTTPError
import requests
import pprint

API_URL = "https://jsonplaceholder.typicode.com"
API_TODO_ENDPOINT = "/todos"
HEADERS = {"Content-type": "application/json; charset=UTF-8"}

def get_todos() -> dict:
    """
    Get all todos from the API endpoint. Raises an HTTPError if status code >= 400.
    """
    req = requests.get(API_URL + API_TODO_ENDPOINT, headers=HEADERS)
    
    req.raise_for_status()
    return req.json()

def create_todo(user: int, title: str, completed: bool = False) -> dict:
    """
    Create a todo from the passed parameters.

    Defaults completed to False.

    Raises an HTTPError if status code >= 400.
    Raises TypeError if passed parameters are invalid.
    """
    req = None
    try:
        req = requests.post(API_URL + API_TODO_ENDPOINT, json={
            "title": title,
            "userId": user,
            "completed": completed,
        }, headers=HEADERS)
    except TypeError:
        if req == None:
            raise TypeError("Malformed data. Cannot serialize as JSON.")
        else:
            raise
        
    req.raise_for_status()
    return req.json()

def delete_todo(id: int) -> int:
    """
    Deletes a todo based on its id. Returns success status code if successful.
    Raises an HTTPError if status code >= 400.
    """
    req = requests.delete(API_URL + API_TODO_ENDPOINT + f"/{id}", headers=HEADERS)
    
    req.raise_for_status()
    return req.status_code


if __name__ == "__main__":
    """
    Small driver script to execute functions.
    """
    req = 0
    while req != 4:
        print("1) get 200 todos.")
        print("2) create todo")
        print("3) delete a todo")
        print("4) quit")
        try:
            req = int(input(">>> "))
        except ValueError:
            print("Enter an integer")
            continue
        
        if req == 1:
            todos = get_todos()
            pprint.pprint(todos)

        elif req == 2:
            user = input("user id: ")
            title = input("title: ")

            completed = None
            while completed is None:
                completed = input("completed? (y/n): ").lower()[0]
                if completed == "y":
                    completed = True
                elif completed == "n":
                    completed = False
            
            try:
                todo = create_todo(user, title, completed)
            except HTTPError as e:
                print(f"Ecountered HTTP Error: {e.code}")
            except TypeError as e:
                print(e)

            if todo is not None:
                print("Your todo:")
                pprint.pprint(todo)

        elif req == 3:
            todo_id = input("todo id: ")
            res = None

            try:
                res = delete_todo(todo_id)
            except HTTPError as e:
                print(f"Ecountered HTTP Error: {e.code}")
            
            if res is not None:
                print(f"Success! Code {res}")
        
        elif req == 4:
            break
        
        print("\n")
