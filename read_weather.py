import os
import pandas as pd

# File path
file_path = 'weather_data.txt'
absolute_path = os.path.abspath(file_path)

# Print the file path for verification
print(f"Checking file at: {absolute_path}")

# Initialize lists to store data
date = []
prep = []
snow_fall = []
snow_depth = []
min_temp = []
max_temp = []

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: File not found at {absolute_path}")
else:
    try:
        # Open and read the file
        with open(file_path, "r") as file:
            for line in file:
                # Split the line by tab and extract columns
                array = line.strip().split("\t")
                date.append(array[0])
                prep.append(round(float(array[1]),5))  # Convert to float for numeric columns
                snow_fall.append(round(float(array[2]),5))
                snow_depth.append(round(float(array[3]),5))
                min_temp.append(round(float(array[4]),5))
                max_temp.append(round(float(array[5]),5))

        # Create a DataFrame
        dataframe = pd.DataFrame({
            "timestamp": pd.to_datetime(date),
            "prep": prep,
            "snow": snow_fall,
            "snow_depth": snow_depth,
            "min_temp": min_temp,
            "max_temp": max_temp,
        })

        # Save the DataFrame to a CSV file
        output_path = "weather_csv.csv"
        dataframe.to_csv(output_path, index=False)
        print(f"Data successfully saved to {output_path}")

    except Exception as e:
        print(f"Error loading result: {e}")

