from datetime import datetime, timedelta, timezone
from typing import Optional

class TimeInterval:
    def __init__(self, start: Optional[datetime] = None, end: Optional[datetime] = None, duration: Optional[timedelta] = None):
        """
        Initialize a TimeInterval object.

        :param start: Start time as a datetime object.
        :param end: End time as a datetime object.
        :param duration: Duration as a timedelta object.
        """
        self.start = start
        self.end = end
        self.duration = duration

    def to_interval(self) -> str:
        """
        Generate an ISO 8601 interval string based on the available data.
        """
        if self.start and self.end:
            # Start and End Time Interval
            return f"{self.start.isoformat()}/{self.end.isoformat()}"
        elif self.start and self.duration:
            # Start Time and Duration
            return f"{self.start.isoformat()}/{self._format_duration(self.duration)}"
        elif self.duration and self.end:
            # Duration and End Time
            return f"{self._format_duration(self.duration)}/{self.end.isoformat()}"
        else:
            raise ValueError("Insufficient data to generate a time interval. Provide start/end and/or duration.")

    @staticmethod
    def _format_duration(duration: timedelta) -> str:
        """
        Format a timedelta as an ISO 8601 duration string (e.g., PT1H30M).
        """
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        duration_str = "P"
        if hours or minutes or seconds:
            duration_str += "T"
            if hours:
                duration_str += f"{hours}H"
            if minutes:
                duration_str += f"{minutes}M"
            if seconds:
                duration_str += f"{seconds}S"
        return duration_str

    @classmethod
    def from_duration_and_end(cls, duration: timedelta, end: datetime):
        """
        Create a TimeInterval from a duration and an end time.
        """
        start = end - duration
        return cls(start=start, end=end)

    @classmethod
    def from_start_and_duration(cls, start: datetime, duration: timedelta):
        """
        Create a TimeInterval from a start time and a duration.
        """
        end = start + duration
        return cls(start=start, end=end)