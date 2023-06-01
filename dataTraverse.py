import os
import pandas as pd
import h5py
import numpy as np

dataset_path = 'C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\MillionSongSubset'
output_csv = 'C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSetV4.csv'

# Initialize an empty dictionary to store the data
data = {}

# Add the headers
headers = ['artist_mbid', 'artist_mbtags', 'artist_mbtags_count', 'artist_name', 'artist_playmeid',
           'artist_terms', 'artist_terms_freq', 'artist_terms_weight', 'audio_md5', 'bars_confidence',
           'bars_start', 'beats_confidence', 'beats_start', 'danceability', 'duration', 'end_of_fade_in',
           'energy', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'release',
           'release_7digitalid', 'sections_confidence', 'sections_start', 'segments_confidence',
           'segments_loudness_max', 'segments_loudness_max_time', 'segments_loudness_start',
           'segments_pitches', 'segments_start', 'segments_timbre', 'similar_artists', 'song_hotttnesss',
           'song_id', 'start_of_fade_out', 'tatums_confidence', 'tatums_start', 'tempo',
           'time_signature', 'time_signature_confidence', 'title', 'track_7digitalid', 'track_id', 'year']



for header in headers:
    data[header] = []

# Process the data for each object in the H5 file
def process_data(name, obj):
    if isinstance(obj, h5py.Dataset):
        for header in headers:
            if name.endswith(header):
                data[header].append(obj[()])

# Traverse through the dataset folders and subfolders
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.endswith(".h5"):
            file_path = os.path.join(root, file)
            # Read the h5 file
            with h5py.File(file_path, 'r') as f:
                # Visit all objects in the file
                f.visititems(process_data)

# Find the maximum length among the arrays
max_length = max(len(data[header]) for header in headers)

# Fill missing values with NaN
for header in headers:
    length = len(data[header])
    if length < max_length:
        data[header].extend([np.nan] * (max_length - length))

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
output_directory = os.path.dirname(output_csv)
os.makedirs(output_directory, exist_ok=True)
df.to_csv(output_csv, index=False)
