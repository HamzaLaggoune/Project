<h1> Machine learning techniques to identify Phishing URLs </h1>

The aim of this project is to use classification methods to identify phishing URLs. We will compare as many methods as possible in order to find the method that gives the highest accuracy.   

<b>Dataset : </b>

Dataset : https://archive.ics.uci.edu/ml/datasets/phishing+websites 

<b>Environment : </b>

We will be using Python 2.7.14 and Scikit-learn library.

<b>Running the code : </b>

Depending on the algorithm you want to use :  

<code>winpty python naives_bayes.py</code>

<code>winpty python decision_tree.py </code>

<code>winpty python SVM.py</code>

<code>winpty python KNN.py</code>

<h3> Performance evaluation  : </h3>

I'm using three metrics to evaluate the performance of the classifiers. 

<b>First : Accuracy </b>
  
Highest accuracy obtained so far equals 0.96 found it with SVM method. 

<b>Second : Recall </b>

Recall answers the following question : Assuming I know the URL tested is a phishing URL, what's the probability that the classifier identifies it as being a phishing URL ?

If you prefer : 

Recall = True positives / (True positives + False negatives)

<b>Third : Precision </b>

Precision answers the question : If my classifier predicts a URL as being a phishing URL, what's the probability that the URL is for real a phishing URL ?

Precision = True positives / (True positives + False positives) 
