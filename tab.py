# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:05:31 2022

@author: tuong
"""

import PySimpleGUI as sg
from salesClass import Sales

contact_information_array = [['Amith', '31 Main St.', '6678989']]
headings = ["Full Name", 'Address', 'Phone Number']

def layoutGenerator(Sales):
    drop_down_layout = [
        [sg.Text(Sales._name)],
         [sg.Text('Broker'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}B-".format(Sales._ID), enable_events=True),
         sg.Text('No File'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}NF-".format(Sales._ID), enable_events=True),
         sg.Text('Design Center'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}DC-".format(Sales._ID), enable_events=True)],
         [sg.Text('Regular'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}R-".format(Sales._ID), enable_events=True),
         sg.Text('No Proof'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}NP-".format(Sales._ID), enable_events=True)]
        ]
    return drop_down_layout

Adri = Sales("Adriana", "A", 4, 4, 4, 4, 4)
Adri._layout = layoutGenerator(Adri)
Linh = Sales("Linh", "L", 4, 4, 4, 4, 4)
Linh._layout = layoutGenerator(Linh)
sales_list = [Adri, Linh]

tab_group = [[sg.TabGroup([[sg.Tab(sale._name, sale._layout) for sale in sales_list]],
                #sg.Tab('Adri', Adri._layout, background_color='Green'),
                #sg.Tab('Linh', Linh._layout, background_color='Green')]],
            tab_location='lefttop',
            title_color='White', 
            tab_background_color='Purple',
            selected_title_color='Green',
            selected_background_color='Yellow',
            border_width=2),
            sg.Button('Exit')
    ]] 

window = sg.Window('Contact Application with Tabs', tab_group)

while True:
    event,values=window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED():
        break
    if event == 'Submit Contact Information':
        contact_information_array.append([values['-NAME-'], values['-ADDRESS-'], values['-PHONE_NUMBER-']])
        window['-TABLE-'].update(values=contact_information_array)
window.close()