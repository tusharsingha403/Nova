import sounddevice as sd
import utils.command
import utils.callback
import utils.transcribe
from UI.assistant import Assistant
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import sys
import threading
import time


app = QApplication(sys.argv)
assistant = Assistant()
assistant.show()

utils.callback.set_assistant(assistant)
utils.command.set_assistant(assistant)


def mainapp():
    print("Listening for 'Hey Nova'...")
    utils.callback.safe_animate("idle")  

    with sd.InputStream(
        samplerate=utils.transcribe.SAMPLE_RATE,
        channels=1,
        dtype="float32",
        blocksize=utils.transcribe.CHUNK_SIZE,
        callback=utils.callback.audio_callback
    ):
        while utils.callback.running:
            sd.sleep(100)
    
    start_t = time.time()
    while time.time() - start_t < 1.3:
        pass

    utils.callback.safe_animate("done")  
    QTimer.singleShot(0, assistant.stop)
    QTimer.singleShot(0, app.quit)

    print("Assistant stopped.")


thread = threading.Thread(target=mainapp, daemon=True)
thread.start()

sys.exit(app.exec_())
