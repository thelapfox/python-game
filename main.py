from engine.core.event_sysyem import *

from engine.core.logging_system import *
from engine.graphics.window import *


def main():
    event_manager = EventManager()
    
    logging_subsystem = LoggingSubsystem(event_manager)
    
    window = Window(event_manager)


if __name__ == "__main__":
    main()