numbers = tuple(map(float, input().split()))

numbers_counter = {}

for number in numbers:
    if number not in numbers_counter:
        numbers_counter[number] = 0
    numbers_counter[number] += 1

for k, v in numbers_counter.items():
    print(f"{k} - {v} items")

