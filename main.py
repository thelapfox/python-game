from engine.core.event_sysyem import *
from engine.core.logging_system import *


def ListenerDebug(event):
    msg = event.payload + '\nReceived'
    print(msg)

def main():
    event_manager = EventManager()
    
    logging_manager = LoggingManager(event_manager)

    

if __name__ == "__main__":
    main()