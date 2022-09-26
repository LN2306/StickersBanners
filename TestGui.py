# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:18:25 2022

@author: tuong
"""

import PySimpleGUI as sg
import os
from readJob import read_file
from queueGenerator import queueGenerator
from printJob import print_Job, print_log, read_log

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
        [sg.Text(Sales._name), sg.Button("Full Queue", key ="{}FQ".format(Sales._ID)), sg.Button("Remove", key = "{}NQ".format(Sales._ID))],
         [sg.Text('Broker'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}B-".format(Sales._ID), enable_events=True),
         sg.Text('No File'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}NF-".format(Sales._ID), enable_events=True),
         sg.Text('Design Center'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}DC-".format(Sales._ID), enable_events=True)],
         [sg.Text('Regular'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}R-".format(Sales._ID), enable_events=True),
         sg.Text('No Proof'), sg.Combo(["100%", "75%", "50%", "25%", "0%"], default_value="100%", size=(5,5), key="-{}NP-".format(Sales._ID), enable_events=True)]
        ]
    return drop_down_layout   

def windowGenerator(Sales_list):   
    tab_group = [[sg.Text("Output Folder"), sg.Input(key="-OUT-"), sg.FolderBrowse("Browse")],
                [sg.TabGroup([[sg.Tab(sale._name, sale._layout) for sale in Sales_list]],
                tab_location='lefttop',
                title_color='Black', 
                tab_background_color='Green',
                selected_title_color='Black',
                selected_background_color='Yellow',
                border_width=5),
                [[sg.Button("Reimport"),
                  sg.Button("Export and Create File"),
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
     events, values = final_window.read()
     
     while True:
        events, values = final_window.read()

        if events == sg.WINDOW_CLOSED or events == "Exit":
            break
        
        elif events == "Reimport":
            if os.path.exists("log.txt"):
                save_path, save_list = read_log()
                for data in save_list:
                    if data in values:
                        values[data] = save_list[data]
                        final_window[data].update(save_list[data])
                values["-OUT-"] = save_path
            else:
                sg.PopupError("No Log Found")
                pass
            
        elif "FQ" in events:
            ID = events.strip("FQ")
            values["-{}B-".format(ID)] = "100%"
            values["-{}NF-".format(ID)] = "100%"
            values["-{}DC-".format(ID)] = "100%"
            values["-{}R-".format(ID)] = "100%"
            values["-{}NP-".format(ID)] = "100%"
            final_window["-{}B-".format(ID)].update("100%")
            final_window["-{}NF-".format(ID)].update("100%")
            final_window["-{}DC-".format(ID)].update("100%")
            final_window["-{}R-".format(ID)].update("100%")
            final_window["-{}NP-".format(ID)].update("100%")
            
        elif "NQ" in events:
            ID = events.strip("NQ")
            values["-{}B-".format(ID)] = "0%"
            values["-{}NF-".format(ID)] = "0%"
            values["-{}DC-".format(ID)] = "0%"
            values["-{}R-".format(ID)] = "0%"
            values["-{}NP-".format(ID)] = "0%"
            final_window["-{}B-".format(ID)].update("0%")
            final_window["-{}NF-".format(ID)].update("0%")
            final_window["-{}DC-".format(ID)].update("0%")
            final_window["-{}R-".format(ID)].update("0%")
            final_window["-{}NP-".format(ID)].update("0%")

        elif events == "Export and Create File":
            if (values["-OUT-"] == ""):
                sg.PopupError("No Output Folder")
            else:
                final_destination = values["-OUT-"]
                values.pop(0, None)
                values.pop('Browse', None)
                print_log(final_destination, values)
                if os.path.exists(final_destination):
                    print(final_destination)
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
                    print_Job(final_destination, Broker, NoFile, Design, Regular, NoProof)
                    sg.popup("Job.vb file has been created")
                else:
                    sg.PopupError("Invalid Output Folder")
        else:
            print (events, values[events])
            
     final_window.close()
     
if __name__ == '__main__':
    try:
        main()
    except TypeError:
        pass
