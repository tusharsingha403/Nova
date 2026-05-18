import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QPoint, QTimer, QSize
from PyQt5.QtCore import pyqtSlot

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GIF_SIZE = QSize(120, 120)  


class Assistant(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label = QLabel(self)

        self.animations = {
            "idle":    os.path.join(BASE_DIR, "assets", "idle.gif"),
            "wakeup":  os.path.join(BASE_DIR, "assets", "wakeup.gif"),
            "working": os.path.join(BASE_DIR, "assets", "working.gif"),
            "done":    os.path.join(BASE_DIR, "assets", "done.gif"),
            "drag":    os.path.join(BASE_DIR, "assets", "drag.gif"),
            "fat":    os.path.join(BASE_DIR, "assets", "fat.gif"),
            "shocked1":    os.path.join(BASE_DIR, "assets", "shocked1.gif"),
            "shocked2":    os.path.join(BASE_DIR, "assets", "shocked2.gif"),
            "shocked3":    os.path.join(BASE_DIR, "assets", "shocked3.gif"),
            "stop":    os.path.join(BASE_DIR, "assets", "stop.gif"),
            "angry":    os.path.join(BASE_DIR, "assets", "angry2.gif"),
            "sad":    os.path.join(BASE_DIR, "assets", "sad2.gif"),
            "dance":    os.path.join(BASE_DIR, "assets", "dance.gif"),
            "love":    os.path.join(BASE_DIR, "assets", "love.gif"),
            "end":    os.path.join(BASE_DIR, "assets", "end.gif"),
        }

        self.movie = None
        self.set_animation("idle")

        self.old_pos = None
        self.move(1770, 930)

    # ---------------- PUBLIC API ----------------

    @pyqtSlot(str)
    def set_animation(self, state: str):
        """Change the animation state. Call this from anywhere."""
        if state not in self.animations:
            print(f"ERROR: Unknown state '{state}'. Valid: {list(self.animations.keys())}")
            return

        if self.movie:
            self.movie.stop()
            try:
                self.movie.frameChanged.disconnect()
            except TypeError:
                pass

        self.movie = QMovie(self.animations[state])

        if not self.movie.isValid():
            print(f"ERROR: Could not load GIF: {self.animations[state]}")
            return

        self.movie.setScaledSize(GIF_SIZE)  
        self.label.setMovie(self.movie)
        self.movie.frameChanged.connect(self.update_size)
        self.movie.start()

        QTimer.singleShot(50, self.update_size)
        print(f"Animation changed to: {state}")

    def stop(self):
        """Stop the assistant and close the window. Call when main program ends."""
        if self.movie:
            self.movie.stop()
        self.close()

    # ---------------- INTERNALS ----------------

    def update_size(self):
        if not self.movie:
            return
        pixmap = self.movie.currentPixmap()
        if pixmap.isNull():
            return
        size = pixmap.size()
        if size.isEmpty():
            return
        self.label.resize(size)
        self.resize(size)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()
            self.set_animation("drag")

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.old_pos = None
        self.set_animation("idle")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    assistant = Assistant()
    assistant.show()
    sys.exit(app.exec_())