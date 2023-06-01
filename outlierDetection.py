import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSetV3.csv')
output_csv = 'C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSetV3Outliers.csv'

# Select the columns that you want to check for outliers
columns_to_check = [
    'song.segments_confidence', 'song.sections_confidence', 'song.segments_start', 'song.sections_start',
    'songs.bars_start', 'song.bars_confidence', 'song.beats_start', 'song.beats_confidence',
    'song.duration', 'song.end_of_fade_in', 'song.key', 'song.key_confidence',
    'song.loudness', 'song.mode', 'song.mode_confidence', 'song.start_of_fade_out',
    'song.tempo', 'song.time_signature', 'song.time_signature_confidence'
]

# Define a function to detect outliers using the IQR method
def detect_outliers_iqr(data, threshold=1.5):
    # Calculate the first quartile (Q1)
    Q1 = data.quantile(0.25)
    # Calculate the third quartile (Q3)
    Q3 = data.quantile(0.75)
    # Calculate the IQR
    IQR = Q3 - Q1
    # Define the lower and upper bounds for outliers
    lower_bound = Q1 - threshold * IQR
    upper_bound = Q3 + threshold * IQR
    # Identify outliers
    outliers = (data < lower_bound) | (data > upper_bound)
    return outliers

# Iterate over the selected columns and detect outliers
for column in columns_to_check:
    outliers = detect_outliers_iqr(df[column])
    print(f"Outliers in column '{column}':")
    print(df[outliers])

# Alternatively, you can remove the outliers from the DataFrame
# df = df[~outliers]

# Save the updated DataFrame to a new CSV file
output_directory = os.path.dirname(output_csv)
os.makedirs(output_directory, exist_ok=True)
df.to_csv(output_csv, index=False)
