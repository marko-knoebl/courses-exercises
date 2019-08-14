# Digit classification

The digit dataset contains 8x8 images of handwritten digits along with their correct label.

The dataset can be loaded via:

```py
from sklearn import datasets

digits = datasets.load_digits()
```

We can inspect the data via:

```
print(digits.images[:5])
print(digits.target[:5])
```

Use various classification algorithms on the data (split into train and test data). Assess their efficiency by printing their _accuracy_ and _confusion matrix_.
