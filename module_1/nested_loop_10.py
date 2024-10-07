import time

start_time = time.time()

for i in range(1000):
    for j in range(10):
        print(0, end=" ")
    print()

print(round((time.time() - start_time), 2))
