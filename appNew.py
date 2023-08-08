import PySimpleGUI as sg
import functions
import data

navCol = [
    [sg.Column(
        [
        [sg.Button('Configure New Dish', key='dishConfigBtn')],
        [sg.Button('Set Your IP', key='setIPBtn')],
        [sg.Button('Ping Connected Device', key='pingDeviceBtn')],
        [sg.Button('Upload Dish Configs', key='uploadConfigsBtn')]
        ]
    )]
]

col1 = [
    [sg.Column(
        [
            [sg.Text('some text')]
        ], 
        key='dishConfig'
    )]
]

col2 = [
    [sg.Column(
        [
            [sg.Text('some different text')]
        ], 
        key='setIP'
    )]
]

col3 = [
    [sg.Column(
        [
            [sg.Text('col3 text')]
        ],
        key='pingDevice'
    )]
]

col4 = [
    [sg.Column(
        [
            [sg.Text('col3 text')]
        ],
        key='uploadConfigs'
    )]
]


layout = [
    [navCol], [col1], [col2], [col3], [col4]
]

window = sg.Window('ShowHide test', layout).Finalize()
window.Maximize()
functions.hideCols(window)
# window['col1'].update(visible=False)
# window['col2'].update(visible=False)
# window['col3'].update(visible=False)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    for colName in data.colNames:
        if event == colName + 'Btn':
            functions.hideCols(window)
            functions.showCol(colName, window) 
    # if event == 'b1':
    #     functions.hideCols(window)
    #     functions.showCol('col1', window)
window.close()
