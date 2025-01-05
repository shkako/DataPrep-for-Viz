import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/s9531f/Desktop/historical-cost-of-computer-memory-and-storage.csv')



# Step 3: Use melt() to reshape the DataFrame
df_melted = df.melt(id_vars=['Year','Code'], 
                    value_vars=['Historical price of flash memory', 
                                 'Historical price of disk drives', 
                                 'Historical price of solid-state drives',
                                 'Historical price of memory',], 
                    var_name='Type', 
                    value_name='Price')

# Step 4: Clean up the 'Type' column if needed (remove the common prefix part)
df_melted['Type'] = df_melted['Type'].str.replace('Historical price of ', '', regex=False)

# Step 5: Save the reshaped DataFrame back to a CSV
df_melted.to_csv('your_modified_file_pivoted.csv', index=False)

df_check = pd.read_csv('your_modified_file_pivoted.csv')

df_melted.to_csv(r'C:\Users\s9531f\Desktop\historical-cost-of-computer-memory-and-storage_python.csv', index=False)


