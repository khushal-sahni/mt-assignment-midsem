#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk 
from nltk.corpus import state_union                       # for training our tokenizer
from nltk.tokenize import PunktSentenceTokenizer          # tokenizer
nltk.download('state_union')                              # text for training 
nltk.download('averaged_perceptron_tagger')


train_text = state_union.raw('2006-GWBUsh.txt')
sample_text = "Ram is a good boy"                        # our text to be given 

custom_tokenizer = PunktSentenceTokenizer(train_text)    # tokenizer getting trained
tokenized = custom_tokenizer.tokenize(sample_text)       # tokenizing our text


def pos():
  try:
    for i in tokenized:
      words = nltk.word_tokenize(i)
      pos_tags = nltk.pos_tag(words)
      print(pos_tags)
  
  except Exception as e:
    print(str(e))


pos()


# In[10]:


# To find which pos means what 

nltk.download('tagsets')

nltk.help.upenn_tagset('NNP')
nltk.help.upenn_tagset('VBZ')
nltk.help.upenn_tagset('DT')
nltk.help.upenn_tagset('JJ')
nltk.help.upenn_tagset('NN')


# ### Syntax tree
# 

# In[11]:


from nltk.tokenize import word_tokenize

text1 = 'Ram is a good boy'

tokens = nltk.pos_tag(word_tokenize(text1))
tokens


# In[12]:


grammer_np= r'NP: {<DT>?<JJ>*<NN>}'

chunk_parser = nltk.RegexpParser(grammer_np)


# In[13]:


import warnings
warnings.filterwarnings('ignore')

chunk_result = chunk_parser.parse(tokens)
chunk_result


# In[14]:


# Tree('S', [('Ram', 'NNP'), ('is', 'VBZ'), Tree('NP', [('a', 'DT'), ('good', 'JJ'), ('boy', 'NN')])])


# In[ ]:




