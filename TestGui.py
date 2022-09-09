# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:18:25 2022

@author: tuong
"""

import PySimpleGUI as sg
from readJob import read_file
from queueGenerator import queueGenerator
from printJob import print_Job

def extraction(drop_down_dict, sales_list):
    for sales in sales_list:
        sales._broker = drop_down_dict["-{}B-".format(sales._ID)]
        sales._no_file = drop_down_dict["-{}NF-".format(sales._ID)]
        sales._design = drop_down_dict['-{}DC-'.format(sales._ID)]
        sales._reg = drop_down_dict['-{}R-'.format(sales._ID)]
        sales._no_proof = drop_down_dict['-{}NP-'.format(sales._ID)]
    return sales_list

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


def windowGenerator(Sales_list):   
    
    tab_group = [[sg.TabGroup([[sg.Tab(sale._name, sale._layout) for sale in Sales_list]],
                tab_location='lefttop',
                title_color='White', 
                tab_background_color='Purple',
                selected_title_color='Green',
                selected_background_color='Yellow',
                border_width=5),
                [[sg.Button("Export and Create File"),
                sg.Button("Exit")]]
        ]] 
    
    window = sg.Window("Frequency Setup", tab_group, finalize=True)
    for Sales in Sales_list:
        window["-{}B-".format(Sales._ID)].bind('<KeyRelease>', 'KEY DOWN')
        window["-{}NF-".format(Sales._ID)].bind('<KeyRelease>', 'KEY DOWN')
        window["-{}DC-".format(Sales._ID)].bind('<KeyRelease>', 'KEY DOWN')
        window["-{}R-".format(Sales._ID)].bind('<KeyRelease>', 'KEY DOWN')
        window["-{}NP-".format(Sales._ID)].bind('<KeyRelease>', 'KEY DOWN')
    return window
   
def main():
     Sales_list = read_file("sales.txt")
     for sale in Sales_list:
         sale._layout = layoutGenerator(sale)
     final_window = windowGenerator(Sales_list)
         
     while True:
        events, values = final_window.read()

        if events == sg.WINDOW_CLOSED or events == "Exit":
            break
        elif events == "Export and Create File":
            for key in values:
                if values[key] == "100%":
                    values[key] = 4
                elif values[key] == "75%":
                    values[key] = 3
                elif values[key] == "50%":
                    values[key] = 2
                elif values[key] == "25%":
                    values[key] = 1
                else:
                    values[key] = 0
            final_sales_list = extraction(values, Sales_list)
            Broker = queueGenerator(final_sales_list, "B")
            NoFile = queueGenerator(final_sales_list, "NF")
            Design = queueGenerator(final_sales_list, "DC")
            Regular = queueGenerator(final_sales_list, "R")
            NoProof = queueGenerator(final_sales_list, "NP")
            print_Job("job.txt", Broker, NoFile, Design, Regular, NoProof)
        else:
            print (events, values[events])
            
     final_window.close()
     
if __name__ == '__main__':
    try:
        main()
    except TypeError:
        pass
