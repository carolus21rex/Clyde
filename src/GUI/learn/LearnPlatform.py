# feature list:
# - Initiation, via import or via setup
# - Automatic Export
# - Live settings: number of shuffles per episode, Duty Cycle, Current temperature, learn rate
# - Live updates on the best model ratings as well as the 10 most recent
# - Pause and play
#
import random
import time
import tkinter as tk
import src.GUI.learn.Temperature as temp
import src.GUI.WindowUtil as wu


# When pressing the pause button this is called.
# procedural logic
def toggle_pause(pause_button, pause):
    p = pause.value
    p *= -1
    pause.value = p
    if p > 0:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")


# Makes all necessary modifications to the window
# TODO Break labels, text boxes, and buttons into their own functions
# procedural logic
def addGizmos(root, data):
    # sliders
    gizmos = {'duty_cycle': wu.add_slider(root, "Duty Cycle", 1, 0),
              'temperature_threshold': wu.add_slider(root, "Temperature Threshold (C)", 100, 0),
              'export_rate': wu.add_slider(root, "Export Rate", 1, 0),
              'shuffle_quantity': wu.add_slider(root, "Shuffle Quantity", 1, 0),
              'learning_rate': wu.add_slider(root, "Learning Rate", .00001, 0),
              'temperature_label': wu.add_label(root, "")}

    # text boxes
    wu.add_label(root, "Best Model")
    gizmos['best_model_textbox'] = wu.add_text_box(root, 1)
    wu.add_label(root, "Prev Model")
    gizmos['prev_models_textbox'] = wu.add_text_box(root, 9)

    # button
    gizmos['pause_button'] = None
    gizmos['pause_button'] = wu.add_button(root, "Resume", lambda: toggle_pause(gizmos['pause_button'], data['pause']))

    return gizmos


# Updates temperature on the GUI
# procedural logic
def update_temp(root, label, tempr):
    wu.update_label(root, label, tempr.decode())


# Reads all sliders on the GUI and stores the values in the data dictionary.
# procedural logic
def readGui(giz, data):
    data['duty_cycle'] = giz['duty_cycle'].get()
    data['temperature_threshold'] = giz['temperature_threshold'].get()
    data['export_rate'] = giz['export_rate'].get()
    data['shuffle_quantity'] = giz['shuffle_quantity'].get()
    data['learning_rate'] = giz['learning_rate'].get()


# Used in place of the standard main loop at ~ 10 FPS. Updates the window.
# recursive procedural logic
def custom_mainloop(giz, root, data):
    wu.write_to_textbox(giz['best_model_textbox'], data['best_text'].value.decode())
    wu.write_to_textbox(giz['prev_models_textbox'], data['prev_text'].value.decode())
    update_temp(root, giz['temperature_label'], data['temperature_text'].value)
    readGui(giz, data)
    root.after(100, custom_mainloop, giz, root, data)


# Initializes the Learning GUI
# procedural logic
def init_window(data):
    root = wu.create_gui()
    wu.resize(root, 400, 650)
    giz = addGizmos(root, data)
    root.after(0, custom_mainloop, giz, root, data)
    root.mainloop()


# Defunct method used for debugging
# procedural logic
def update_text(data, stop_flag):
    while not stop_flag.is_set():
        if data['pause'].value < 0:
            data['prev_text'].value = (f"Random Previous Models: {str(random.randint(1, 100))}\n"
                                       f"Random Previous Models: {str(random.randint(1, 100))}\n"
                                       f"test\ntest\ntest\ntest\ntest\ntest\ntest").encode()
            data['best_text'].value = ("Random Best Model: " + str(random.randint(1, 100))).encode()
            data['temperature_text'].value = f"Temperature: {temp.getTemp()}".encode()
        time.sleep(0.09)
