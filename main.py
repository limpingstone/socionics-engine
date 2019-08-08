#!/usr/bin/env python3
#
# main.py - By Steven Chen Hao Nyeo 
# Graphical interface for Socionics Engine 
# Created: August 8, 2019

import wx
from cognitive_function import *
from entity import Entity
from function_to_type import Translator
from function_analysis import *

class TypeFrame(wx.Frame):
    def __init__(self, parent, title):
        
        # Create Frame
        wx.Frame.__init__(self, parent, title = title, size = (530, 480), style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self)
      
        # The current list of cognitive functions entered into the system 
        self.entityList = []

        # Arrays containing the rows of buttons for dominant and auxiliary functions
        self.domButtons = []
        self.auxButtons = []

        # Keep track of the current row of buttons to enable
        self.rowCount = 0

        # Setup for program interface
        self.row_1_y = 30
        self.row_2_y = 90
        self.row_3_y = 150
        wx.StaticText(self.panel, label = "Dominant Function:", pos = (30, self.row_1_y - 20))
        self.createCogButtons(0)
        wx.StaticText(self.panel, label = "Auxiliary Function:", pos = (30, self.row_2_y - 20))
        self.createCogButtons(1)

    # The function that creates the buttons for the eight cognitive functions
    def createCogButtons(self, row):

        # Keeps track of creation of dominant or auxiliary buttons
        cogButtons = self.domButtons if row == 0 else self.auxButtons 
        
        # Create and bind the buttons to the event
        labels = ["N", "S", "T", "F"]
        for i in range(4):   
            cogButtons.append(wx.Button(self.panel, label = labels[i] + "i", size = (50, 30) , pos = (30 + 120 * i, self.row_1_y if row == 0 else self.row_2_y)))
            cogButtons.append(wx.Button(self.panel, label = labels[i] + "e", size = (50, 30) , pos = (90 + 120 * i, self.row_1_y if row == 0 else self.row_2_y)))
        for i in range(8):
            self.Bind(wx.EVT_BUTTON, self.onclick_cogFunction, cogButtons[i])

        # The auxiliary buttons are disabled before the dominant function is entered
        if (row == 1): 
            for button in self.auxButtons:
                button.Disable()

    # The event handler for clicking on the buttons
    def onclick_cogFunction(self, event):
        btnLabel = event.GetEventObject().GetLabel()

        # First row - dominant function
        if (self.rowCount == 0):

            # Disable the dominant function buttons
            self.rowCount = 1
            self.entityList.append(self.labelToFunction(btnLabel))
            for button in self.domButtons:
                button.Disable()

            # Re-enable the appropriate auxiliary function buttons
            for button in self.auxButtons:
                if (button.Label[1] == self.entityList[0].opposite().sublabel 
                        and button.Label[0] != self.entityList[0].opposite_orientation().label
                        and button.Label[0] != self.entityList[0].label):
                    button.Enable()

        # Second row - auxiliary function
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

    # The helper functin that returns the corresponding function object according to the entered string
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
