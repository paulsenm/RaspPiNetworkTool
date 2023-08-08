#!/usr/bin/env python
import sys
import PySimpleGUI as sg
sg.set_options(font=('Arial Bold', 40))
# import PySimpleGUIWeb as sg

# Usage of Tabs in PSG
#
# sg.set_options(background_color='cornsilk4',
#         element_background_color='cornsilk2',
#         input_elements_background_color='cornsilk2')

sg.theme('Light Green 5')

tab1_layout = [
                [sg.Column(
                    [
                        [sg.Text('Configure Dish', background_color='darkslateblue', text_color='white')],
                        [sg.Input(key='-configDish-')]
                    ]
                )]

            ]

tab2_layout = [
                [sg.Text('This is inside tab 2', background_color='tan1')],
                [sg.Input(key='-in2-')]
            ]


tab3_layout = [
                [sg.Text('This is inside tab 3')],
                [sg.Input(key='-in2-')]
            ]

tab4_layout = [[sg.Text('This is inside tab 4', background_color='darkseagreen')],
               [sg.Input(key='-in3-')]]

tab5_layout = [[sg.Text('This is inside tab 5')],
               [sg.Input(key='-in4-')]]


layout = [
    [sg.TabGroup(
        [
            [
                sg.Tab('Configure Dish', tab1_layout, background_color='lightgray', key='-mykey-', pady=20, expand_x=True),
                sg.Tab('Set IP', tab2_layout, background_color='lightgray', expand_x=True),
                sg.Tab('Ping Dish', tab3_layout, background_color='lightgray', expand_x=True)
            ]
        ], 
        key='-group2-', 
        title_color='red', 
        selected_title_color='green',
        tab_location='left',
        size=(800, 800),
        expand_x=True,
        
        ),
            #    sg.TabGroup([[sg.Tab('Tab 4', tab4_layout, background_color='darkseagreen', key='-mykey-'),
            #                  sg.Tab('Tab 5', tab5_layout)]], key='-group1-', tab_location='top', selected_title_color='purple')],
    ],
            #   [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, background_color='darkslateblue', key='-mykey-'),
            #                  sg.Tab('Tab 2', tab2_layout, background_color='tan1'),
            #                  sg.Tab('Tab 3', tab3_layout)]],
            #                key='-group3-', title_color='red',
            #                selected_title_color='green', tab_location='left'),
            #    sg.TabGroup([[sg.Tab('Tab 4', tab4_layout, background_color='darkseagreen', key='-mykey-'),
            #                  sg.Tab('Tab 5', tab5_layout)]], key='-group4-', tab_location='bottom', selected_title_color='purple')],
    [sg.Button('Read')]
]

window = sg.Window('My window with tabs', layout).Finalize()
window.Maximize()


while True:
    event, values = window.read()
    sg.popup_non_blocking(event, values)
    print(event, values)
    if event == sg.WIN_CLOSED:           # always,  always give a way out!
        break
window.close()