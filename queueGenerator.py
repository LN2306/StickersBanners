# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:53:04 2022

@author: tuong
"""
from salesClass import Sales

def queueGenerator(sales_list, queueType):
    MAIN_COUNTER = 4
    final_queue = []
    if queueType == "B":
        while MAIN_COUNTER > 0:
            for sales_rep in sales_list:
                if sales_rep._broker > 0:
                    final_queue.append(int(sales_rep._ID))
                    sales_rep._broker -= 1
            MAIN_COUNTER -= 1
    elif queueType == "NF":
        while MAIN_COUNTER > 0:
            for sales_rep in sales_list:
                if sales_rep._no_file > 0:
                    final_queue.append(int(sales_rep._ID))
                    sales_rep._no_file -= 1
            MAIN_COUNTER -= 1
    elif queueType == "DC":
        while MAIN_COUNTER > 0:
            for sales_rep in sales_list:
                if sales_rep._design > 0:
                    final_queue.append(int(sales_rep._ID))
                    sales_rep._design -= 1
            MAIN_COUNTER -= 1
    elif queueType == "R":
        while MAIN_COUNTER > 0:
            for sales_rep in sales_list:
                if sales_rep._reg > 0:
                    final_queue.append(int(sales_rep._ID))
                    sales_rep._reg -= 1
            MAIN_COUNTER -= 1
    elif queueType == "NP":
        while MAIN_COUNTER > 0:
            for sales_rep in sales_list:
                if sales_rep._no_proof > 0:
                    final_queue.append(int(sales_rep._ID))
                    sales_rep._no_proof -= 1
            MAIN_COUNTER -= 1
    else:
        return "Queue Type not found"
    
    return ("{" + str(final_queue).strip("[").strip("]") + "}")
