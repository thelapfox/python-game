
class LogManager:
    def __init__(self, buffer_size: int, log_path: str):
        self.buffer_size = buffer_size
        self.log_path = log_path

        self.log_buffer = ''
    
    def log_event(self, event):
        log_type = event.data["LOG_TYPE"]
        log_info = event.data["DATA"]
        log_timestamp = event.timestamp

        msg: str = "<" + log_timestamp + "> [" + log_type + "] " + log_info
        self.log_buffer += msg

        if len(self.log_buffer) >= self.buffer_size:
            print(self.log_buffer)

            self._write_file(self.log_buffer)
            self.log_buffer = '' 


    def _write_file(self, text: str):
        with open(self.log_path, 'a') as file:
            file.write(text + '\n')
