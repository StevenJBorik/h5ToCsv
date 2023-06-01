import pandas as pd

# Read the main dataset
main_dataset_path = 'C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSubSetV3.csv'
main_dataset = pd.read_csv(main_dataset_path)

# Read the mapping file
mapping_file_path = 'C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSubSetV3GenreEncodingV2.csv'
mapping_file = pd.read_csv(mapping_file_path)

# Create a dictionary of term mappings
term_mappings = dict(zip(mapping_file['artist_terms'], mapping_file['encoded_terms']))

# Replace artist.terms values with encoded terms
main_dataset['artist.terms'] = main_dataset['artist.terms'].map(term_mappings)

# Save the updated dataset to a new CSV file
output_csv = 'C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSubSetV3Encoded.csv'
main_dataset.to_csv(output_csv, index=False)
