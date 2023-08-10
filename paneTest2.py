import PySimpleGUI as sg

navCol = [
    [sg.Button('Button1')],
    [sg.Button('Button2')]
]

pane1 = sg.Pane(
    [
        sg.Col(
            [
                [sg.Text('Pane1')]
            ]
        )
    ]
)

pane2 = sg.Pane(
        [
            sg.Col(
                [
                    [sg.Text('Pane2')]
                ]
            )
        ],
        key='pane2'
    )


mainCol = [
    [
        pane1,
        pane2
    ]
]

layout = [

        navCol,
        [sg.Column(mainCol)]


]

window = sg.Window('Pane Test 2', layout, resizable=True, size=(600,600))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()