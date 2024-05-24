import logging  # pylint: disable=C0114
import sys
from logging.handlers import RotatingFileHandler

from colorlog import ColoredFormatter, StreamHandler, getLogger
from colorlog.escape_codes import parse_colors


class YACLogger:
    """
    Yet Another Colorful Logger is just another Python colorful logger
    that uses adds color to console log messages based on their severity level.

    Attributes:
        DEBUG (int): Debug level from the logging module.
        INFO (int): Info level from the logging module.
        WARNING (int): Warning level from the logging module.
        ERROR (int): Error level from the logging module.
        CRITICAL (int): Critical level from the logging module.
        logger (Logger): An instance of a logger with a
            specific name and color formatting.
    """

    class LogLevel:
        """
        Enum representing the various log levels available
        in the logging module.

        Attributes
        ----------
        DEBUG : int
            Detailed information, typically of interest
            only when diagnosing problems.
        INFO : int
            Confirmation that things are working as expected.
        WARNING : int
            An indication that something unexpected happened, or there
            may be some problem in the near future.
            The software is still working as expected.
        ERROR : int
            Due to a more serious problem,
            the software has not been able to perform some function.
        CRITICAL : int
            A very serious error, indicating that the program itself
            may be unable to continue running.
        """

        DEBUG = logging.DEBUG
        INFO = logging.INFO
        WARNING = logging.WARNING
        ERROR = logging.ERROR
        CRITICAL = logging.CRITICAL

    def __init__(
        self,
        name: str = "",
        filepath: str = "",
        level: int = LogLevel.INFO,
        log_colors=None,
        max_log_size: int = 10,
    ):
        """
        Initialize the YACLogger.

        Args:
            name (str): The name of the logger.
            level (int): The logging level (DEBUG, INFO,
            WARNING, ERROR, CRITICAL). Default is DEBUG.
            log_colors_dict (dict): A dictionary of colors
            for each logging level. Default is None.
        """
        supported_levels = []
        for attrbt, value in self.LogLevel.__dict__.items():
            if "__" not in attrbt:
                supported_levels.append(attrbt.lower())
                supported_levels.append(value)
        assert isinstance(name, str), "The name must be a string."
        assert name != "", "The logger name cannot be empty."
        assert isinstance(filepath, str), "The filepath must be a string."
        assert isinstance(
            max_log_size,
            int,
        ), "The max_log_size must be an integer."
        assert max_log_size > 0, "The max_log_size must be greater than 0."
        assert level in supported_levels, "".join(
            [
                "Log level must be LogLevel.<LEVEL>:",
                " DEBUG, INFO, WARNING, ERROR, CRITICAL.",
            ]
        )

        if filepath != "":
            try:
                with open(filepath, "a", encoding="UTF-8") as fp:
                    fp.close()
                fileformatter = logging.Formatter(
                    (
                        "[%(asctime)s.%(msecs)05ds]"
                        "[%(threadName)s]"
                        "[%(name)s] %(message)s"
                    ),
                    datefmt="%d/%m/%Y][%H:%M:%S",
                    style="%",
                )
            except (
                IsADirectoryError,
                FileNotFoundError,
                PermissionError,
            ) as excpt:
                raise ValueError("The log file path is invalid.") from excpt

        if log_colors is not None:
            assert isinstance(
                log_colors, dict
            ), "The parameter log_colors must be a dictionary"
            if not all(key in supported_levels for key in log_colors.keys()):
                raise KeyError("Invalid log_colors parameter")
            log_colors = {
                key: value
                for key, value in log_colors.items()
                if key in supported_levels
            }
            for _, value in log_colors.items():
                parse_colors(value)
        else:
            log_colors = {
                "debug": "",
                "info": "",
                "warning": "",
                "error": "",
                "critical": "",
            }

        coloredformatter = ColoredFormatter(
            (
                "%(log_color)s[%(asctime)s.%(msecs)05ds]"
                "[%(threadName)s]"
                "[%(name)s] %(message)s"
            ),
            datefmt="%d/%m/%Y][%H:%M:%S",
            reset=True,
            log_colors={
                "DEBUG": log_colors.get("debug", "") or "cyan",
                "INFO": log_colors.get("info", "") or "white",
                "WARNING": log_colors.get("warning", "") or "yellow",
                "ERROR": log_colors.get("error", "") or "bold_red",
                "CRITICAL": log_colors.get("critical", "") or "white,bg_red",
            },
            secondary_log_colors={},
            style="%",
        )

        self.logger = getLogger(name)
        handler = StreamHandler()
        handler.setFormatter(coloredformatter)
        self.logger.addHandler(handler)
        if filepath != "":
            file_logging_handler = RotatingFileHandler(
                filepath,
                mode="a",
                maxBytes=max_log_size * 1024 * 1024,
                backupCount=2,
                encoding=None,
            )
            file_logging_handler.setFormatter(fileformatter)
            self.logger.addHandler(file_logging_handler)
        self.set_level(level)

    def set_level(self, level):
        """
        Set the logging level.

        Args:
            level (int): The logging level (DEBUG, INFO,
                         WARNING, ERROR, CRITICAL).
        """
        self.logger.setLevel(level)

    def debug(self, formatter, *args):
        """
        Log a debug message.

        Args:
            formatter (str): The log message format.
            args: Values to format into the message.
        """
        self.logger.debug(formatter.format(*args))

    def info(self, formatter, *args):
        """
        Log an info message.

        Args:
            formatter (str): The log message format.
            args: Values to format into the message.
        """
        self.logger.info(formatter.format(*args))

    def warning(self, formatter, *args):
        """
        Log a warning message.

        Args:
            formatter (str): The log message format.
            args: Values to format into the message.
        """
        self.logger.warning(formatter.format(*args))

    def error(self, formatter, *args):
        """
        Log an error message.

        Args:
            formatter (str): The log message format.
            args: Values to format into the message.
        """
        self.logger.error(formatter.format(*args))

    def critical(self, formatter, *args):
        """
        Log a critical message and exit with status code -1.

        Args:
            formatter (str): The log message format.
            args: Values to format into the message.
        """
        self.logger.critical(formatter.format(*args))
        sys.exit(-1)
