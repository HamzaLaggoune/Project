from sklearn import svm
import pickle
from time import time
import numpy as np
from lib import *
import joblib 
from sklearn.model_selection import KFold

dictionary = pickle.load( open("dataset_dict.pickle", "r") )

# features_list = ['Result', 
# 				'having_IP_Address',
# 				'URL_Length',
# 				'Shortining_Service ',
# 				'having_At_Symbol',
# 				'double_slash_redirecting',
# 				'Prefix_Suffix',
# 				'having_Sub_Domain',
# 				'Domain_registeration_length',
#  				'Favicon',
#  				'HTTPS_token',
#  				'Request_URL',
#  				'URL_of_Anchor',
#  				'Links_in_tags',
#  				'SFH',
#  				'Submitting_to_email',
#  				'Abnormal_URL',
#  				'Iframe',
#  				'age_of_domain',
#  				'DNSRecord',
#  				'web_traffic',
#  				'Google_Index',
#  				'Statistical_report']

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


 

######### Create SVM classifier using K-FOLD algorithm to split the data 

#clf = svm.SVC(gamma='scale',kernel='rbf',C=1000)
# kf = KFold(n_splits=7)
# best_accuracy = 0

# for train_index, test_index in kf.split(url_features):
# 	X_train, Y_train, X_test, Y_test = split_data(train_index,test_index,url_features,url_labels)
# 	clf.fit(X_train, Y_train)
# 	pred = clf.predict(X_test)
# 	current_accuracy = calculate_accuracy(pred,Y_test)
# 	print current_accuracy
# 	#  best_accuracy ==0 means it's the first iteration so we export the model 
# 	if best_accuracy ==0 :
# 		best_accuracy = current_accuracy	
# 		joblib.dump(clf, 'SVM_model_improved.pk1', compress=9)
# 	# than if in this iteration the split allows our classifier to get a better performance than we update the exported version 
# 	elif best_accuracy < current_accuracy :
# 		best_accuracy = current_accuracy
# 		joblib.dump(clf, 'SVM_model_improved.pk1', compress=9)

# print "best accuracy : ",best_accuracy
   	
#from sklearn.feature_selection import SelectKBest, chi2,f_classif
#selector = SelectKBest(score_func=f_classif, k=25)
#selector.fit_transform(url_features, url_labels)
#print("selected index:",selector.get_support(True))
#X_train_new = selector.transform(url_features)

from sklearn.model_selection import train_test_split
#feature_train, feature_test, target_train, target_test = train_test_split(X_train_new, url_labels, test_size=0.1, random_state=42)
feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)

clf = svm.SVC(gamma='scale',kernel='rbf',C=100)
clf.fit(feature_train, target_train) 
pred = clf.predict(feature_test)
print "Accuracy score ",calculate_accuracy(pred,target_test)
print "Recall score : ",calculate_recall(target_test, pred)
print "Precision score : ",calculate_precision(target_test, pred)



# clf = svm.SVC(gamma='scale',kernel='rbf',C=1000)
# kf = KFold(n_splits=7)
# best_accuracy = 0

# for train_index, test_index in kf.split(X_train_new):
# 	X_train, Y_train, X_test, Y_test = split_data(train_index,test_index,X_train_new,url_labels)
# 	clf.fit(X_train, Y_train)
# 	pred = clf.predict(X_test)
# 	current_accuracy = calculate_accuracy(pred,Y_test)
# 	print current_accuracy
# 	#  best_accuracy ==0 means it's the first iteration so we export the model 
# 	if best_accuracy ==0 :
# 		best_accuracy = current_accuracy	
# 		joblib.dump(clf, 'SVM_model_improved_second.pk1', compress=9)
# 	# than if in this iteration the split allows our classifier to get a better performance than we update the exported version 
# 	elif best_accuracy < current_accuracy :
# 		best_accuracy = current_accuracy
# 		joblib.dump(clf, 'SVM_model_improved_second.pk1', compress=9)

# print "best accuracy : ",best_accuracy

# loading the model since it's ready. SVM model has been created with lines 49-53 
#clf  = joblib.load('SVM_model_improved.pk1')

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
# # t1 = time()
# pred = clf.predict(feature_test)

 
# print "Recall score : ",calculate_recall(target_test, pred)


# print "Precision score : ",calculate_precision(target_test, pred)


# #print "predicting time :",round(time()-t1, 3), "s"

# print "Accuracy score ",calculate_accuracy(pred,target_test)
