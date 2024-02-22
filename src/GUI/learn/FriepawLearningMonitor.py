import src.GUI.learn.LearnPlatform as lp
import src.GUI.learn.ManageIntelligence as mi
import src.GUI.WindowUtil as wu
import multiprocessing as mp


# Learning GUI entry point
# procedural logic
def start_processes(root, intel, exportPath):
    root.destroy()
    shared_data = {
        # data going to the GUI
        'prev_text': mp.Array('c', 255),  # string length 255
        'best_text': mp.Array('c', 255),
        'temperature_text': mp.Array('c', 50),
        # data coming from the GUI
        'pause': mp.Value('i', 1),  # integer initialized to 1
        'duty_cycle': mp.Value('i', 50),
        'temperature_threshold': mp.Value('i', 80),
        'export_rate': mp.Value('i', 10),
        'shuffle_quantity': mp.Value('i', 5),
        'learning_rate': mp.Value('i', 100)
    }

    stop_flag = mp.Event()

    window_process = mp.Process(target=lp.init_window, args=(shared_data,))
    window_process.start()

    random_text_process = mp.Process(target=lp.update_text, args=(shared_data, stop_flag))
    random_text_process.start()

    window_process.join()

    stop_flag.set()

    random_text_process.join()



