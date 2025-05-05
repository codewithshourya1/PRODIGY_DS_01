import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
# Generate Sample Data
np.random.seed(42)
ages = np.random.randint(10, 80, 500)
genders = np.random.choice(["Male", "Female"], size=500, p=[0.5, 0.5])
df = pd.DataFrame({'Age': ages, 'Gender': genders})
df.head()
#Step 4: Create Histogram for Age Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Age'], bins=20, kde=True, color='blue') 
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution in the Population")
plt.savefig("age distribution.png") #save image 
plt.show()
#Step 5: Create Bar Chart for Gender Distribution
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="pastel")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("gender  Distribution in the Population")
plt.savefig("gender distribution.png") #save image 
