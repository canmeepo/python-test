todo = {
    'work': 'today',
    'sleep': 'tomorrow'
}

print(todo['work'])

todo['eat'] = 'now'

print(todo)

del todo['sleep']
print(todo)

print('work' in todo.keys())


cars = {
    'n': {
        'n1': True,
        'n2': 12,
        'n3': 'String'
    },
    "x": {
        'x1': False
    }
}

print(cars)
print(cars['n']['n3'])