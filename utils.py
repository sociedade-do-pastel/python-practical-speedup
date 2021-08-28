import numpy as np
import sympy as sp

def split_list_into_chunks(data, number_of_chunks):
  return np.array_split(data, number_of_chunks)

def how_much_primes(data):
  number_of_primes = 0

  for number in data:
    if sp.isprime(number):
      number_of_primes += 1

  return number_of_primes