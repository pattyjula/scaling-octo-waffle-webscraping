# DESC: Create a list of all the Parcel Identification Numbers (PIN) in the
#       city of Los Angeles using the Pandas library.

# Import library
import pandas as pd

# Define CSV file
file_pin= 'Resources/parcels.csv'

df = pd.read_csv(file_pin)

# Delete extra columns
df.drop(["the_geom", "ID", "ASSETID", "MAPSHEET", "BPP", "MAP_REF","TRACT","PIND", "BLOCK","MOD", "LOT","ARB", "ENG_DIST","CNCL_DIST", "LST_MODF_D","CRTN_DT"], axis=1, inplace=True)

df.to_csv('./Resources/parcels_reduce.csv')
#query PIN column
df2=df[["PIN"]]

# Save PIN values to a list
my_list = df2["PIN"].tolist()
