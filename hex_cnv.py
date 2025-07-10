class Solution:
    def toHex(self, num: int) -> str:

        # if num < 0:
        #     return "ffffffff"
        # return hex(num)[2:]
        return format(num & 0xffffffff,'x')
        