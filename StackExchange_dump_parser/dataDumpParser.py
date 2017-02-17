#! python3

from pathlib import Path
import xmltodict
import pandas as pd
import re

def splitTags(series):
    tagRegex = re.compile(r'^<(\S+)>$')
    tags_series = []
    for tags in series:
        try:
            tags_series.append(list(tagRegex.search(tags).groups()))
        except AttributeError:
            tags_series.append(None)
    return tags_series
	
# def removeAtSymbol(df):
	# return df.rename(columns = lambda x : str(x)[1:])

dataFolderPath = Path(Path(__file__).parent.parent, 'xmldata', 'gaming.stackexchange.com')

# convert .xml to pandas dataframe
def streamingXML(filename):
    stream_list = []
    def handle(path, item):
        stream_list.append(path[1][1]) # modifying global variable...any way to avoid this?
        return True    
    
    with open(Path(dataFolderPath, filename), encoding='utf-8') as fd:
        xmltodict.parse(fd.read(), item_depth=2, item_callback=handle)
    df_xml = pd.DataFrame(stream_list)
    return df_xml

# reads in ags.xml
df_tags = streamingXML('Tags.xml')
# print(df_tags[:5])

# reads in Posts.xml
df_posts = streamingXML('Posts.xml')

df_tags.to_csv(Path(Path(__file__).parent.parent, 'csvdata', 'Tags.csv'))
df_posts.to_csv(Path(Path(__file__).parent.parent, 'csvdata', 'Posts.csv'))
  

# # reads in Posts.xml    
# with open(Path(dataFolderPath, 'Posts.xml'), encoding='utf-8') as fd:
    # posts_doc = xmltodict.parse(fd.read(), item_depth=1, item_callback=handle)

    
# # Converts .xml files in StackExchange data dump to a pandas data frame, where each <row/> object gives an observation with corresponding attribute names as column names.
# df_tags = pd.DataFrame.from_dict(tags_doc['tags']['row'])
# # df_tags = df_tags.rename(columns = lambda x : str(x)[1:]) # remove @ 
# df_tags = removeAtSymbol(df_tags)

# df_posts = pd.DataFrame.from_dict(posts_doc['posts']['row'][:10])
# df_posts = removeAtSymbol(df_posts)

# # TODO: split the tags of each post into a list
# df_posts.assign(tags_list = splitTags(df_posts.Tags))