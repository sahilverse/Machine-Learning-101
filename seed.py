import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducibility

# Generate 1000 random study hours between 1 and 12
hours = np.random.uniform(1, 12, 1000)

# Generate marks roughly as: marks = 8.5 * hours + noise, clipped between 0 and 100
noise = np.random.normal(0, 5, 1000)  # noise with std dev 5
marks = 8.5 * hours + noise

# Clip marks to max 100 and min 0
marks = np.clip(marks, 0, 100)

# Create DataFrame
df = pd.DataFrame({
    'hours': np.round(hours, 2),
    'marks': np.round(marks, 2)
})

# Save to CSV
df.to_csv('data/student_scores_1000.csv', index=False)

print("CSV file 'student_scores_1000.csv' with 1000 student records created.")
