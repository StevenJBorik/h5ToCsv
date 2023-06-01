import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Read the CSV file
df = pd.read_csv('C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSubSetV3.csv')
output_csv = 'C:\\Users\\SBD2RP\\OneDrive - MillerKnoll\\installs\\Desktop\\songDataSubSetV3Encoding.csv'

# Extract unique artist.terms values
artist_terms = df['artist.terms'].unique()

# Perform label encoding
label_encoder = LabelEncoder()
encoded_terms = label_encoder.fit_transform(artist_terms)

# Create a dictionary of term mappings
term_mappings = {term: encoded for term, encoded in zip(artist_terms, encoded_terms)}

# Create a new DataFrame for term mappings
mappings_df = pd.DataFrame({'artist_terms': artist_terms, 'encoded_terms': encoded_terms})

# Save the updated DataFrame to a new CSV file
output_directory = os.path.dirname(output_csv)
os.makedirs(output_directory, exist_ok=True)
mappings_df.to_csv(output_csv, index=False)