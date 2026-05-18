import sounddevice as sd
import numpy as np
import whisper
import ollama
import utils.callback
import subprocess
import time


# --- Config ---
SAMPLE_RATE = 16000
CHUNK_SIZE = 1280
COMMAND_DURATION = 3


# --- Load models ---
print("Starting Ollama...")

ollama_process = subprocess.Popen(["ollama", "serve"])

print("Waiting...")
#time.sleep(5)

print("Ollama API is running")

response = ollama.chat(
    model="gemma4-physics-edu",
    messages=[
        {
            "role": "user",
            "content": "hello"
        }
    ]
)


print("Loading whisper models...")
whisper_model = whisper.load_model("base")
print("Models loaded!")


# --- Audio to Text ---

def transcribe_command():
    """Record and transcribe command after wake word."""
    print("Listening for command...")
    audio = sd.rec(
        int(COMMAND_DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype=np.float32
    )
    sd.wait()
    result = whisper_model.transcribe(audio.flatten(), fp16=False, language="en")
    return result["text"].strip()



def follow_command():
    print("follow-up command")
    start_time = time.time()
    with sd.InputStream(
        samplerate=16000,
        channels=1,
        callback=utils.callback.follow_callback
    ):
        while True:
            
            """if utils.callback.frunning:
                start_time = time.time()
                utils.callback.frunning = False"""
            
            current_time = time.time()
            
            if current_time - start_time > 10:
                break
