1. 
2. # -*- coding: utf-8 -*-
3. """
4.
5. 
6. """
7.
8. from nltk.corpus import wordnet
9. from gensim.models import KeyedVectors
10.
11. def get_related_word(starting_words):
12. related_word_list = []
13. #Word embeddings in gensim format
14. gloveModel = KeyedVectors.load_word2vec_format('../gensim_glove.6b.50d.txt')
15.
16. for starting_word in starting_words:
17. related_words = get_wordnet_synsets(starting_word)
18. similar_word_embeddings = gloveModel.similar_by_word(starting_word, 5)
19. similar_words = [w_embedding for w_embedding,similarity in similar_word_embeddi
ngs]
20. print('similar words: ', similar_words)
21. related_word_list = related_word_list + related_words + similar_words
22.
23. return set(related_word_list)
24.
25.
26. def get_wordnet_synsets(word):
27. syns = wordnet.synsets(word)
28. synsets = [synword.lemmas()[0].name() for synword in syns]
29. return synsets
30.
31. #Used for converting from glove format to gensim which is used in this case
32. def convert_glove_to_gensim(src_glove, dst_gensim):
33. from gensim.scripts.glove2word2vec import glove2word2vec
34. glove2word2vec(src_glove, dst_gensim)
35.
36. if __name__ == '__main__':
37. cs_words = ['computer', 'hash', 'array', 'programming', 'number', 'float', 'double'
, 'integer', 'encrypt',
38. 'password', 'user', 'machine', 'learning', 'network']
39.
40. related_words = get_related_word(cs_words)
41. print(related_words)
14