Hey this is starting repos of ML with basic datasets<br>
Added Data Preprocess for the text and standard dataset set<br> 
Added The Regression Folder into the Repository<br>
From Today it will contain outputs with graphs<br>
 # Data Preprocessing
  The subject matter in Machine Learning is Data preprocessing<br>
  It is said that 80% is data preprocessing from the 100% of data science.<br>
  So I introduce You two types of data preprocessing in numbers<br>
  - ### Categorical Variable
    There are mainly 2 types
     - Ordinal
     - Numeral
   #### Ordinal
   - They are the one's which can be compared or ordered<br>
      Say for example we can order grade A to grade B i.e.<br>
      Garde A > Grade B or say marks in grade A is > grade B.<br>
      They are handled by simply mapping ranking
  #### Nominal
   - This is the one's which can not be compared or at same level<br>
     best example gender we cannot compare gender<br>
     They are to be one hot encoded i.e. say male => [1, 0]<br>
     Female => [0, 1] as per this [Male, Female] is the data<br>
     <br>
 # Regression
   In Statistics, Regression is defined as the method of<br>
   Obtaining co realtions or a mapping such that F(x) ~= Y<br>
   i.e. an estimate of the general population.<br>
   <br>
   But let's see or look it with a simple human prespective<br>
   Not the stastical one, Let's say you are in a party <br>
   And rather interesting game pops up i.e. you need to guess<br>
   The number of balls in jar without counting, opening or anyway<br>
   touching the jar (Closest number wins. And Winner get's a good gift.<br>
   You need that gift<br>
   <br>
   So you think of a way to see, And guess a number, Now the way <br>
   To do this is Take note of the previous guess and perform an estimate<br>
   with the mean of the people who are coming back with wrong answer<br>
   This is basically sandwiching towards the right direction and make a guess.<br>
   The activity you just perform let you as a winner Why? Cause of stats<br>
   This activity is estimation, and that is what we do in regression<br>
   Like the jar winning method, we do is take the guess from avilable information<br>
   Calculate or guess a number find how much far we are and then see the next person(number)<br>
   with the closest and guess again until you reach the lowest error or estimate<br>
  <br> 
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

# Image Classification of Cifar 100 dataset using CNN.

## What is CNN

CNN also known as Convolution Neural Network is a kind of Deep Neural network which is commonly used in analyzing visual data such as images. To explain in simple terms, it is a deep neural network where the first layer takes inputs and understand what each image pixel tries to account for using various filters, after that we flatten them and pass it to a Neural Network, then it goes to a classifier for predictions.

## The Dataset

The CIFAR-100 dataset consists of 60000 32x32 colour images in 100 classes. It has 100 classes containing 600 images each. There are 500 training images and 100 testing images per class.

## Training the Dataset

For a better training we need lots and lots of data but as we know we have very limited amount of data. So we have to randomize the dataset by applying different properties like Data Augmentation.
  * __Data augmentation__: It is a strategy that enables practitioners to significantly increase the diversity of data available for training models, without actually collecting new data. Data augmentation techniques such as cropping, padding, and horizontal flipping are commonly used to train large neural networks.

  * __Data Normalization__: In this technique we normalized the image tensors by subtracting the mean and dividing by the standard deviation of pixels across each channel. Normalizing the data prevents the pixel values from any one channel from disproportionately affecting the losses and gradients.

## Model

I have used a 12 layers CNN model where there are 6 residual layers and 5 convolutional block. Each convolutional block convert the number of channels from in_channels to out_channels. A kernel of size 3x3 is used. We also apply batch Normalization and Max Pooling(Explained Later). An activation function of ReLu is used for training our model.

## Hyperparameters

_Batch Size_: 400<br>
_Optimization Function_: Adam<br>
_Activation Function_: ReLu<br>
_Learning Rate Scheduler_: ONE CYCLE METHOD <br>
_Total No of Epochs_: (10+10+4+4+10)<br>
_Learning Rates_: (0.001,0.005,0.00001,0.0001,0.0001)<br>

## Conclusion

Using my model I achieved a maximum accuracy of nearly 73%. As the number of images are too less and limited the accuracy is difficult to push any further even after using many pretrained models like vgg and Resnet. 

## Defining the terms

 * __Max Pooling__: Max pooling is a sample-based discretization process. The objective is to down-sample an input representation (image, hidden-layer output matrix, etc.), reducing its dimensionality and allowing for assumptions to be made about features contained in the sub-regions binned. Max pooling is done by applying a max filter to (usually) non-overlapping subregions of the initial representation.

* __Batch Normalization__: Batch Normalization is a supervised learning technique that converts interlayer outputs into of a neural network into a standard format, called normalizing.  This effectively 'resets' the distribution of the output of the previous layer to be more efficiently processed by the subsequent layer.

* __ONE CYCLE METHOD__: It is a learning rate scheduler. In this method learning rate of each epochs increases in the beginning to reach a peak value of the learning rate at nearly 30% of the total number of epochs and then gradually decreases. 