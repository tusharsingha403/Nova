from openwakeword.model import Model
from PyQt5.QtCore import QMetaObject, Qt, Q_ARG
import PyQt5.QtCore as QtCore
import numpy as np
import utils.command
import utils.transcribe
import pyautogui
from PyQt5.QtCore import QTimer
import threading

# --- Config ---

ONNX_MODEL_PATH = "model/hey_nova_20260413_031510.onnx"
THRESHOLD = 0.15
running = True
assistant_active = False
assistant = None  # Set via set_assistant() from main.py

# --- Load models ---

print("Loading oww model...")
oww_model = Model(
    wakeword_models=[ONNX_MODEL_PATH],
    inference_framework="onnx"
)

screen = pyautogui.screenshot()


# --- Helper ---


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


# --- Follow-up callback ---

def follow_callback(indata, frames, time, status):
    global assistant_active
    volume = np.linalg.norm(indata)

    if volume > 0.30:
        print("Sound detected!")
        command = utils.transcribe.transcribe_command()
        assistant_active = utils.command.handle_command(command)
        print("again follow up command")


# --- Main audio callback ---

def audio_callback(indata, frames, time_info, status):
    global running

    if not running:
        return

    # Convert float32 → int16 for openwakeword
    audio_chunk = (indata[:, 0] * 32767).astype(np.int16)

    # Feed chunk to wake word model
    prediction = oww_model.predict(audio_chunk)

    for model_name, score in oww_model.prediction_buffer.items():
        latest_score = score[-1]
        print(f"[{model_name}]: {latest_score:.3f}", end="\r")

        if latest_score >= THRESHOLD:
            print(f"\n'Hey Nova' detected! (confidence: {latest_score:.2f})")

            safe_animate("wakeup")

            oww_model.reset()

            command = utils.transcribe.transcribe_command()
            running = utils.command.handle_command(command)

            print("\nListening for 'Hey Nova'...")
            threading.Timer(2.0, lambda: safe_animate("idle")).start()