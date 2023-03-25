import queue 
import threading


INFO_EVENT = "INFO_EVENT"

class Event:
    def __init__(self, event_type: str, event_source: object, event_payload) -> None:
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
        event_type = event.type
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(event)

