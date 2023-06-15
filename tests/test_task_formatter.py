from unittest.mock import Mock
from lib.task_formatter import TaskFormatter

# format returns complete task formatted as a string 

def test_formatted_returns_complete_task_as_string():
    task = Mock()
    task.title = "wash the floor" 
    task.complete = True
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "[x] wash the floor"

def test_formatted_returns_incomplete_task_as_string():
    task = Mock()
    task.title = "wash the floor" 
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "[] wash the floor"

