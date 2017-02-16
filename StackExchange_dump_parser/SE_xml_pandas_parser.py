#! python3
from pathlib import Path
import os, xmltodict, codecs
import pandas as pd

dataFolderPath = Path(Path(os.path.realpath(__file__)).parent.parent, 'gaming.stackexchange.com')

# reads in Tags.xml
with codecs.open(Path(dataFolderPath, 'Tags.xml'), 'r', 'utf-8') as fd:
    doc = xmltodict.parse(fd.read())
    

# Converts .xml files in StackExchange data dump to a pandas data frame, where each <row/> object gives an observation with corresponding attribute names as column names.
df = pd.DataFrame.from_dict(doc['tags']['row'])
df = df.rename(columns = lambda x : str(x)[1:]) # remove @ 
print(df)
