from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal



### attention le rammasse miette de python n est pas assez efficace -> il faut forcer le destructeur!!!!!
class ExecuteThread(QThread):
    my_signal = pyqtSignal()

    def __init__(self,target=None,args=()):
        super().__init__()
        self._target = target
        self._args = args
    def emit_signal(self):
        self.my_signal.emit()
    def run(self):
        try:
            self.my_signal.emit()
            if self._target:
                self._target(*self._args)
        finally:
            del self._target, self._args
        pass

    def stop(self):
        self.terminate()

    def __del__(self):
        print("--------------------> destructor of ExecuteThread")

from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')