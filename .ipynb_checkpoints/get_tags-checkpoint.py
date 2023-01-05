import pickle
import json


#load list_of_docs
with open('./list_of_docs.pkl', 'rb') as f:
    list_of_docs = pickle.load(f)
    
test  = list_of_docs

article_tags = []
    
for i, doc in enumerate(test):
    # print('index', i)
    article_tags.extend(test[i]['article_tags'])
    # print()
    
print(len(test))
                       
# article_tags = list(set(article_tags))
# article_tags = list(filter(None, article_tags))
# article_tags = sorted(article_tags)
# with open('article_tags.json', 'w') as f:
#     json.dump(article_tags, f)
                       