import sys
import pickle
import numpy as np
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

def featureFormat( dictionary, features, remove_NaN=True, remove_all_zeroes=True, remove_any_zeroes=False, sort_keys = False):
    

    return_list = []

    # Key order - first branch is for Python 3 compatibility on mini-projects,
    # second branch is for compatibility on final project.
    if isinstance(sort_keys, str):
        import pickle
        keys = pickle.load(open(sort_keys, "rb"))
    elif sort_keys:
        keys = sorted(dictionary.keys())
    else:
        keys = dictionary.keys()

    for key in keys:
        tmp_list = []
        for feature in features:
            try:
                dictionary[key][feature]
            except KeyError:
                print "error: key ", feature, " not present"
                return
            value = dictionary[key][feature]
            if value=="NaN" and remove_NaN:
                value = 0
            tmp_list.append( int(value) )

        # Logic for deciding whether or not to add the data point.
        append = True
        # exclude 'Result' class as criteria.
        if features[0] == 'Result':
            test_list = tmp_list[1:]
        else:
            test_list = tmp_list
        ### if all features are zero and you want to remove
        ### data points that are all zero, do that here
        if remove_all_zeroes:
            append = False
            for item in test_list:
                if item != 0 and item != "NaN":
                    append = True
                    break
        ### if any features for a given data point are zero
        ### and you want to remove data points with any zeroes,
        ### handle that here
        if remove_any_zeroes:
            if 0 in test_list or "NaN" in test_list:
                append = False
        ### Append the data point if flagged for addition.
        if append:
            return_list.append( np.array(tmp_list) )

    return np.array(return_list)

def targetFeatureSplit( data ):
	features = []
	labels = [] 

	for line in data :
		features.append( line[1:] )
		labels.append( line[0] )

	return features, labels 

def calculate_accuracy(pred,target_test) :
	from sklearn.metrics import accuracy_score
	accuracy = accuracy_score(pred, target_test)
	return accuracy

def calculate_recall(target_test,pred) :
	return recall_score(target_test, pred)


def calculate_precision(target_test,pred) : 

	return precision_score(target_test, pred, average='macro') 

def split_data(train_index,test_index,X,Y) :
		X_train = [] 
		Y_train = []
		X_test  = []
		Y_test  = []
		
		# create training data
		for i in train_index :
			X_train.append(X[i])
			Y_train.append(Y[i])
			
		for j in test_index :
			X_test.append(X[j])
			Y_test.append(Y[j])
		

		return X_train, Y_train,X_test, Y_test