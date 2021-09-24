import time
import random

# Starting messages
print("Welcome to the random dice!")
time.sleep(1.5)

while True:
    input("Press enter to continue.")
    cpu = random.choice([1,2,3,4,5,6])
    time.sleep(1.5)
    print(f"The dice rolled {cpu}")
    time.sleep(1.5)