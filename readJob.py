# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:13:13 2022

@author: tuong
"""
from salesClass import Sales

def read_file(directory):
    job = open(directory , "r")
    content = job.readlines()
    job.close()
    sales_list = []
    for line in content:
        name, ID = line.split(" ")
        temp = Sales(name, ID.strip("\n") ,4,4,4,4,4)
        exec(name + " = temp")
        exec("sales_list.append(" + name + ")")
    return sales_list

sales_list = read_file("sales.txt")


    
