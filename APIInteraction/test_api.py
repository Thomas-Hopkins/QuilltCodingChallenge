from . import api
import pytest

def test_get_todos():
    todos = api.get_todos()
    assert isinstance(todos, list)
    assert len(todos) == 200

def test_create_todo():
    todo1 = api.create_todo(user=1, title="hello")
    assert todo1
    assert todo1["title"] == "hello"
    assert todo1["userId"] == 1
    assert todo1["completed"] == False

    with pytest.raises(TypeError):
        api.create_todo(user=1, title=object())

    # API still accepts users that don't exist
    todo3 = api.create_todo(user=20_000_000, title="hello")
    assert todo3
    assert todo3["title"] == "hello"
    assert todo3["userId"] == 20_000_000
    assert todo3["completed"] == False

    # API still accepts users that don't and can't exist
    todo4 = api.create_todo(user=-100, title="hello")
    assert todo4
    assert todo4["title"] == "hello"
    assert todo4["userId"] == -100
    assert todo4["completed"] == False

    todo5 = api.create_todo(user=1, title="", completed=True)
    assert todo5
    assert todo5["title"] == ""
    assert todo5["userId"] == 1
    assert todo5["completed"] == True

def test_delete_todo():
    todo1 = api.delete_todo(1)
    assert todo1 == 200

    # API still accepts posts that don't exist
    todo1 = api.delete_todo(20_000_000)
    assert todo1 == 200

    # API still accepts posts that don't and can't exist
    todo1 = api.delete_todo(-200)
    assert todo1 == 200
