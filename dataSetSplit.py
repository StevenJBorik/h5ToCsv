import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Read the dataset from CSV
df = pd.read_csv('C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSubSetV3Encoded.csv')

# Shuffle the dataset
df_shuffled = df.sample(frac=1, random_state=42)

# Perform an 80-20 split
train_df, test_df = train_test_split(df_shuffled, test_size=0.2, random_state=42)

# Specify the output directory and create it if it doesn't exist
output_directory = 'C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\output'
os.makedirs(output_directory, exist_ok=True)

# Save the shuffled and split data into separate CSV files
train_df.to_csv(os.path.join(output_directory, 'train_data_v1.csv'), index=False)
test_df.to_csv(os.path.join(output_directory, 'test_data_v1.csv'), index=False)
