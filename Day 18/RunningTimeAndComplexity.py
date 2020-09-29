'''
Objective
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!

Task
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it's  or .
Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Input Format
The first line contains an integer, , the number of test cases.
Each of the  subsequent lines contains an integer, , to be tested for primality.


Output Format
For each test case, print whether  is  or  on a new line.

Sample Input
3
12
5
7

Sample Output
Not prime
Prime
Prime

'''


import math
for i in range(int(input())):
    n=int(input())
    sq=math.ceil(math.sqrt(n))
    if n==1:
        print("Not prime")
    elif n==2:
        print("Prime")
    else:    
        for i in range(2,sq+1):
            if n%i==0:
                print("Not prime")
                break
        else:
            print("Prime")