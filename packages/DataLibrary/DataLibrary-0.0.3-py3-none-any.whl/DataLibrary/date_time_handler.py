import pandas as pd

class DateTimeHandler:
    def extract_date(self, data, column):
        """
        Extract date from datetime column.
        """
        data[column] = pd.to_datetime(data[column])
        return data[column].dt.date

    def extract_time(self, data, column):
        """
        Extract time from datetime column.
        """
        data[column] = pd.to_datetime(data[column])
        return data[column].dt.time

    def convert_timezone(self, data, column, timezone):
        """
        Convert datetime column to specified timezone.
        """
        data[column] = pd.to_datetime(data[column])
        return data[column].dt.tz_localize('UTC').dt.tz_convert(timezone)