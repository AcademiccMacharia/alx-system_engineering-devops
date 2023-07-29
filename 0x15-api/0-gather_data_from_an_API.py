#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    
    user = "{}users/{}".format(url, sys.argv[1]);
    result = requests.get(user)
    res = result.json()
    print("Employee {} is done with tasks".format(res.get('name')), end="")

    todos = "{}todos?userId={}".format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in tasks:
        print("\t {}".format(task.get("title")))
