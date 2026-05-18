import pyautogui
import numpy as np
import utils.llmkeyword
import utils.ocrdata
from PyQt5.QtCore import QMetaObject, Qt, Q_ARG
import threading
import utils.yolodata


# --- Assistant instance (set from main.py) ---

assistant = None

def set_assistant(instance):
    global assistant
    assistant = instance

def safe_animate(state):
    """Truly thread-safe: forces immediate execution on the main thread."""
    if assistant:
        QMetaObject.invokeMethod(
            assistant,
            "set_animation",
            Qt.QueuedConnection,
            Q_ARG(str, state)
        )


# --- Handles Command ---

def handle_command(text):
    """Handle recognized command."""
    safe_animate("working")  
    print(f"Command: {text}")
    text = text.lower()
    
    
    if "fat" in text and "you" in text:
        safe_animate("fat")
    elif "stop" in text:
        safe_animate("end")
    elif "you" in text and ("ugly" in text or "annoying" in text or "hate" in text or "useless" in text):
        safe_animate("shocked3")
        threading.Timer(2.0, lambda: safe_animate("shocked2")).start()
    elif "bad" in text and "you" in text:
        safe_animate("sad")
    elif "dance for me" in text or "can you dance" in text:
        safe_animate("dance")
    elif "you" in text and ("cute" in text or "love" in text):
        safe_animate("love")
        
    
    key_word = utils.llmkeyword.whatkeyword(text)
    key_word = key_word.strip()
    print("'", key_word, "'")

    if key_word == "v_mute":
        pyautogui.press('volumemute')

    elif key_word == "v_up":
        pyautogui.press('volumeup')

    elif key_word == "v_down":
        pyautogui.press('volumedown')

    elif key_word == "m_pp":
        pyautogui.press('playpause')
    
    elif "scroll" in text and "up" in text :
        pyautogui.scroll(500)
    
    elif "scroll" in text and "down" in text :
        pyautogui.scroll(-500)
    
    elif "press" in key_word:
        key_word = key_word.replace("press_", "")
        pyautogui.press(key_word)

    elif key_word == "next_window":
        pyautogui.hotkey('alt', 'tab')

    elif key_word == "c_window":
        pyautogui.hotkey('alt', 'f4')

    elif key_word == "t_manager":
        pyautogui.hotkey('ctrl', 'shift', 'esc')

    elif key_word == "min_all":
        pyautogui.hotkey('win', 'd')

    elif key_word == "copy":
        pyautogui.hotkey('ctrl', 'c')

    elif key_word == "cut":
        pyautogui.hotkey('ctrl', 'x')

    elif key_word == "paste":
        pyautogui.hotkey('ctrl', 'v')

    elif key_word == "undo":
        pyautogui.hotkey('ctrl', 'z')

    elif key_word == "s_all":
        pyautogui.hotkey('ctrl', 'a')

    elif key_word == "save":
        pyautogui.hotkey('ctrl', 's')

    elif key_word == "refresh":
        pyautogui.press('f5')

    elif key_word == "b_new_tab":
        pyautogui.hotkey('ctrl', 't')

    elif key_word == "b_close_tab":
        pyautogui.hotkey('ctrl', 'w')

    elif key_word == "b_next_tab":
        pyautogui.hotkey('ctrl', 'tab')
    
    elif "b_tab" in key_word:
        tab_no = key_word.replace("b_tab_", "")
        pyautogui.hotkey('ctrl', tab_no)

    elif key_word == "b_incognito_tab":
        pyautogui.hotkey('ctrl', 'shift', 'n')

    elif key_word == "b_downloads":
        pyautogui.hotkey('ctrl', 'j')

    elif key_word == "b_history":
        pyautogui.hotkey('ctrl', 'h')

    elif key_word == "b_window":
        pyautogui.hotkey('ctrl', 'n')

    elif key_word == "b_back":
        pyautogui.hotkey('alt', 'left')

    elif key_word == "b_forward":
        pyautogui.hotkey('alt', 'right')

    elif key_word == "b_save":
        pyautogui.hotkey('ctrl', 's')

    elif key_word == "b_show_sc":
        pyautogui.hotkey('ctrl', 'u')

    elif key_word == "b_print":
        pyautogui.hotkey('ctrl', 'p')
        
    
    elif key_word == "like_icon":
        screen = np.array(pyautogui.screenshot())
        screen = screen[:, :, ::-1]
        try:
            x,y = utils.yolodata.yolocoords(key_word,screen)
            pyautogui.click(x, y)
        except:
            print("not found")
    
    elif key_word == "dislike_icon":
        screen = np.array(pyautogui.screenshot())
        screen = screen[:, :, ::-1]
        try:
            x,y = utils.yolodata.yolocoords(key_word,screen)
            pyautogui.click(x, y)
        except:
            print("not found")
    
    elif key_word == "share_icon":
        screen = np.array(pyautogui.screenshot())
        screen = screen[:, :, ::-1]
        try:
            x,y = utils.yolodata.yolocoords(key_word,screen)
            pyautogui.click(x, y)
        except:
            print("not found")
    

    elif "weather" in text:
        print("→ Getting weather...")

    elif "time" in text:
        import datetime
        print(f"→ Time: {datetime.datetime.now().strftime('%H:%M')}")

    elif "open" in key_word:
        screen = np.array(pyautogui.screenshot())
        try:
            target_word = key_word.replace("open_", "")
            x, y = utils.ocrdata.ocrcoords(target_word, screen)
            print(x, y)
            pyautogui.doubleClick(x, y)
        except:
            try:
                screen = np.array(pyautogui.screenshot())
                screen = screen[:, :, ::-1]
                target_word = key_word.replace("open_", "")
                target_word = (target_word + "_logo")
                print(target_word)
                x,y = utils.yolodata.yolocoords(target_word,screen)
                pyautogui.doubleClick(x, y)
            except:
                print("not found")

    elif "go" in key_word:
        screen = np.array(pyautogui.screenshot())
        target_word = key_word.replace("go_", "")
        try:
            x, y = utils.ocrdata.ocrcoords(target_word, screen)
            print(x, y)
            pyautogui.click(x, y)
        except:
            try:
                screen = np.array(pyautogui.screenshot())
                screen = screen[:, :, ::-1]
                target_word = key_word.replace("go_", "")
                target_word = (target_word + "_icon")
                print(target_word)
                x,y = utils.yolodata.yolocoords(target_word,screen)
                pyautogui.click(x, y)
            except:
                print("not found")
    
    elif "rc" in key_word:
        screen = np.array(pyautogui.screenshot())
        target_word = key_word.replace("rc_", "")
        try:
            x, y = utils.ocrdata.ocrcoords(target_word, screen)
            print(x, y)
            pyautogui.rightClick(x, y)
        except:
            print("not found")
    

    elif "stop" in text or "exit" in text:
        print("→ Goodbye!")
        return False

    else:
        print(f"→ Unknown command: '{text}'")

    return True

"""# --- Audio callback ---

def audio_callback(indata, frames, time_info, status):
    global running
    if not running:
        return

    # Convert float32 → int16 for openwakeword
    audio_chunk = (indata[:, 0] * 32767).astype(np.int16)

    # Feed chunk to wake word model
    prediction = oww_model.predict(audio_chunk)

    # Check each detected model's score
    for model_name, score in oww_model.prediction_buffer.items():
        latest_score = score[-1]  # most recent confidence score
        print(f"[{model_name}]: {latest_score:.3f}", end="\r")

        if latest_score >= THRESHOLD:
            print(f"\n'Hey Nova' detected! (confidence: {latest_score:.2f})")
            oww_model.reset()  # reset buffer to avoid re-triggering
            command = transcribe_command()
            running = handle_command(command)
            print("\nListening for 'Hey Nova'...")"""

