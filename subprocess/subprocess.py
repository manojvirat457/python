import subprocess


p1 = subprocess.run(['dir'], shell=True, capture_output=True)


#log creation
with open('log.txt', 'w') as logFile:
    process1 = subprocess.run('dir', stdout=logFile, text=True, shell=True)

print(p1.stdout.decode())