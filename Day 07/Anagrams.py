'''
Anagrams

Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Input :

test cases,t
two strings a and b, for each test case
Output:

Desired O/p

Constraints :

string lengths<=10000

Note :

Anagram of a word is formed by rearranging the letters of the word.

For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.

SAMPLE INPUT 
1
cde
abc
SAMPLE OUTPUT 
4
'''

from collections import Counter

for _ in range(int(input())):

   a=list(input())

   b=list(input())

   x=Counter(a)

   y=Counter(b)

   x.subtract(y)

   print(sum(abs(i) for i in x.values()))