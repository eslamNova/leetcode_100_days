class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        cm = float('inf')
        w = {}

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum = i + j
                    if index_sum < cm:
                        cm = index_sum
                        w = {list1[i]: index_sum}  # reset dict to only store current min
                    elif index_sum == cm:
                        w[list1[i]] = index_sum  # add to result if same min

        return list(w.keys())
        