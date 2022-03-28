import psutil
import sys
import os

counter = 0
parameter = sys.argv[1]
if parameter == "cpu":
  print("CPU")
  print("---")
  print("")
  print("cores")
  print("-----")
  print("-")
  print(psutil.cpu_count())
  print("-")
  print("")
  print("load average")
  print("------------")
  print(" 1    5    15")
  print("---  ---   ---")
  get_load_avarage=psutil.getloadavg()
  print(get_load_avarage[0],"",get_load_avarage[1]," ",get_load_avarage[2])
  print("")
  print("times")
  print("-----")
  print("     user nice system idle iowait irq softirq steal guest guest_nice")
  print("--   ---- ---- ------ ---- ------ --- ------- ----- ----- ----------")
  for cpu_work_time in psutil.cpu_times(percpu=True):
    counter = counter + 1
    print(counter,"",cpu_work_time.user,"",cpu_work_time.nice,""
    ,cpu_work_time.system,"",cpu_work_time.idle,"",cpu_work_time.iowait,""
    ,cpu_work_time.irq,"",cpu_work_time.softirq,"",cpu_work_time.steal,""
    ,cpu_work_time.guest,"",cpu_work_time.guest_nice)
  counter = 0
  print("")
  print("utilization")
  print("-----------")
  for cpu_work_precent in psutil.cpu_percent(percpu=True):
    counter = counter + 1
    if counter == len(psutil.cpu_percent(percpu=True)):
      print("",counter)
    else:
      print(" ",counter,end ="  ")
  counter = 0
  for cpu_work_precent in psutil.cpu_percent(percpu=True):
    counter = counter + 1
    if counter == len(psutil.cpu_percent(percpu=True)):
      print("----")
    else:
      print("----",end =" ")
  counter = 0
  for cpu_work_precent in psutil.cpu_percent(percpu=True):
    counter = counter + 1
    if counter == len(psutil.cpu_percent(percpu=True)):
      print("",cpu_work_precent)
    else:
      print("",cpu_work_precent,end =" ")
  counter = 0
elif parameter == "mem":
  print("MEMORY")
  print("------")
  print("")
  print("virtual memory")
  print("--------------")
  print("---------  ----------")
  print("total",psutil.virtual_memory().total)
  print("available",psutil.virtual_memory().available)
  print("percent",psutil.virtual_memory().percent)
  print("used",psutil.virtual_memory().used)
  print("free",psutil.virtual_memory().free)
  print("active",psutil.virtual_memory().active)
  print("inactive",psutil.virtual_memory().inactive)
  print("buffers",psutil.virtual_memory().buffers)
  print("cached",psutil.virtual_memory().cached)
  print("shared",psutil.virtual_memory().shared)
  print("slab",psutil.virtual_memory().slab)
  print("---------  ----------")
  print("")
  print("swap")
  print("----")
  print("-------  ----------")
  print("total",psutil.swap_memory().total)
  print("used",psutil.swap_memory().used)
  print("free",psutil.swap_memory().free)
  print("percent",psutil.swap_memory().percent)
  print("sin",psutil.swap_memory().sin)
  print("sout",psutil.swap_memory().sout)
  print("-------  ----------")
os.system("pause")
