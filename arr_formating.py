class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:


        # nr = []

        # for j in range(arr):
        #     for i in range(len(pieces)):
        #         if a == pieces[i][0]:
        #             nr.append(a)
                    
        # return nr == arr
        # Input:
        # arr    = [91, 4, 64, 78]
        # pieces = [[78], [4, 64], [91]]

        # Step 1: Create a dictionary from first element of each piece
        # mapping = {78: [78], 4: [4, 64], 91: [91]}
        mapping = {piece[0]: piece for piece in pieces}

        i = 0  # index in arr

        # Step 2: Start scanning arr
        # i = 0, arr[i] = 91 → mapping[91] = [91]
        # Check arr[0] == 91 → ✅ match, move i to 1
        # Now i = 1

        # i = 1, arr[i] = 4 → mapping[4] = [4, 64]
        # Check arr[1] == 4 → ✅
        # Check arr[2] == 64 → ✅, move i to 3

        # i = 3, arr[i] = 78 → mapping[78] = [78]
        # Check arr[3] == 78 → ✅, move i to 4 (end of arr)

        while i < len(arr):
            if arr[i] not in mapping:
                # If current arr[i] doesn't match any piece start → ❌
                return False

            piece = mapping[arr[i]]

            # Match every number in this piece to the corresponding arr slice
            for num in piece:
                if i >= len(arr) or arr[i] != num:
                    return False
                i += 1  # Advance to next number in arr

        # If we finished scanning and all matched
        return True


        