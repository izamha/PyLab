import pandas as pd

# Define a dict containing employee data
data = {'Name': ['jai', 'Prince', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Kampala', 'Musanze', 'Kigali', 'Kayonza'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dict to DataFrame
df = pd.DataFrame(data)

# Select two columns
print(df[['Name', 'Qualification']])
