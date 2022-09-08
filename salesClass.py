# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:21:19 2022

@author: tuong
"""

class Sales:
    def __init__(self, name, ID, broker, no_file, design, reg, no_proof):
        self._name = name
        self._ID = ID
        self._broker = broker
        self._no_file = no_file
        self._design = design
        self._reg = reg
        self._no_proof = no_proof
        self._layout = []
    
    @property
    def broker(self):
        return self._broker
    @broker.setter
    def broker(self, freq):
        self._broker = freq

    @property
    def no_file(self):
        return self._no_file
    @no_file.setter
    def no_file(self, freq):
        self._no_file = freq
        
    @property
    def design(self):
        return self._design
    @design.setter
    def design(self, freq):
        self._design = freq
        
    @property
    def reg(self):
        return self._req
    @reg.setter
    def reg(self, freq):
        self._reg = freq
        
    @property
    def no_proof(self):
        return self._no_proof
    @no_proof.setter
    def no_proof(self, freq):
        self._no_proof = freq
    
    @property
    def layout(self):
        return self._layout
    @layout.setter
    def layout(self, layout):
        self._layout = layout

Adri = Sales("Adriana", 123456, 4 ,4, 4, 4, 4)
print(Adri._broker)
print(Adri._ID)
print(Adri._name)
print(Adri._layout)