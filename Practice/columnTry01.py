#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Usage of Column Element

    How to embed a layout in a layout

    Copyright 2022 PySimpleGUI
'''

sg.theme('BlueMono')

# Column layout
col = [
    [
        sg.Text('col Row 1', text_color='white', background_color='blue')
    ],
]
# Window layout
layout = [
    [
        sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(200, 30)),
        sg.Column(col, background_color='blue')
    ],
    [sg.Input('Last input')],
    [sg.OK()]
]

# Display the window and get values
window = sg.Window('Column Element', layout, margins=(0, 0), element_padding=(0, 0))
event, values = window.read()


window.close()