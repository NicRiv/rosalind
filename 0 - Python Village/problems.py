#1 - Installing Python
print('Exercise one')
import this

#2 - Variables and Some Arithmetic
"""
Problem:
Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle 
        whose legs have lengths a and b. 
"""
print('\n', 'Exercise two')
a = 941
b = 893
result2 = a**2 + b**2
print(result2)

#3 - Strings and Lists
"""
Problem:
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), 
        inclusively. In other words, we should include elements s[b] and s[d] in our slice.
"""
print('\n', 'Exercise three')
Ai = 60
Af = 62
Bi = 83
Bf = 94
s = 'n6gU8Zp0B1I3k2D4McgObJM3DNfobLJ1XM16iAVgNBk7cIG4SZ8CxXglbxwxBoarebVP6YotwtoZaZSHfAQtaezanowskyiugXLLvIMafK1tbsKbPfVn3ERgsHd9nXwcx2RMmKmtmqwPC3hqwTwQDglwO7G0WVpomPL6SZq.'
result3 = s[Ai:Af+1] + ' ' + s[Bi:Bf+1]
print('-',result3,'-')

#4 - Conditions and Loops
"""
Problem:
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
"""
print('\n', 'Exercise four')
NUMBER_A = 4434
NUMBER_B = 8671
sum_of_odd_numbers = 0

for i in range(NUMBER_A, NUMBER_B + 1):
    if(i % 2 != 0):
        sum_of_odd_numbers += i

print(sum_of_odd_numbers)