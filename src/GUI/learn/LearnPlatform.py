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
import multiprocessing as mp
import temperature as temp


# used for sliders, so they look right
# functional logic: returns rounded value to the nearest resolution
def snap_to_resolution(value, res):
    min_val = res.cget("from")
    max_val = res.cget("to")
    res = (max_val - min_val) / 100.0
    return round(value/res)*res


# calls snap_to_release. Could be inlined.
# procedural logic
def on_slider_release(value, slider):
    slider.set(snap_to_resolution(value, slider))


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


# Creates the sliders on screen.
# TODO eradicate the if case logic for better readability
# functional logic: returns a cookie cutter slider
def create_slider(parent, label_text):
    frame = tk.Frame(parent, bg="black")
    frame.pack(fill=tk.X, padx=10, pady=5)

    label = tk.Label(frame, text=label_text, bg="black", fg="white")
    label.pack(side=tk.LEFT)
    if label_text == "Learning Rate":
        slider = tk.Scale(frame, from_=0, to=0.01, orient=tk.HORIZONTAL, length=200, resolution=0.0001, bg="black", fg="white")
    else:
        slider = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, length=200, resolution=1, bg="black", fg="white")
    slider.pack(side=tk.RIGHT)

    slider.bind("<ButtonRelease-1>", lambda event: on_slider_release(slider.get(), slider))
    return slider


# Writes best and previous strings to the screen from the data dictionary
# procedural logic
def write_to_text_boxes(best_model_text, best_text, prev_models_text, prev_text):
    best_model_text.delete(1.0, tk.END)
    best_model_text.insert(tk.END, best_text.value)

    prev_models_text.delete(1.0, tk.END)
    prev_models_text.insert(tk.END, prev_text.value)


# Makes all necessary modifications to the window
# TODO Break labels, text boxes, and buttons into their own functions
# procedural logic
def addGizmos(root, data):
    # sliders
    gizmos = {'duty_cycle': create_slider(root, "Duty Cycle"),
              'temperature_threshold': create_slider(root, "Temperature Threshold (C)"),
              'export_rate': create_slider(root, "Export Rate"),
              'shuffle_quantity': create_slider(root, "Shuffle Quantity"),
              'learning_rate': create_slider(root, "Learning Rate"),
              'temperature_label': tk.Label(root, text="Original Text", fg="white", bg="black")}


    # label
    gizmos['temperature_label'].pack()

    # text boxes
    best_model_label = tk.Label(root, text="Best Model", fg="white", bg="black")
    best_model_label.pack(padx=10, pady=(10, 5), anchor="w")

    gizmos['best_model_text'] = tk.Text(root, height=1, width=40, fg="white", bg="black")
    gizmos['best_model_text'].pack(padx=10, pady=(0, 5), anchor="w")

    prev_models_label = tk.Label(root, text="Previous Models", fg="white", bg="black")
    prev_models_label.pack(padx=10, pady=(10, 5), anchor="w")

    gizmos['prev_models_text'] = tk.Text(root, height=9, width=40, fg="white", bg="black")
    gizmos['prev_models_text'].pack(padx=10, pady=(0, 5), anchor="w")

    # button
    gizmos['pause_button'] = tk.Button(root, text="Pause" if data['pause'] == 1 else "Resume",
                                       command=lambda: toggle_pause(gizmos['pause_button'], data['pause']))
    gizmos['pause_button'].pack(padx=10, pady=10)

    return gizmos


# Creates the gui and posts on screen
# TODO Handle Settings
# functional logic: returns TK window
def create_gui():
    root = tk.Tk()
    root.title("Clyde's Talking Window")
    root.geometry("400x600")
    root.config(bg="black")  # Set background color to dark

    return root


# Updates temperature on the GUI
# procedural logic
def update_temp(label, tempr):
    label.config(text=f"Temperature: {tempr.decode()} C")


# reads all sliders on the GUI and stores the values in the data dictionary.
# procedural logic
def readGui(giz, data):
    data['duty_cycle'] = giz['duty_cycle'].get()
    data['temperature_threshold'] = giz['temperature_threshold'].get()
    data['export_rate'] = giz['export_rate'].get()
    data['shuffle_quantity'] = giz['shuffle_quantity'].get()
    data['learning_rate'] = giz['learning_rate'].get()


def custom_mainloop(giz, rot, data):
    write_to_text_boxes(giz['best_model_text'], data['best_text'], giz['prev_models_text'], data['prev_text'])
    update_temp(giz['temperature_label'], data['temperature_text'].value)
    readGui(giz, data)
    # Schedule this function to be called again after 1000 milliseconds (1 second)
    rot.after(100, custom_mainloop, giz, rot, data)


def make_window(data):
    rot = create_gui()
    giz = addGizmos(rot, data)
    rot.after(0, custom_mainloop, giz, rot, data)
    rot.mainloop()


def update_text(data, stop_flag):
    while not stop_flag.is_set():
        data['prev_text'].value = (f"Random Previous Models: {str(random.randint(1, 100))}\n"
                                   f"Random Previous Models: {str(random.randint(1, 100))}\n"
                                   f"test\ntest\ntest\ntest\ntest\ntest\ntest").encode()
        data['best_text'].value = ("Random Best Model: " + str(random.randint(1, 100))).encode()
        data['temperature_text'].value = temp.getTemp().encode()
        time.sleep(0.09)


def start_processes():
    shared_data = {
        # data going to the window
        'prev_text': mp.Array('c', 255),  # string length 255
        'best_text': mp.Array('c', 255),
        'temperature_text': mp.Array('c', 50),
        # data coming from the window
        'pause': mp.Value('i', 1),
        'duty_cycle': mp.Value('i', 50),
        'temperature_threshold': mp.Value('i', 80),
        'export_rate': mp.Value('i', 10),
        'shuffle_quantity': mp.Value('i', 5),
        'learning_rate': mp.Value('i', 100)
    }

    # Create a flag to signal the random_text function to stop
    stop_flag = mp.Event()

    # Create a process for running make_window
    window_process = mp.Process(target=make_window, args=(shared_data,))
    window_process.start()

    # Run random_text in a separate process
    random_text_process = mp.Process(target=update_text, args=(shared_data, stop_flag))
    random_text_process.start()

    # Wait for the window process to finish
    window_process.join()

    # Set the flag to signal the random_text function to stop
    stop_flag.set()

    # Wait for the random_text process to finish
    random_text_process.join()


if __name__ == "__main__":
    start_processes()
