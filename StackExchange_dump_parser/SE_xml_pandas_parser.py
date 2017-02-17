#! python3

from pathlib import Path
import xmltodict, codecs
import pandas as pd

dataFolderPath = Path(Path(__file__).parent.parent, 'gaming.stackexchange.com')

# reads in Tags.xml
with codecs.open(Path(dataFolderPath, 'Tags.xml'), 'r', 'utf-8') as fd:
    tags_doc = xmltodict.parse(fd.read())
    
# reads in Posts.xml    
with codecs.open(Path(dataFolderPath, 'Posts.xml'), 'r', 'utf-8') as fd:
    posts_doc = xmltodict.parse(fd.read())

    
# Converts .xml files in StackExchange data dump to a pandas data frame, where each <row/> object gives an observation with corresponding attribute names as column names.
df_tags = pd.DataFrame.from_dict(tags_doc['tags']['row'])
df_tags = df_tags.rename(columns = lambda x : str(x)[1:]) # remove @ 

df_posts = pd.DataFrame.from_dict(posts_doc['posts']['row'][:5])
print(df_tags[:5])
print(df_posts)

