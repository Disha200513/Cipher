import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the data
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'World': [29.3, 32.5, 35.7, 38.9, 42.1, 44.8, 47.1, 49.5, 51.8, 53.6, 56.1],
    'Asia': [22.6, 25.5, 28.5, 31.4, 34.3, 37.2, 40.4, 43.1, 46.2, 48.4, 50.9],
    'Europe': [63.2, 67.0, 70.5, 73.5, 76.5, 78.9, 80.5, 82.1, 83.8, 85.2, 87.2],
    'Africa': [10.4, 12.0, 13.7, 15.4, 17.2, 19.3, 21.8, 23.7, 25.9, 27.8, 29.9],
    'Americas': [49.5, 51.9, 54.1, 56.3, 58.3, 60.3, 62.2, 64.1, 65.7, 67.5, 69.2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Melt the data for easier plotting
df_melted = df.melt(id_vars='Year', var_name='Region', value_name='Internet_Usage')

# Set the style and context
sns.set(style='whitegrid', context='talk')

# Create the figure and axes
plt.figure(figsize=(14, 8))

# Plot the data
sns.lineplot(x='Year', y='Internet_Usage', hue='Region', data=df_melted, marker='o')

# Adding titles and labels
plt.title('Global Internet Usage Over Time', fontsize=20, fontweight='bold')
plt.xlabel('Year', fontsize=16)
plt.ylabel('Internet Usage (%)', fontsize=16)
plt.legend(title='Region')

# Show the plot
plt.show()