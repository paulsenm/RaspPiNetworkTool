import PySimpleGUI as sg

pane1 = [sg.Pane(
        [sg.Col(
            [
                [sg.Text('Pane1')]
            ]
        )]
)]

pane2 = [sg.Pane(
        [sg.Col(
            [
                [sg.Text('Pane2')]
            ]
        )]
)]

layout = [
    [sg.Col([pane1])], [sg.Col([pane2])]
]

window = sg.Window('Pane Test 2', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()