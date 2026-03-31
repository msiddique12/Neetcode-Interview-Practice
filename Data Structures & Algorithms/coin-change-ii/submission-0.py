class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = {}

        def dfs(i, remaining):
            if remaining == 0:
                return 1
            if i == len(coins):
                return 0

            if (i, remaining) in mem:
                return mem[(i, remaining)]

            ways = 0

            # take coin
            if remaining >= coins[i]:
                ways += dfs(i, remaining - coins[i])

            # skip coin
            ways += dfs(i + 1, remaining)

            mem[(i, remaining)] = ways
            return ways

        return dfs(0, amount)