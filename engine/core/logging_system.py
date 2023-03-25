import datetime
import logging

from engine.core.core_subsystem import *
from engine.core.event_sysyem import *

FILE_LOG_PATH = "D:\Python\python-game\config\logging.txt"


class LoggingManager(EngineSubsytem):
    def __init__(self, event_manager: EventManager) -> None:
        super().__init__(event_manager)

        self.event_manager.register_listener(INFO_EVENT, self.logging)

    def logging(self, event):
        # get the current date and time stamp
        now = datetime.datetime.now()
        
        msg = f"[{now}] [{event.type}] [{event.source}] = {event.payload}\n"
        print(msg)
        
        with open(FILE_LOG_PATH, 'a') as file:
            file.write(msg)

