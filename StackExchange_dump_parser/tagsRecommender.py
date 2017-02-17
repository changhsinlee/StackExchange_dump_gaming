#! python3
import pprint

# With an input of a set of tags, return either 1) the most relevant tags missing or 2) the tag that is likely to get most views?
# problem: if aim is most views, irrelevant tag may show up (e.g. ubisoft in star-craft?)

# TODO: fetch a set of tags input as a list of string
tags = ['aaa','bbb']

# TODO: build content-based recommender (don't try collaborate filtering yet)
# Try ranking by logistic regression first 

# TODO: feed into recommender
# rec_tags = recommender(input_tags)
rec_tags = ['ccc', 'ddd']


# print tags
print('People who tagged ' + ', '.join(tags) + ' also tagged: ')
print('\n'.join(rec_tags))