class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:


        c = Counter(students)

        s,c = c[1],c[0]
        print(s,c)
        sdc = len(sandwiches)

        for sd in sandwiches:
            if sd == 1:
                if s >= 1:
                    s -= 1
                    sdc -= 1
                else:
                    break
                
            else:
                if c >= 1:
                    c -= 1
                    sdc -= 1
                else:
                    break
            

        return sdc
        