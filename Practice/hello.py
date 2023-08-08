import PySimpleGUI as sg

sg.theme('DarkAmber')

content = [
    [sg.Button('original')]
]

newButtons = [
    [sg.Button('new button 1')],
    [sg.Button('new button 2')]
]

layout = [
    [sg.Column(
        [
            [sg.Button('Thing 1', key='thing1')],
            [sg.Button('Thing 2', key='thing2')]
        ]
    ),
    sg.VSeparator(),
    sg.Column(content, key='content')]
]

window = sg.Window("Super app", layout).Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'thing1':
        print("thing1 pressed")
        window['content'].update(newButtons)
    if event == 'thing2':
        window['content'].update(newButtons)
window.close()
