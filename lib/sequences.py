#!/usr/bin/env python3

def print_fibonacci(length):
  fibo_array = []
  if length == 0:
    print(fibo_array)
  elif length == 1:
    fibo_array = [0]
    print(fibo_array)
  else:
    fibo_array = [0, 1]
    for i in range(2, length):
        fibo_array.append(fibo_array[-1] + fibo_array[-2])
    print(fibo_array)