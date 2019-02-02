from sklearn import svm
import pickle
from time import time
import numpy as np
from lib import *


dictionary = pickle.load( open("dataset_dict.pickle", "r") )

features_list = ['Result', 
					'URL_Length',
					'Shortining_Service ',
					'having_At_Symbol',
					'double_slash_redirecting',
					'Prefix_Suffix',
					'having_Sub_Domain',
					'SSLfinal_State',
					'Domain_registeration_length',
					'Favicon',
					'port',
					'HTTPS_token',
					'Request_URL',
					'URL_of_Anchor' ,
					'Links_in_tags',
					'SFH',
					'Submitting_to_email',
					'Abnormal_URL',
					'Redirect',
					'on_mouseover',
					'RightClick',
					'popUpWidnow',
					'Iframe',
					'age_of_domain',
					'DNSRecord',
					'web_traffic',
					'Page_Rank',
					'Google_Index',
					'Links_pointing_to_page',
					'Statistical_report',
					'having_IP_Address']


vec = featureFormat(dictionary,features_list)
url_features, url_labels= targetFeatureSplit(vec)

from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)


clf = svm.SVC(gamma='scale',kernel='rbf',C=10000)
t0 = time()
clf.fit(feature_train, target_train) 
print "training time :",round(time()-t0, 3), "s" 

"""SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='scale', kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
"""

t1 = time()
pred = clf.predict(feature_test)
print "predicting time :",round(time()-t1, 3), "s"

print calculate_accuracy(pred,target_test)
