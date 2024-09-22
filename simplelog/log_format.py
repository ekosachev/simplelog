class LogFormat:
    timestamp: bool
    timestamp_format: str
    filename: bool

    def __init__(
            self,
            display_timestamp: bool = True,
            timestamp_format: str = "%d/%m/%y %H:%M:%S.%f",
            display_filename: bool = False,
    ):
        self.timestamp = display_timestamp
        self.timestamp_format = timestamp_format
        self.filename = display_filename

    @classmethod
    def default(cls):
        return cls()
