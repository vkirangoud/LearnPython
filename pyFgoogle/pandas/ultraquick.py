import numpy as np
import pandas as pd

# Creating a DataFrame
mydata = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]]);
# create a python list that holds the names of the two columns
my_column_names = ['temperature', 'activity']

#Create a DataFrame.
my_dataframe = pd.DataFrame(data=mydata, columns=my_column_names)

# print the entire DataFrame
print(my_dataframe)

# add new column named "adjusted"
my_dataframe["adjusted"] = my_dataframe["activity"] + 2
# print the entire DataFrame
print(my_dataframe)

print("Rows #0, #1, and #2:")
print(my_dataframe.head(3), '\n')

print("Row #2:")
print(my_dataframe.iloc[[2]], '\n')

print("Rows #1, #2, and #3:")
print(my_dataframe[1:4], '\n')

print("Column 'temperature':")
print(my_dataframe['temperature'])

# Task 1
xnew_array = np.random.randint(low=1, high=100,size=(3,4))
col_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason'];
my_frame = pd.DataFrame(data=xnew_array, columns=col_names)
print(my_frame)
# The value in the cell of row # 1 of the Eleanor column
print(my_frame.iloc[1]['Eleanor'])
my_frame['Janet'] = my_frame['Tahani'] + my_frame['Jason']
print(my_frame)

# Referencing if you assign a DataFrame to a new variable, any change to the DataFrame
# or to the new variable will be reflected in the  other

# Copying. if you call the pd.DataFrame.copy method - you create a true independent
#  copy and changes to one will not reflect in the other.
print('Experiment with a reference:')
reference_to_df = my_frame;
# Print the starting value of a particular cell.
print(" Starting value of my_frame: %d" % my_frame['Jason'][1])
print(" Starting value of reference_my_frame: %d" % reference_to_df['Jason'][1])

# Modify a cell in my_frame
my_frame.at[1,'Jason'] = my_frame['Jason'][1] + 5
print("  Updated my_frame: %d" % my_frame['Jason'][1])
print("  Updated reference_to_df: %d\n\n" % reference_to_df['Jason'][1])

# Create a true copy of my_dataframe
print("Experiment with a true copy:")
copy_of_my_dataframe = my_dataframe.copy()

# Print the starting value of a particular cell.
print("  Starting value of my_dataframe: %d" % my_dataframe['activity'][1])
print("  Starting value of copy_of_my_dataframe: %d\n" % copy_of_my_dataframe['activity'][1])

# Modify a cell in df.
my_dataframe.at[1, 'activity'] = my_dataframe['activity'][1] + 3
print("  Updated my_dataframe: %d" % my_dataframe['activity'][1])
print("  copy_of_my_dataframe does not get updated: %d" % copy_of_my_dataframe['activity'][1])
