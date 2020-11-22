# There are two ways to define a dictionary in python
# one is using the curly brace
# the other is using the dict() function
# using the second method you assign values to keys
# by using '=' sign

# Some examples
# Using curly braces
personal_todos = [
    {
        "name": "Do some python list excerisces",
        "due_date": "20201908",
        "priority": "medium",
        "completed": True,
        "sub_tasks": []
    },
    {
        "name": "Develope songbook",
        "due_date": "20201304",
        "priority": "high",
        "completed": False,
        "sub_tasks": [
            {
                "name": "Design UI",
                "due_date": "20200909",
                "priority": "medium",
                "completed": True,
                "sub_tasks": ["something is missing!"]
            }
        ]
    }
]

# Accessing the dict
print(personal_todos)
# Accessing indvidual items in the dict
print(personal_todos[1]["sub_tasks"][0]["sub_tasks"][0][0:13:] + '...')

# Using the dict keyword
work_todo = dict(name='Lab clean up', date='20200808', priority='high')
print(work_todo)

macs = [
'a4-1f-72-63-73-d3','a4-1f-72-63-86-06','18-03-73-e6-13-95','a4-1f-72-64-63-b7','a4-1f-72-63-87-f1','a4-1f-72-63-7d-2e','18-03-73-ee-14-1e','a4-1f-72-61-77-34','d4-be-d9-9d-31-3c','a4-1f-72-63-89-2c','a4-1f-73-63-a9-50','18-03-73-e2-a6-d1','a4-1f-72-64-03-b5','18-03-73-e2-8d-37','a4-1f-72-61-ab-06',
'a4-1f-72-64-53-25','d4:be:d9:9d:2e:36','d4-be-d9-9d-2e-05','a4-1f-72-63-73-57'
]

for mac in macs:
    mac.replace('-', ':')

print(macs)
