class Solution:
    def countTime(self, time: str) -> int:

        hh, mm = time.split(":")
        
        # Count possible hours
        if hh == "??":
            hours = 24
        elif hh[0] == "?":
            if hh[1] == "?":
                hours = 24
            else:
                d2 = int(hh[1])
                if d2 <= 3:
                    hours = 3  # 0,1,2
                else:
                    hours = 2  # 0,1
        elif hh[1] == "?":
            d1 = int(hh[0])
            if d1 == 2:
                hours = 4  # 20–23
            else:
                hours = 10  # 0–9
        else:
            hours = 1 if 0 <= int(hh) < 24 else 0
        
        # Count possible minutes
        if mm == "??":
            minutes = 60
        elif mm[0] == "?":
            minutes = 6  # 00–59 → first digit 0–5
        elif mm[1] == "?":
            minutes = 10  # 0–9
        else:
            minutes = 1 if 0 <= int(mm) < 60 else 0
        
        return hours * minutes
