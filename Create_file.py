
#Assign a vsriable for the file to load and the path
import csv
import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    
    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
