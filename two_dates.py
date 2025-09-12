from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Convert strings into datetime objects
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        
        # Return the absolute difference in days
        return abs((d1 - d2).days)