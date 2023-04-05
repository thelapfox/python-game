import datetime

class Event:
    def __init__(self, type: str, data: dict):
        self.type = type
        self.data = data

        self.timestamp = datetime.datetime.now()
        self.handled = False

class EventManager:
    def __init__(self):
        self.listeners: dict = {}
        self.events: list = []

    def add_listener(self, type: str, listener):
        if(self.listeners.get(type)):
            self.listeners[type].append(listener)
            return
        
        vec: list = [listener]
        self.listeners[type] = list

    def remove_listener(self, type: str, listener):
        listeners: list = self.listeners.get(type)
        if(~list): return

        listeners.remove(listener)

    def add_event(self, event: Event):
        self.events.append(event)
    
    def dispatch_immediately(self, event: Event):
        listeners: list = self.listeners.get(type)
        if(list is []): return

        for listener in listeners:
            listener(event)        

        event.handled = True

    def dispatch(self):
        for event in self.events:
            self.dispatch_immediately(event)

        self.events = [obj for obj in self.events if not obj.handled]

