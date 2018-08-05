import random
import sys
import math

def one_time_check(number):
    return pow(random.randint(2, number - 1), number - 1, number) != 1

def primality_check(number, tries):
    for i in range(0, tries):
         if one_time_check(number):
             return '{} is most probably not a prime number'.format(number)
    return '{} is most probably a prime number'.format(number)

if __name__ == "__main__":
    print(primality_check(int(sys.argv[1]), int(math.ceil(int(sys.argv[1]) / 2))))
