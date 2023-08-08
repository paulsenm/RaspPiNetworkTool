import PySimpleGUI as sg

navCol = [
    [sg.Column(
        [
        [sg.Button('b1')],
        [sg.Button('b2')],
        [sg.Button('b3')]
        ]
    )]
]

col1 = [
    [sg.Column(
        [
            [sg.Text('some text')]
        ], 
        key='col1'
    )]
]

col2 = [
    [sg.Column(
        [
            [sg.Text('some different text')]
        ], 
        key='col2'
    )]
]

col3 = [
    [sg.Column(
        [
            [sg.Text('col3 text')]
        ],
        key='col3'
    )]
]


layout = [
    [navCol], [col1], [col2], [col3]
]

window = sg.Window('ShowHide test', layout).Finalize()
window.Maximize()
window['col1'].update(visible=False)
window['col2'].update(visible=False)
window['col3'].update(visible=False)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'b1':
        window['col2'].update(visible=False)
        window['col3'].update(visible=False)
        window['col1'].update(visible=True)
window.close()
