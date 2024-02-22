import os
import tkinter as tk
from tkinter import filedialog
import src.GUI.WindowUtil as wu
import src.GUI.learn.FriepawLearningMonitor as flm
import src.GUI.learn.ManageIntelligence as mi


def file_explorer(root, path, pretext):
    filename = filedialog.askopenfilename()
    wu.update_label(root, path, f"{pretext} {filename}")


def parse_path(path):
    path = wu.read_label(path)
    path = path.split("Path: ", 1)[-1].strip()  # Get everything after "Path: " and remove leading/trailing whitespaces
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path '{path}' does not exist.")
    return path


def goto_learn_platform(root, importPath, exportPath, errorBox):
    if wu.read_label(importPath) == "Import Path":
        wu.write_to_textbox(errorBox, "You must select an Import Path First")
    if wu.read_label(exportPath) == "Export Path":
        wu.write_to_textbox(errorBox, "You must select an Export Path First")

    try:
        importPath = parse_path(importPath)
    except FileNotFoundError:
        wu.write_to_textbox(errorBox, "Import Path is not a valid path.")
        return
    try:
        exportPath = parse_path(exportPath)
    except FileNotFoundError:
        wu.write_to_textbox(errorBox, "Import Path is not a valid path.")
        return
    print("successful import. Woo!")
    # TODO: import intelligence
    # TODO: have export allow folder submissions
    flm.start_processes(root, mi.import_intelligence(importPath), exportPath)


def entry(root):
    wu.resize(root, 300, 300)
    importPath = wu.add_label(root, "Import Path")
    exportPath = wu.add_label(root, "Export Path")
    # TODO: stylize the text for overflow case
    wu.add_button(root, "Find Import", lambda: file_explorer(root, importPath, "Import Path:"))
    wu.add_button(root, "Find Export", lambda: file_explorer(root, exportPath, "Export Path:"))
    errorBox = None
    wu.add_button(root, "Launch", lambda: goto_learn_platform(root, importPath, exportPath, errorBox))
    errorBox = wu.add_text_box(root, 5)

