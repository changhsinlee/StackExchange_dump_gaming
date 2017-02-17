#! python3
import pprint
import pandas as pd
from sklearn import linear_model

# With an input of a set of tags, return either 1) the most relevant tags missing or 2) the tag that is likely to get most views?
# problem: if aim is most views, irrelevant tag may show up (e.g. ubisoft in star-craft?)
# df_post: post.xml
# df_tags: tags.xml

# TODO: fetch master list of tags
# tags_list = df_tags['Tags']
tags_list = ['a','b','c','d','e','f']

# convert the column of list of tags to a column of list of 0,1 based on tags_list
df_post = df_post.assign(vector = df.Tags.map(lambda x: pd.Series(tags_list).isin(x).astype(int)))
df_training_data = pd.DataFrame()
df_training_data[tags_list] = df_post.vector.apply(lambda x: pd.Series(x))

# TODO: build content-based recommender (don't try collaborate filtering yet)
# Try ranking by logistic regression first (won't recommend completely new tag)
# basically a bunch of models, one for each tag...
model_list = []
for model_num in range(len(tags_list)):
    # TODO: build a model 
    x = df_training_data.drop(df_training_data.columns[model_num], axis=1)
    y = df_training_data.iloc[:, model_num]
    model_list[model_num] = logreg = linear_model.LogisticRegression.fit(x,y) # logistic regression y~x

# TODO: fetch a set of tags input as a list of string
tags = ['a','b']

# TODO: feed into recommender
# rec_tags = recommender(input_tags)
rec_tags = ['ccc', 'ddd']


# print tags
print('People who tagged ' + ', '.join(tags) + ' also tagged: ')
print('\n'.join(rec_tags))