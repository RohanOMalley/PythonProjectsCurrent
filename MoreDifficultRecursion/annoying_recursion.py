


def annoying_factorial (n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 4 * annoying_factorial(3)
    elif n == 5:
        return 5 * annoying_factorial(4)
    elif n == 6:
        return 6 * annoying_factorial(5)
    elif n >= 7:
        return n * annoying_factorial(n - 1)

def annoying_fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    # 1,1,2,3,5,8,13,21,34,55
    # 1,2,3,4,5,6, 7,8
    elif n == 4:
        return annoying_fibonacci(3) + annoying_fibonacci(2)
    elif n == 5:
        return annoying_fibonacci(4) + annoying_fibonacci(3)
    elif n == 6:
        return annoying_fibonacci(5) + annoying_fibonacci(4)
    elif n >= 7:
        return annoying_fibonacci(n - 1) + annoying_fibonacci(n - 2)

def annoying_climbUp(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,2]
    elif n == 3:
        return [1,2,3]
    elif n == 4:
        return annoying_climbUp(3) + [4] 
    elif n == 5:
        return annoying_climbUp(4) + [5]
    elif n == 6:
        return annoying_climbUp(5) + [6]
    elif n >= 7:
        return annoying_climbUp(n-1) + [n]


def annoying_climbDownUp (n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [2,1,2]
    elif n == 3:
        return [3,2,1,2,3]
    elif n == 4:
        return [4] + annoying_climbDownUp(3) + [4]
    elif n == 5:
        return [5] + annoying_climbDownUp(4) + [5]
    elif n == 6:
        return [6] + annoying_climbDownUp(5) + [6]
    elif n >= 7:
        return [n] + annoying_climbDownUp(n-1) + [n]