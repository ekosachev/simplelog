from datetime import datetime
from enum import Enum

import rich

from color import Color
from log_format import LogFormat
from log_style import LogStyle
from modifier import Modifier


class LogLevel(int, Enum):
    debug = 0
    info = 1
    warning = 2
    error = 3
    fatal = 4

    def __str__(self) -> str:
        match self:
            case LogLevel.debug:
                return "DEBUG"
            case LogLevel.info:
                return "INFO"
            case LogLevel.warning:
                return "WARN"
            case LogLevel.error:
                return "ERROR"
            case LogLevel.fatal:
                return "FATAL"


class Logger(object):
    min_level: LogLevel
    format: LogFormat
    styles: list[LogStyle] = [
        LogStyle(Color.bright_black, modifiers=Modifier.italic),
        LogStyle(),
        LogStyle(Color.yellow),
        LogStyle(Color.red, modifiers=Modifier.bold),
        LogStyle(Color.black, bg=Color.bright_white, modifiers=Modifier.bold)
    ]

    def __init__(self,
                 min_level: LogLevel = LogLevel.info,
                 log_format: LogFormat = LogFormat.default()
                 ):
        self.min_level = min_level
        self.format = log_format

    def set_style(self, level: LogLevel, style: LogStyle):
        self.styles[level] = style

    def set_format(self, new_format: LogFormat):
        self.format = new_format

    def set_min_level(self, level: LogLevel):
        self.min_level = level

    def _apply_format(self, text, level: LogLevel) -> str:
        level_str: str = str(level).ljust(6)
        file_str: str = str(__file__).split('\\')[-1].ljust(30)
        timestamp: datetime = datetime.now()
        timestamp_str: str = timestamp.strftime(
            self.format.timestamp_format
        ).ljust(30)
        prelude = level_str
        if self.format.timestamp:
            prelude += timestamp_str
        if self.format.filename:
            prelude += file_str


        return f"{prelude} | {text}"

    def _log(self, level: LogLevel, text: str):
        if level >= self.min_level:
            style: LogStyle = self.styles[level]
            rich.print(self._apply_format(style.format(text), level))

    def debug(self, text: str):
        self._log(LogLevel.debug, text)

    def info(self, text: str):
        self._log(LogLevel.info, text)

    def warning(self, text: str):
        self._log(LogLevel.warning, text)

    def error(self, text: str):
        self._log(LogLevel.error, text)

    def fatal(self, text: str):
        self._log(LogLevel.fatal, text)
