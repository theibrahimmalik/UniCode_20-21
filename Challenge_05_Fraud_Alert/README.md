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
