import tkinter as tk
import src.GUI.WindowUtil as wu
import src.GUI.learn.importModel as im
# import src.GUI.learn.createModel as cm


def goto_import_model(root):
    wu.change_window(root, im)


def goto_create_model(root):
    print("moving to cm")
    # wu.change_window(root, cm)


def entry(root):
    wu.resize(root, 300, 150)
    wu.add_button(root, "Import Model", lambda: goto_import_model(root))
    wu.add_button(root, "Create Model", lambda: goto_create_model(root))
