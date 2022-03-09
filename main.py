import threading
import random,time

max_showers=1
from threading import BoundedSemaphore,Thread
container=BoundedSemaphore(max_showers)

def woman(nloops):
  container.acquire()
  print("Женщина заняла душевую")
  for i in range(nloops):
    time.sleep(random.randrange(2,5))
  try:
    container.release()
    print("Женщина вышла из душевой.")
  except ValueError:
    print("Занято.")

def man(nloops):
  for i in range(nloops):
    time.sleep(random.randrange(2,5))
    if container.acquire(False):
      print("Душевая свободна.Мужчина заходит в душевую")
    else:
      print("Душевая занята.Нужна проверка на пол")

threads=[]
nloops=random.randrange(3,6)
threads.append(Thread(target=woman,args=(nloops,)))
threads.append(Thread(target=man,args=(random.randrange(nloops,nloops+max_showers+2),)))
for thread in threads: #Starts all the threads.
  thread.start()
for thread in threads: #Waits for threads to complete
  thread.join()
print("Кто-либо вышедший идет за пивом")

