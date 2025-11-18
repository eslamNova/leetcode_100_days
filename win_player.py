class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        o = 0 
        pl = {}
        for p in pick:
            print(p)
            print("-_-_-_")
            print(pl)
            if p[0] not in pl:
                pl[p[0]] = {}
                pl[p[0]][p[1]] = 1
                
            else:
                if p[1] not in pl[p[0]]:
                    pl[p[0]][p[1]] = 1
                else:
                    pl[p[0]][p[1]] += 1

        print(pl)

        # for p in pl:
        #     if pl.key >= 0 :
        #         o += 1
        for player, colors in pl.items():
            print(colors.values())
            max_count = max(colors.values()) 
            if max_count >= player + 1:
                o += 1
        return o            

            

        