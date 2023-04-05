from engine.core import events, logging, event_types


def main():
    event_manager =  events.EventManager()

    path = "logging.txt"
    log_manager = logging.LogManager(1, path)

    event_manager.add_listener(event_types.logging_event, log_manager.log_event)

    log_dict = {"LOG_TYPE": "INFO", "DATA": "test event logging"}
    log = events.Event(event_types.logging_event, log_dict)

    event_manager.add_event(log)
    event_manager.dispatch()

if __name__ == "__main__":
    main()