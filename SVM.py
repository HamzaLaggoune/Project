from sklearn import svm
import pickle
from time import time
import numpy as np
from lib import *
import joblib 


dictionary = pickle.load( open("dataset_dict.pickle", "r") )

features_list = ['Result', 
				'having_IP_Address',
				'URL_Length',
				'Shortining_Service ',
				'having_At_Symbol',
				'double_slash_redirecting',
				'Prefix_Suffix',
				'having_Sub_Domain',
				'Domain_registeration_length',
 				'Favicon',
 				'HTTPS_token',
 				'Request_URL',
 				'URL_of_Anchor',
 				'Links_in_tags',
 				'SFH',
 				'Submitting_to_email',
 				'Abnormal_URL',
 				'Iframe',
 				'age_of_domain',
 				'DNSRecord',
 				'web_traffic',
 				'Google_Index',
 				'Statistical_report']

 

vec = featureFormat(dictionary,features_list) 
 
url_features, url_labels= targetFeatureSplit(vec)

from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)

# loading the model since it's ready. SVM model has been created with lines 49-53 
clf  = joblib.load('SVM_model.pk1')

######### remove the comments in the following lines to create, train and export the SVM model
"""
clf = svm.SVC(gamma='scale',kernel='rbf',C=1000)
t0 = time()
clf.fit(feature_train, target_train) 
print "training time :",round(time()-t0, 3), "s" 
joblib.dump(clf, 'SVM_model.pk1', compress=9)
"""
########## END 

"""SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='scale', kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
"""
t1 = time()
pred = clf.predict(feature_test)

 
print "Recall score : ",calculate_recall(target_test, pred)


print "Precision score : ",calculate_precision(target_test, pred)


print "predicting time :",round(time()-t1, 3), "s"

print "Accuracy score ",calculate_accuracy(pred,target_test)
