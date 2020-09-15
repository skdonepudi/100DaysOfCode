'''
Monk and Suffix Sort
Monk loves to play games. On his birthday, his friend gifted him a string S. Monk and his friend started playing a new game called as Suffix Game. In Suffix Game, Monk's friend will ask him lexicographically  smallest suffix of the string S. Monk wants to eat the cake first so he asked you to play the game.

Input Format:
First line contains a string S () and an integer k ().

Output Format:
Print the lexicographically  smallest suffix of the string S.

Sample Input:
aacb 3
Sample Output:
b

Explanation
All the suffices of the string are:
aacb
acb
cb
b

After sorting the order of the suffices will be:
aacb
acb
b
cb

3rd smallest suffix will be b.

'''

def suffixsort(s, k): 
   
    a = []
    n = len(s)
    for i in range(n): 
        a.append(s[i: n]); 
    
    a.sort()
    print (a[k-1])

s,k = input().split(maxsplit=1)
suffixsort(s,int(k))