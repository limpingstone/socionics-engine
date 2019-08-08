#!/usr/bin/env python3
#
# graphics.py - By Steven Chen Hao Nyeo 
# Graphical interface for different personality types 
# Created: August 8, 2019

import wx
from cognitive_function import *
from entity import Entity
from value import Value
from strength import Strength
from consciousness import Consciousness
from function_to_type import Translator
from function_analysis import *

class TypeFrame(wx.Frame):
    def __init__(self, parent, title):
        
        # Create Frame
        wx.Frame.__init__(self, parent, title = title, size = (530, 480), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        self.panel = wx.Panel(self)
       
        self.entityList = []
        self.domButtons = []
        self.auxButtons = []
        self.rowCount = 0

        self.row_1_y = 30
        self.row_2_y = 90
        self.row_3_y = 150

        wx.StaticText(self.panel, label = "Dominant Function:", pos = (30, self.row_1_y - 20))
        self.createCogButtons(0)
        wx.StaticText(self.panel, label = "Auxiliary Function:", pos = (30, self.row_2_y - 20))
        self.createCogButtons(1)

    # The function that creates the buttons for the eight cognitive functions
    def createCogButtons(self, row):
        cogButtons = self.domButtons if row == 0 else self.auxButtons 
        labels = ["N", "S", "T", "F"]
        for i in range(4):   
            cogButtons.append(wx.Button(self.panel, label = labels[i] + "i", size = (50, 30) , pos = (30 + 120 * i, self.row_1_y if row == 0 else self.row_2_y)))
            cogButtons.append(wx.Button(self.panel, label = labels[i] + "e", size = (50, 30) , pos = (90 + 120 * i, self.row_1_y if row == 0 else self.row_2_y)))
        for i in range(8):
            self.Bind(wx.EVT_BUTTON, self.onclick_cogFunc, cogButtons[i])
        if (row == 1):
            for button in self.auxButtons:
                button.Disable()

    def onclick_cogFunc(self, event):
        btnLabel = event.GetEventObject().GetLabel()
        if (self.rowCount == 0):
            self.rowCount = 1
            self.entityList.append(self.labelToFunction(btnLabel))
            for button in self.domButtons:
                button.Disable()
            for button in self.auxButtons:
                if (button.Label[1] == self.entityList[0].opposite().sublabel 
                        and button.Label[0] != self.entityList[0].opposite_orientation().label
                        and button.Label[0] != self.entityList[0].label):
                    button.Enable()
        else:
            self.entityList.append(self.labelToFunction(btnLabel))
            for button in self.auxButtons:
                button.Disable()

        if (len(self.entityList) == 2):
            e = Entity(self.entityList)

            print(Translator.translate_orientation(e) +
                        Translator.translate_observing(e) +
                        Translator.translate_decision_making(e) +
                        Translator.translate_perception(e))

    def labelToFunction(self, btnLabel):
        if (btnLabel == "Ni"):                   
            return Ni
        elif (btnLabel == "Ne"): 
            return Ne
        elif (btnLabel == "Si"): 
            return Si
        elif (btnLabel == "Se"): 
            return Se
        elif (btnLabel == "Ti"): 
            return Ti
        elif (btnLabel == "Te"): 
            return Te
        elif (btnLabel == "Fi"): 
            return Fi
        elif (btnLabel == "Fe"):          
            return Fe

if __name__ == "__main__":
    app = wx.App()
    frame = TypeFrame(None, title = "Socionics Engine")
    frame.Show()
    app.MainLoop()
