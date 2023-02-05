


def getFactors(x):
    #Returns a list of factors of the given number x.
    factors = []
    for i in range(1, x + 1, 1):
        if x % i == 0:
            factors.append(i)
            
    return factors


def isPrime(x):
    #Returns whether or not the given number x is prime.

  
    if x == 0 or x == 1:
        return False
    elif x < 0:
        return False
    elif x == 2:
        return True

    elif x > 2:
        for i in range(2, x):
            if x % i == 0:
                return False
            
        else:
            return True    
            

def isComposite(x):
    #Returns whether or not the given number x is composite.
 
    if x == 0 or x == 1:
        return False
    elif x < 0:
        return False
    elif x == 2:
        return False

    elif x > 2:
        for i in range(2, x):
            if x % i == 0:
                return True
            
        else:
            return False
    


def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """
    factor = 0
    
    if x == 0 or x == 1:
        return False
    elif x < 0:
        return False
    
    elif x > 1:
        for i in range(1, x):
            if x % i == 0:
                factor += i
                
        if factor == x:
            return True
            
        else:
            return False


def isAbundant(x):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.
    """
    
    factor = 0
    
    if x == 0 or x == 1:
        return False
    elif x < 0:
        return False
    
    elif x > 1:
        for i in range(1, x):
            if x % i == 0:
                factor += i
                
        if factor > x:
            return True
            
        else:
            return False


def isTriangular(x):
    """Returns whether or not a given number x is triangular.
    
    The triangular number Tn is a number that can be represented in the form of a triangular 
    grid of points where the first row contains a single element and each subsequent row contains 
    one more element than the previous one.
    
    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.
    
    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)
    
    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """
    
    if x == 0 or x == 1:
        return True
    for i in range(x):
        if x == i * (i + 1) / 2:
            return True
    else:
        return False
    

def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """
    length = len(str(x))
    digits = []
    numsum = 0
    
    
    
    if x in range(0, 10):
        return True
    elif x > 9:
        for num in str(x):
            digits.append(num)
            
        for i in list(digits):
            numsum += int(i) ** int(length)
            
    if numsum == x:
        return True
    else:
        return False
        

def main():

    playing = True
    while playing == True:

        num_input = input('Give me a number from 1 to 10000.  Type -1 to exit. ')

        try:
            num = int(num_input)

            if (num == -1):
                playing = False
                continue

            if (num <= 0 or num > 10000):
                continue

            factors = getFactors(num)
            print("The factors of", num, "are", factors)

            if isPrime(num):
                print(str(num) + ' is prime')
            if isComposite(num):
                print(str(num) + ' is composite')
            if isPerfect(num):
                print(str(num) + ' is perfect')
            if isAbundant(num):
                print(str(num) + ' is abundant')
            if isTriangular(num):
                print(str(num) + ' is triangular')
            if isNarcissistic(num):
                print(str(num) + ' is narcissistic')

        except ValueError:
            print('Sorry, the input is not an int.  Please try again.')
            


if __name__ == '__main__':
    main()







