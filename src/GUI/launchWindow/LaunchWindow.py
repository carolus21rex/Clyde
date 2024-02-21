import tkinter as tk
import src.GUI.learn.ClydeLearningMonitor as clm


def create_gui():
    root = tk.Tk()
    root.title("Button Window")
    root.geometry("300x150")
    root.config(bg="black")
    return root


def button_pressed(button_num, root, pressed_button):
    pressed_button.set(button_num)
    root.destroy()


def add_buttons(root, pressed_button):
    button_texts = ["Learning", "Monopoly Money", "Live Launch"]
    for i, text in enumerate(button_texts, start=1):
        button = tk.Button(root, text=text, bg="black", fg="white",
                           command=lambda num=i: button_pressed(num, root, pressed_button))
        button.pack(pady=5, padx=10, fill=tk.X)


def launchSetting(choice):
    if choice == 1:
        clm.start_processes()
        return
    if choice == 2:
        print("Monopoly money was chosen. this has not been implemented.")
        return
    print("Live Launch was chosen. this has not been implemented.")


def init_window():
    root = create_gui()
    pressed_button = tk.StringVar()
    add_buttons(root, pressed_button)
    root.mainloop()
    launchSetting(int(pressed_button.get()))


if __name__ == "__main__":
    init_window()
