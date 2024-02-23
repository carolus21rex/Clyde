import tkinter as tk
import src.GUI.learn.LearningInit as li
import src.GUI.WindowUtil as wu


def launch_learning(root):
    wu.change_window(root, li)


def launch_assessment(root):
    print("Has not been implemented")


def launch_application(root):
    print("Has not been implemented")


def init_window():
    root = wu.create_gui()
    wu.add_button(root, "Learning", lambda: launch_learning(root))
    wu.add_button(root, "Assess", lambda: launch_assessment(root))
    wu.add_button(root, "Apply", lambda: launch_application(root))
    root.mainloop()


if __name__ == "__main__":
    init_window()
