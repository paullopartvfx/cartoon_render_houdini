########################################################################################################
# Version = 0.1
# 
# Content = Main app script. This is the first version, code style.
#
# Author =  Pau Llopart <paullopartvfx@gmail.com>
#######################################################################################################

import hou
import os
import sys

from PySide2.QtWidgets import QMessageBox
from PySide2 import QtWidgets, QtGui, QtUiTools

DIR_PATH = r'D:\Houdini\Python_Houdini_Advanced\cartoon render houdini'
UI_PATH  = DIR_PATH + "/04_ui/Cartoon_Render_UI_v01.ui"

class CartoonRender:
    def __init__(self):
        # Load UI
        self.wg_util = QtUiTools.QUiLoader().load(UI_PATH)

        # Connect buttons with function
        self.wg_util.btn_add.clicked.connect(self.press_add)
        self.wg_util.btn_delete.clicked.connect(self.press_delete)

        self.wg_util.show()
    
    # PRESS ---------------------------------------------------------------------------------------
    def press_add(self):
        obj = hou.node('obj')

        selected_nodes = hou.selectedNodes()

        for node in selected_nodes:
            name = node.name()
            self.wg_util.cbx_nodes.addItem(name)
            print("Imported: " + name)
    
    def press_delete(self):
        self.wg_util.cbx_nodes.clear()
        print("All assets are gone!")

# START --------------------------------------------------------------------------------------------
def start():
	global main_widget
	main_widget = CartoonRender()
     
start()