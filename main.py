import time

from win32gui import GetForegroundWindow, GetWindowText
import logging
import pyscreenshot


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_idle_time(_start_time: float, _end_time: float) -> int:
    return int(end_time - start_time)


last_active_window_text: str = ""
start_time = time.time()
while True:
    if last_active_window_text != GetWindowText(GetForegroundWindow()):
        last_active_window_text = GetWindowText(GetForegroundWindow())
        end_time = time.time()
        logger.info(f": {last_active_window_text} : {get_idle_time(_start_time=start_time, _end_time=end_time)} ms")
        image = pyscreenshot.grab()
        image.save("GeeksforGeeks.png")
        start_time = time.time()
