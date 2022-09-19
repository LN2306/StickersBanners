# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:56:31 2022

@author: tuong
"""

import os

def print_Job(file_name, Broker, No_File, Design, Regular, No_Proof):
    """
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        pass
    """
    f = open(file_name + "/" + "job.vb", 'w')
    f.write("Imports Microsoft.VisualBasic\n\n")
    f.write("Namespace TohCommonCode\n")
    f.write("  Public Class CommonCode\n\n")
    f.write("public Shared matrix1() As Single = New Single() {}\n\n".format(Broker))
    f.write("public Shared matrix2() As Single = New Single() {}\n\n".format(No_File))
    f.write("public Shared matrix3() As Single = New Single() {}\n\n".format(Design))
    f.write("public Shared matrix4() As Single = New Single() {}\n\n".format(Regular))
    f.write("public Shared matrix5() As Single = New Single() {}\n\n".format(No_Proof))
    f.write("  End Class\n")
    f.write("End Namespace\n")
