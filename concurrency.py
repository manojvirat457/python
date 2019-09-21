import concurrent.futures as future
import time

start = time.perf_counter() # start time

# This function is to calculating the runtime
def sleepFor(duration):
    time.sleep(duration)
    print(f"currect runtime {duration}")
    
with future.ThreadPoolExecutor() as executor:
    durations = [1, 2, 5, 7, 1, 0.5]
    executor.map(sleepFor, durations)

finish = time.perf_counter()

print(f'\nFinished in {round(finish-start, 2)} seconds(s)')