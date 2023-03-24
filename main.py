from engine.core.event_sysyem import *


def ListenerDebug(event):
    msg = event.payload + '/nReceived'
    print(msg)

def main():
    event_manager = EventManager()
    event_manager.register_listener(ERROR_EVENT, ListenerDebug)

    event_debug = Event(ERROR_EVENT, None, "This is a debug event!")
    event_manager.dispatch_event(event_debug)

if __name__ == "__main__":
    main()