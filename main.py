from multi_threading import solve_with_threads
from multi_processing import solve_with_processes
import pandas as pd

if __name__ == '__main__':
  with open("data.csv") as file:
    data = [line.strip() for line in file]

  data = list(map(int, data))

  register_mprocs = solve_with_processes(data)
  register_mthread = solve_with_threads(data)

  df1 = pd.DataFrame(data=register_mthread)
  df2 = pd.DataFrame(data=register_mprocs)
  with pd.ExcelWriter('dados.xlsx') as writer:
    df1.to_excel(writer, sheet_name='threads', index=False)
    df2.to_excel(writer, sheet_name='processes', index=False)