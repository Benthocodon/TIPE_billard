import os
import time

from core.console.console import Console
from core.hal.hal import HardwareAbstractionLayer
from core.logs.logger import Logger
from core.system_monitor.system_monitor import Monitor
from core.manager.app_manager import AppManager
from core.server.server import Server, start_chrome

os.environ["LOG_LEVEL"] = "2"

server = Server()
server.start()

hal = HardwareAbstractionLayer(server)

hal.start_driver("web_audio_stream")
hal.start_driver("voice_commands")
logger = Logger(server)
logger.log_listenner()

monitor = Monitor(server)
monitor.record_listenner()

app_manager = AppManager(hal, server)
app_manager.start_up()

time.sleep(2)

console = Console(hal, server, app_manager)
start_chrome(server.path)
console.start()
