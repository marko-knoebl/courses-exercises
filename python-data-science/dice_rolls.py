import numpy as np

dice = np.random.randint(1, 10, (10000, 10))

total = dice.sum(axis=1)

print(total.mean())
print(total.std())
