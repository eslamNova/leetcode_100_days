class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        a = 0 

        for c in commands:
            if c == "UP":
                a -= n 
            elif c == "DOWN":
                a += n
            elif c == "RIGHT":
                a += 1
            else:
                a -= 1
        return a
        