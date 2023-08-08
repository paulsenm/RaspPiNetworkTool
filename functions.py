import PySimpleGUI as pg
import data

def hideCols(window):
    for colName in data.colNames:
        window[colName].update(visible=False)
    # window['col1'].update(visible=False)
    # window['col2'].update(visible=False)
    # window['col3'].update(visible=False)

def showCol(colName, window):
    window[colName].update(visible=True)