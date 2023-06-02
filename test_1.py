# Prueba de Pull Request

import pandas as pd

# Create a list of column names
columns = ["Name", "Age", "Gender", "Country", "City", "Income", "Education", "Occupation"]

# Generate a DataFrame with 100 cases
df = pd.DataFrame(columns=columns)

# Fill the DataFrame with random data
for i in range(100):
  df["Name"] = np.random.choice(["John", "Mary", "Peter", "Susan"], 1)
  df["Age"] = np.random.randint(18, 65, 1)
  df["Gender"] = np.random.choice(["Male", "Female"], 1)
  df["Country"] = np.random.choice(["USA", "Canada", "UK", "Australia"], 1)
  df["City"] = np.random.choice(["New York", "Los Angeles", "Chicago", "Toronto"], 1)
  df["Income"] = np.random.randint(10000, 100000, 1)
  df["Education"] = np.random.choice(["High School", "College", "Graduate School"], 1)
  df["Occupation"] = np.random.choice(["Doctor", "Lawyer", "Engineer", "Teacher"], 1)
  
# Print the DataFrame
print(df)