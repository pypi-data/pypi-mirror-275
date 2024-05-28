import logging
import json
import boto3


class CloudWatchLogger:
    def __init__(
        self,
        log_level=logging.INFO,
        name=__name__,
        log_group_name=None,
        log_stream_name=None,
    ):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # Initialize CloudWatch client
        self.cloudwatch = boto3.client("logs")

        # Setup CloudWatch log stream if not provided
        if not log_group_name or not log_stream_name:
            raise ValueError(
                "Both log_group_name and log_stream_name must be provided."
            )

        self.log_group_name = log_group_name
        self.log_stream_name = log_stream_name

        # Handler to send logs to CloudWatch
        self.handler = logging.Handler()
        self.handler.setFormatter(self.get_formatter())
        self.logger.addHandler(self.handler)

    def get_formatter(self):
        """Return a formatter that outputs logs in JSON format."""

        class JsonFormatter(logging.Formatter):
            def format(self, record):
                return json.dumps(
                    {
                        "timestamp": record.created,
                        "level": record.levelname,
                        "message": record.msg,
                        "logger": record.name,
                    }
                )

        return JsonFormatter("%(message)s")

    def send_logs(self, log_records):
        """Send log records to CloudWatch."""
        log_events = [
            {"timestamp": int(record.created * 1000), "message": record.msg}
            for record in log_records
        ]
        self.cloudwatch.put_log_events(
            logGroupName=self.log_group_name,
            logStreamName=self.log_stream_name,
            logEvents=log_events,
        )


# Usage example
if __name__ == "__main__":
    logger = CloudWatchLogger(
        log_level=logging.DEBUG,
        log_group_name="YourCloudWatchLogGroup",
        log_stream_name="YourCloudWatchLogStream",
    )

    logger.logger.debug("This is a debug message")
    logger.send_logs(logger.logger.records)
