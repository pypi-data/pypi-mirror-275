import logging
import json
from datetime import datetime


class ConsoleJsonLogger:
    def __init__(self, log_level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # Create a StreamHandler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)

        # Set up a custom JSON formatter
        formatter = self.get_formatter()
        stream_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(stream_handler)

    def get_formatter(self):
        """Return a formatter that outputs logs in JSON format."""

        # Current UTC time
        current_utc_time = datetime.utcnow().isoformat() + "Z"

        class JsonFormatter(logging.Formatter):
            def format(self, record):
                return json.dumps(
                    {
                        "timestamp": record.created,
                        "current_utc_time": current_utc_time,
                        "level": record.levelname,
                        "message": record.msg,
                        "logger": record.name,
                    }
                )

        return JsonFormatter("%(message)s")

    def log_message(self, level, message):
        """Log a message at the specified level."""
        if hasattr(self.logger, level):
            getattr(self.logger, level)(message)
        else:
            self.logger.error(f"Invalid log level: {level}")
