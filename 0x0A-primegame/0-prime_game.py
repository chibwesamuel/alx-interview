#!/usr/bin/python3
"""
Determines winner of prime number removal game with optimal play.
"""

def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Prototype: def isWinner(x, nums)

    Args:
        x: The number of rounds played.
        nums: An array of integers representing the value of n for each round.

    Returns:
        The name of the player who won the most rounds.
        If the winner cannot be determined, returns None.
    """
    if x < 1 or not nums:
        return None
    
    def sieve(n):
        """
        Returns a list of primes up to n using the Sieve of Eratosthenes
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        primes = []
        for i in range(n + 1):
            if is_prime[i]:
                primes.append(i)
        return primes

    max_num = max(nums)
    primes_up_to_max = sieve(max_num)
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue
        primes = [p for p in primes_up_to_max if p <= n]
        multiples_removed = [False] * (n + 1)
        move_count = 0
        
        while True:
            move_made = False
            for prime in primes:
                if not multiples_removed[prime]:
                    move_count += 1
                    for multiple in range(prime, n + 1, prime):
                        multiples_removed[multiple] = True
                    move_made = True
                    break
            if not move_made:
                break
        
        if move_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
