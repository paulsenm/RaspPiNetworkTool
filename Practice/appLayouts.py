import PySimpleGUI as sg

backCol = [
    [sg.Button('Back')],
    [sg.Text('Go Back')]
]

configTab = [
    [backCol]
]


home = [
    [sg.Tab('Configure Dish', configTab)]
]

home_nav_buttons = [
    sg.Button('Configure New Dish', key='configDish')
]