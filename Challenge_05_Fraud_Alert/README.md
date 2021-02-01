# Challenge Details: 


Visa’s new in-app payment system uses a secure key for authentication and generates a related token for transmission to merchants. To speed up processing, a quick validation can be performed on this (key, token) pair to reject fraudulent submissions before backend verification, by using an adjacency check.


A key and token can be considered adjacent if:


they are the same length
each letter in the key is adjacent to a unique letter in the token
Two letters are adjacent if:


They are the same letter, or
They are lexigraphically adjacent, i.e.
J -> I, J -> K

(Z -> A is NOT adjacent)


For example, the strings CAT and SAD are adjacent as C -> D, A -> A and T -> S.


You can assume both the key and token contain only uppercase letters.


`("CAT", "SAD"), True)`


`("FAT", "SAD"), False)`



<ar>TEST CASES:</ar>

I can see why it's proving so contentious as from a purely technical perspective and as per the brief of what constitutes a key token pair you are right: an empty string should match an empty string. In this case it's the context of the question that matters:

The question states that they key token pair are used for authentication to access a financial system. No financial system built should be accepting an empty string for authentication. 

Again, appreciate that it's something that possibly should've been made clearer in the question but we're learning all the time. Hopefully going forward the challenges will have no ambiguity!!
Public | Can handle two simple, adjacent strings.
Public | Can handle two simple, non-adjacent strings.
1 Pts | Can handle handle two identical individual letters.
1 Pts | Can handle longer adjacent strings
2 Pts | Can handle strings with multiple repeat letters.
1 Pts | Can handle two individual letters that aren't adjacent.
1 Pts | Can handle two individual letters that are adjacent.
3 Pts | Can handle A and Z which are not adjacent.
4 Pts | Can handle scenario where one character has multiple adjacent and the other only has one.
