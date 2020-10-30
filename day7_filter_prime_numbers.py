# Required concepts: https://www.w3schools.com/python/python_intro.asp map, filter, lambda

print('Question: prime numbers in list,')

def check_prime(num):
  # note: you can end the for loop at √num
  for i in range(2,num):
    if num == 1:
      return False
    if num%i == 0:
      # you found a factor of num!
      return False
  # you didn't find any multiple, you're prime
  return True

li = [2,3,4,5,6,7,8,9]
print(li)

primes = filter(check_prime,li)

print(list(primes))