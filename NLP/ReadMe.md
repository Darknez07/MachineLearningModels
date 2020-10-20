# NLP - Text Classification 

It is field of AI in which we try to process natural language (language we speak -hindi , english etc) and draw neccessay insights from it .Just like we do with it .
## Preprocessing 
 As computer doesnot understand natural language , we will encode it into numbers.
 We will do it with the help of tokenizer .The advance form of tokenizer is countervector which encode text into numbers and convert it  into vectors.
 
 Preprocessing also includes removing stopwords (e.g ['here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each']) and punctuation (e.g '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~').
 As both of them do not have importance in drawing insights from text .
 
 
 Further if we want to know which have importance or not we can use TFIDF (A short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.)  library of python .
 
 ## Classifier 
 There are many classifier . But the ones which are frequently used are-
 #### 1. Naive bayes classifier
Naive Bayes is a family of statistical algorithms we can make use of when doing text classification. One of the members of that family is Multinomial Naive Bayes (MNB). One of its main advantages is that you can get really good results when data available is not much (~ a couple of thousand tagged samples) and computational resources are scarce.

All you need to know is that Naive Bayes is based on Bayes’s Theorem, 

#### 2. SVM Classifier
Support Vector Machines (SVM) is just one out of many algorithms we can choose from when doing text classification. Like naive bayes, SVM doesn’t need much training data to start providing accurate results. Although it needs more computational resources than Naive Bayes, SVM can achieve more accurate results.
#### 3. Deep Learning
Deep learning is a set of algorithms and techniques inspired by how the human brain works. The two main deep learning architectures used in text classification are Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN).

* On the one hand, deep learning algorithms require much more training data than traditional machine learning algorithms, i.e. at least millions of tagged examples. On the other hand, traditional machine learning algorithms such as SVM and NB reach a certain threshold where adding more training data doesn’t improve their accuracy. In contrast, deep learning classifiers continue to get better the more data you feed them with.
* Deep learning algorithms such as Word2Vec or GloVe are also used in order to obtain better vector representations for words and improve the accuracy of classifiers trained with traditional machine learning algorithms(transfered learning)