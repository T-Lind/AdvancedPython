import time, random

max = 2_147_483_647
n_items = 10_000_000
gen = (random.randint(-max, max) for _ in range(n_items))
print("Starting sorting...")
before = time.time()
sorted(gen)
after = time.time()
total_ms = (after - before) * 1000
print(f"{total_ms} milliseconds")
