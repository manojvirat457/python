import time
import threading


start = time.perf_counter() # start time

# This function is to calculating the runtime
def sleepFor(duration):
    print(f"Sleep for {duration} second")
    time.sleep(duration)
    print("sleep Completed")

# Creating Threads
thread1 = threading.Thread(target=sleepFor, args=[1.0])
thread2 = threading.Thread(target=sleepFor, args=[3.0])
thread3 = threading.Thread(target=sleepFor, args=[5.0])

# Starting Threads
thread1.start()
thread2.start()
thread3.start()

# Joining Threads
thread1.join()
thread2.join()
thread3.join()

finish = time.perf_counter()

print(f'\nFinished in {round(finish-start, 2)} seconds(s)')