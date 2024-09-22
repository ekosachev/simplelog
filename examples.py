from color import Color
from log_format import LogFormat
from log_style import LogStyle
from logger import Logger, LogLevel
from modifier import Modifier

# Default logger
my_logger = Logger()

my_logger.info("Hello world!")
my_logger.warning("somefile.json not found, creating...")
my_logger.info("somefile.json created")
my_logger.error("You cannot divide by zero")
my_logger.fatal("Database unreachable")

# By default, you need to change minimal log level for DEBUG lines to be
# displayed

my_logger.debug("This will not be displayed")
my_logger.set_min_level(LogLevel.debug)
my_logger.debug("This will be displayed")

# You also can customize styles
my_logger.set_style(
    level=LogLevel.error,
    style=LogStyle(color=Color.red, modifiers=Modifier.underline)
)
my_logger.error("This text is underlined")

# Or change the data displayed
my_logger.set_format(
    LogFormat(
        display_timestamp=False,
        display_filename=True
    )
)
my_logger.info("This will tell you the filename")
my_logger.set_format(
    LogFormat(
        display_timestamp=True,
        display_filename=True
    )
)
my_logger.info("Or everything at once")
