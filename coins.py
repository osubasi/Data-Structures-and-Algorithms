# Omer Subasi

def coinChange(coins, amount):
    def dp(coins, amount, memo):
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        
        min_coins = float('inf')
        for coin in coins:
            if coin <= amount:
                min_coins = min(min_coins, 1 + dp(coins, amount - coin, memo))

        memo[amount] = min_coins
        return memo[amount]

    res = dp(coins, amount, {})
    return res if res != float('inf') else -1
