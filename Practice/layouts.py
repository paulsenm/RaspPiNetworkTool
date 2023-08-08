import PySimpleGUI as sg

home = [
        [sg.Text("Some text on row 1")],
        [sg.Text("Enter thing: "), sg.InputText()],
        [sg.Button('Ok', key='ok'), sg.Button('Cancel', key='cancel')],
        [sg.Button('test', key='test')]
    ]

def test():
    return [
        [sg.Text('This is the test screen')],
        [sg.Button('Go Back', key='goBack')]
    ]

def thing1():
    return [
        [sg.Button('asdf 1'), sg.Button('asdf 2'), sg.Button('asdf 3')],
        [sg.Button('fdsa 1'), sg.Button('fdsa 2'), sg.Button('fdsa 3')],
        [sg.Button('qwer 1'), sg.Button('qwer 2'), sg.Button('qwer 3')]
    ]

def thing2():
    return [sg.Text('This is the thing 2 view, it\'s just text')]
    

def thing3():
    return [[]]

def topButtons():
    return [
    [sg.Button('Thing 1', key='thing1'), sg.Button('Thing 2', key='thing2'), sg.Button('Thing 3', key='thing3')],
    [sg.Column([], key='response')]  # Create an empty column with the key 'response'
]
