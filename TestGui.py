# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:18:25 2022

@author: tuong
"""

import PySimpleGUI as sg
from salesClass import Sales



def layoutGenerator(Sales):
    drop_down_layout = [
        [sg.Text(Sales._name)],
         [[sg.Text('Broker'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-{}B-".format(Sales._ID), enable_events=True),
         sg.Text('No File'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-{}NF-".format(Sales._ID), enable_events=True),
         sg.Text('Design Center'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-{}DC-".format(Sales._ID), enable_events=True)],
         [sg.Text('Regular'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-{}R-".format(Sales._ID), enable_events=True),
         sg.Text('No Proof'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-{}NP-".format(Sales._ID), enable_events=True)]]
         
        ]
    return drop_down_layout


def windowGenerator(Sales_list, finalLayout):
    window = sg.Window("Frequency Choose", finalLayout, finalize = True)
    for Sales in Sales_list:
        window["-{}B-".format(Sales._ID)].bind('<KeyRelease>', 'KEY DOWN')
        window["-{}NF-".format(Sales._ID)].bind('<KeyRelease', 'KEY DOWN')
        window["-{}DC-".format(Sales._ID)].bind('<KeyRelease', 'KEY DOWN')
        window["-{}R-".format(Sales._ID)].bind('<KeyRelease', 'KEY DOWN')
        window["-{}NP-".format(Sales._ID)].bind('<KeyRelease', 'KEY DOWN')
    return window
   
def main():
     final_layout = []
     Adri = Sales("Adriana", 264136, 4, 4, 4, 4, 4)
     Linh = Sales("Linh", 257277, 4, 4, 4, 4, 4)
     Danny = Sales("Danny", 124482, 4, 4, 4, 4, 4)
     Ian = Sales("Ian", 217798, 4, 4, 4, 4, 4)
     Sales_list = [Adri, Linh, Danny, Ian]
     
     for sale in Sales_list:
         sale._layout = layoutGenerator(sale)
         final_layout.append(sale._layout)
         
     final_window = windowGenerator(Sales_list, final_layout)
         
     while True:
        events, values = final_window.read()
        print(events, values)
        if events == sg.WINDOW_CLOSED or events == "Exit":
            break
     final_window.close()
    
if __name__ == '__main__':
    main()
