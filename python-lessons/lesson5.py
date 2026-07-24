# Countdown using a while loop
# While loops are great when you do not know when the task will end
print()
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast Off!!!!!!!")
print()

# Build a simple rep counter
for index, rep in enumerate(range(1, 4), start=1):
    print(f"{index}. This is rep no: {rep}")