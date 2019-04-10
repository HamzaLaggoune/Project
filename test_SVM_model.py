from sklearn import svm
import pickle
from time import time
import numpy as np
from lib import *
import joblib 
from sklearn.model_selection import KFold
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

# from sklearn.model_selection import train_test_split
# feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)

# for key in keys :
# 	result = dictionary[key]['Result']
# 	if result == -1 :
# 		print key

# print dictionary['URL3454']


# clf = svm.SVC(gamma='scale',kernel='rbf',C=1000)
# clf.fit(feature_train, target_train)
# pred = clf.predict(feature_test)
# print "Accuracy score ",calculate_accuracy(pred,target_test) 
# joblib.dump(clf, 'for_extension.pk1', compress=9)

clf  = joblib.load('SVM_model.pk1')
cl2  = joblib.load('for_extension.pk1')
# test = [1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 0, 1, -1, 1, -1, -1, -1, 1, 1] returned 1 
#test = [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1]
test = [-1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 0, 0, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1]



new_test = np.array(test)

new_test = new_test.reshape(1,-1)
 
pred = clf.predict(new_test)
pred2 = cl2.predict(new_test) 
print pred
print pred2