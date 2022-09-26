# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:56:31 2022

@author: tuong
"""
import os
import json

def print_Job(file_name, Broker, No_File, Design, Regular, No_Proof):
    f = open(file_name + "/" + "job.vb", 'w')
    f.write("Imports Microsoft.VisualBasic\n\n")
    f.write("Namespace TohCommonCode\n")
    f.write("  Public Class CommonCode\n\n")
    f.write("    public Shared matrix1() As Single = New Single() {}\n\n".format(Broker))
    f.write("    public Shared matrix2() As Single = New Single() {}\n\n".format(No_File))
    f.write("    public Shared matrix3() As Single = New Single() {}\n\n".format(Design))
    f.write("    public Shared matrix4() As Single = New Single() {}\n\n".format(Regular))
    f.write("    public Shared matrix5() As Single = New Single() {}\n\n".format(No_Proof))
    f.write("  End Class\n")
    f.write("End Namespace\n")
    
def print_log(save_path, sales_queue):
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    else:
        pass
    f = open("log.txt", 'w')
    f.write("PATH: {}\n".format(save_path))
    f.write("SALES: {}".format(sales_queue))
    
def read_log():
    f = open("log.txt", 'r')
    content = f.readlines()
    save_path = content[0].strip("PATH: ").rstrip()
    save_list = content[1].strip("SALES: ")
    converted = save_list.replace("'", "\"")
    final_save = json.loads(converted)
    return(save_path, final_save)
    