from statistics import mean
from utils import split_list_into_chunks, how_much_primes
import concurrent.futures
import time


def solve_with_processes(data):
  print(f'Analyzing {len(data)} entries...')

  processes_for_test = [2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 80, 100, 125, 200, 250]
  number_of_tests = 50
  register = {'processes': processes_for_test, 'simple_time': [], 'mproc_time': []}

  for number_of_procs in processes_for_test:
    timer_simple = []
    timer_mproc = []

    for _ in range(number_of_tests):
      t1 = time.perf_counter()
      number_of_primes_mprocs = 0
      with concurrent.futures.ProcessPoolExecutor() as executor:
        chunks = split_list_into_chunks(data, number_of_procs)
        results = executor.map(how_much_primes, chunks)
        number_of_primes_mprocs += sum(results)
      t2 = time.perf_counter()
      timer_mproc.append(t2-t1)

      t3 = time.perf_counter()
      number_of_primes_simple = 0
      chunks = split_list_into_chunks(data, number_of_procs)
      for chunk in chunks:
        number_of_primes_simple += how_much_primes(chunk)
      t4 = time.perf_counter()
      timer_simple.append(t4-t3)

    mean_simple = mean(timer_simple)
    mean_mproc = mean(timer_mproc)
    register['simple_time'].append(mean_simple)
    register['mproc_time'].append(mean_mproc)

    print(f'Number of primes on simple approach: {number_of_primes_simple}, calculated in {round(t4-t3, 3)} second(s)')
    print(f'Number of primes using {number_of_procs} processes approach: {number_of_primes_mprocs}, calculated in {round(t2-t1, 3)} second(s)')
    print(f'Speed Up = {round(mean_simple/mean_mproc, 3)}\n')

  return register