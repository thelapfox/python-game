from engine.core.event_sysyem import *


class EngineSubsytem:
    def __init__(self, event_manager: EventManager) -> None:
        self.event_manager = event_manager
        
