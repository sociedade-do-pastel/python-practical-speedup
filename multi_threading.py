from statistics import mean
from utils import split_list_into_chunks, how_much_primes
import concurrent.futures
import time


def solve_with_threads(data):
  print(f'Analyzing {len(data)} entries...')

  threads_for_test = [2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 80, 100, 125, 200, 250]
  number_of_tests = 50
  register = {'threads': threads_for_test, 'simple_time': [], 'mthread_time': []}

  for number_of_threads in threads_for_test:
    timer_simple = []
    timer_mthread = []

    for _ in range(number_of_tests):
      t1 = time.perf_counter()
      number_of_primes_mthreads = 0
      with concurrent.futures.ThreadPoolExecutor() as executor:
        chunks = split_list_into_chunks(data, number_of_threads)
        results = executor.map(how_much_primes, chunks)
        number_of_primes_mthreads += sum(results)
      t2 = time.perf_counter()
      timer_mthread.append(t2-t1)

      t3 = time.perf_counter()
      number_of_primes_simple = 0
      chunks = split_list_into_chunks(data, number_of_threads)
      for chunk in chunks:
        number_of_primes_simple += how_much_primes(chunk)
      t4 = time.perf_counter()
      timer_simple.append(t4-t3)

    mean_simple = mean(timer_simple)
    mean_mthread = mean(timer_mthread)
    register['simple_time'].append(mean_simple)
    register['mthread_time'].append(mean_mthread)

    print(f'Number of primes on simple approach: {number_of_primes_simple}, calculated in {round(mean_simple, 3)} second(s)')
    print(f'Number of primes using {number_of_threads} threads approach: {number_of_primes_mthreads}, calculated in {round(mean_mthread, 3)} second(s)')
    print(f'Speed Up = {round(mean_simple/mean_mthread, 3)}\n')

  return register