import threading
from pymasterstorage.storage import CheckStorage

def initstorage() -> None:
    thread = threading.Thread(target=CheckStorage)
    thread.start()