import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: Create a NumPy array of numbers from 1 to 10 and calculate the mean
arr = np.arange(1, 11)
mean_value = np.mean(arr)
print(f"NumPy array: {arr}")
print(f"Mean value: {mean_value}")

# Task 2: Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 29],
    "Height_cm": [165, 180, 175, 170, 160],
    "Weight_kg": [65, 80, 75, 70, 60]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary statistics:")
print(df.describe())

# Task 3: Fetch data from a public API using requests and print a key piece of information
response = requests.get("https://api.agify.io?name=michael")
if response.status_code == 200:
    result = response.json()
    print(f"\nAPI response: The predicted age for the name '{result['name']}' is {result['age']}.")
else:
    print("Failed to fetch data from the API.")

# Task 4: Plot a simple line graph using matplotlib
numbers = [1, 3, 2, 5, 7, 8, 6, 9, 10, 12]
plt.plot(numbers)
plt.title("Simple Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
