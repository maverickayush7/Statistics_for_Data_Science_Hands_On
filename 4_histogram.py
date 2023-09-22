import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate synthetic exam scores
np.random.seed(0)
exam_scores = np.random.randint(50, 100, size=100)

# Create a histogram with Seaborn
plt.figure(figsize=(8, 6))
sns.histplot(exam_scores, bins=100, kde=True)     # if bins value is increased 
plt.xlabel("Exam Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Exam Scores")
plt.show()