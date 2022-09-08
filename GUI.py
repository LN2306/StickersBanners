# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:41:39 2022

@author: tuong
"""
import PySimpleGUI as sg

def main():

    DROP_DOWN_LAYOUT1 = [
         [sg.Text('Adriana')],
         [sg.Text('Broker'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-B-", enable_events=True),
         sg.Text('No File'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-NF-", enable_events=True),
         sg.Text('Design Center'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-DC-", enable_events=True)],
         [sg.Text('Regular'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-R-", enable_events=True),
         sg.Text('No Proof'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-NP-", enable_events=True)],
         sg.Text('Adriana')
        ]
    
    DROP_DOWN_LAYOUT2 = [
         [sg.Text("Linh")],
         [sg.Text('Broker'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-B-", enable_events=True),
         sg.Text('No File'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-NF-", enable_events=True),
         sg.Text('Design Center'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-DC-", enable_events=True)],
         [sg.Text('Regular'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-R-", enable_events=True),
         sg.Text('No Proof'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], size=(5,5), key="-NP-", enable_events=True)]
        ]
    
    DROP_DOWN_LAYOUT = [DROP_DOWN_LAYOUT1,DROP_DOWN_LAYOUT2]
    
    window = sg.Window('Window Title', DROP_DOWN_LAYOUT, finalize = True)
    window['-B-'].bind('<KeyRelease>', 'KEY DOWN')
    window['-NF-'].bind('<KeyRelease>', 'KEY DOWN')
    window['-DC-'].bind('<KeyRelease>', 'KEY DOWN')
    window['-R-'].bind('<KeyRelease>', 'KEY DOWN')
    window['-NP-'].bind('<KeyRelease>', 'KEY DOWN')

    while True:
        events, values = window.read()
        print(events, values)
        if events == sg.WINDOW_CLOSED or events == "Exit":
            break
        """
        if events == "-B-KEY DOWN":
            window["-B-"].Widget.event_generate('<Down>')
        elif events == "-NF-KEY DOWN":
            window["-NF-"].Widget.event_generate('<Down>')
        """
    window.close()
if __name__ == '__main__':
    main()
    #Sales_layout = [sg.Text('Adriana'), DROP_DOWN_LAYOUT]