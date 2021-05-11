# 18. Exercise: Using countable additivity
# Let the sample space be the set of positive integers
# and suppose that P(n)=1/2n, for n=1,2,…
# Find the probability of the set {3,6,9,…}, that is,
# of the set of of positive integers that are multiples of 3.

n = 3000000
x = 0

for i in range(1, n):
    x = x + pow(0.5, i * 3)

print(str(x))
