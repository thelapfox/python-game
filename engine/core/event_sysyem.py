import queue 
import threading


ERROR_EVENT = "ERROR_EVENT"

class Event:
    def __init__(self, event_type, event_source, event_payload) -> None:
        self.type: str = event_type
        self.source = event_source
        self.payload = event_payload

class EventManager:
    def __init__(self) -> None:
        self.listeners = {}

    def register_listener(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unregister_listener(self, event_type, listener):
        if event_type in self.listeners:
            if listener in self.listeners[event_type]:
                self.listeners[event_type].remove(listener)

    def dispatch_event(self, event):
        if event in self.listeners:
            event_type = event.type
            for listener in self.listeners[event_type]:
                listener(event)

