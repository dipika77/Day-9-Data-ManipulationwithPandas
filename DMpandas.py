#Transfroming DataFrames
#instructions
'''Print the head of the homelessness DataFrame.'''

# Print the head of the homelessness data
print(homelessness.head())


#instructions
'''Print the head of the homelessness data.
Print information about homelessness.
Print the number of rows and columns in homelessness.
Print a description of homelessness'''

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())


#instructions
'''Import pandas using the alias pd.
Print a 2D NumPy array of the values in homelessness.
Print the column names of homelessness.
Print the index of homelessness.'''

# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)


#Sorting and Subsetting
#instructions
'''Sort homelessness by the number of homeless individuals in the individuals column, 
from smallest to largest, and save this as homelessness_ind.
Print the head of the sorted DataFrame.
Sort homelessness by the number of homeless family_members in descending order,
and save this as homelessness_fam.
Sort homelessness first by region (ascending), and then by number of family members (descending).
Save this as homelessness_reg_fam.'''

# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending = False)

print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending = [True,False])

# Print the top few rows
print(homelessness_reg_fam.head())


#instructions
'''Create a Series called individuals that contains only the 
individuals column of homelessness.
Create a DataFrame called state_fam that contains only the state and 
family_members columns of homelessness, in that order.
Create a DataFrame called ind_state that contains the individuals and state columns
of homelessness, in that order.'''

# Select the individuals column
individuals = homelessness["individuals"]

print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

print(ind_state.head())


#instructions
'''Filter homelessness for cases where the number of individuals is greater than
ten thousand, assigning to ind_gt_10k. View the printed result.
Filter homelessness for cases where the USA Census region is "Mountain",
assigning to mountain_reg. View the printed result.
Filter homelessness for cases where the number of family_members is less than one
thousand and the region is "Pacific", assigning to fam_lt_1k_pac. View the printed result.'''

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)

#instructions
'''Filter homelessness for cases where the USA census state is in the list of 
Mojave states,canu, assigning to mojave_homelessness. View the printed result.'''

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)


