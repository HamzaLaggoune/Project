import random
import joblib 
import pickle
import random
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from lib import *
from sklearn.model_selection import train_test_split
dictionary = pickle.load( open("dataset_dict.pickle", "r") )

class SBS:

  #list of all features initialy 
  features_vector = [1] * 31
  my_current_features = features_vector
  #contains all features initialy 
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
  
  
	

  def print_features(self) :
  	print self.features_list

  def print_features_vector(self) :
  	print self.features_vector

  def random_feature_position(self) : 
  	return (random.randint(1,30))

  def test(self) : 
  	print self.features_list[30]

  def update_features_vector(self,position,signe) :
  	if signe == -1 :
  		self.features_vector[position] = 0
  	else :
  		self.features_vector[position] = 1 


  def build_features_list(self,feature):
  	j=0
  	temp_features_list = []
  	
  	for i in range(0,len(self.features_vector)-1) :
  		if self.features_vector[i] !=0 :
  			temp_features_list.append(self.features_list[i])
  		i+=1
  	return temp_features_list

  def create_evaluate_model(self,feature_train,target_train,feature_test,target_test) :
 	clf = svm.SVC(gamma='scale',kernel='rbf',C=10)
	clf.fit(feature_train, target_train) 
	
	#************************************
	#clf = tree.DecisionTreeClassifier(min_samples_split = 40)
	#clf.fit(feature_train, target_train)
	#pred = clf.predict(feature_test)

	#***************************************

	# clf = GaussianNB()
	# clf.fit(feature_train, target_train)
	# pred = clf.predict(feature_test)

	#print "training time :",round(time()-t0, 3), "s" 
	#joblib.dump(clf, 'SVM_by_SBS.pk1', compress=9)
	pred = clf.predict(feature_test)
  	
  	return calculate_precision(target_test, pred)


  def Sbs_Method(self) :
  	
  	vec = featureFormat(dictionary,self.features_list) 
	url_features, url_labels= targetFeatureSplit(vec)
	feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)
	max_accuracy = self.create_evaluate_model(feature_train,target_train,feature_test,target_test)	
	print "this is first : "+ str(max_accuracy)

	for i in range(1,50) :

  		#feature is chosen randomly 
		feature = self.random_feature_position()
		
		# -1 means remove the feature at position = feature while 1 means add it 
  		self.update_features_vector(feature,-1)
  		 	
  		list_attributes = self.build_features_list(feature)
 		vec = featureFormat(dictionary,list_attributes) 
		url_features, url_labels= targetFeatureSplit(vec)
		feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)
		new_accuracy = self.create_evaluate_model(feature_train,target_train,feature_test,target_test)
		
		if new_accuracy >= max_accuracy :
			max_accuracy = new_accuracy
		else :
			self.update_features_vector(feature,+1)	

	print self.features_vector
	print max_accuracy

  def randomSolution(self,features) :
	position = self.random_feature_position()
	
	if features[position] == 0 :
		features[position] =1
	else :
		features[position] =0


 	return features


  def neighbour(self,features,pos) :
	if features[pos] == 1 :
		features[pos] =0
	else :
		features[pos] =1
	
	return features

  def best_neighbour(self,pbest) :


			for i in range(8) :
				temp_features = self.my_current_features
				temp_features = self.neighbour(temp_features,i)

				list_attributes = self.build_features_list(temp_features)

				vec = featureFormat(dictionary,list_attributes) 
				url_features, url_labels= targetFeatureSplit(vec)
				
				feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)
				new_accuracy = self.create_evaluate_model(feature_train,target_train,feature_test,target_test)
				
				if(new_accuracy >= pbest) :
					self.my_current_features = temp_features
					pbest = new_accuracy
		

			return pbest





  def Sls_method(self) : 
  	Wp = 0.61 
  	attempsNotImprouving = 5
  

 	vec = featureFormat(dictionary,self.features_list) 
	url_features, url_labels= targetFeatureSplit(vec)
	feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)
	max_accuracy = self.create_evaluate_model(feature_train,target_train,feature_test,target_test)	
	pbest = max_accuracy
	print "this is first : "+ str(max_accuracy)
	print self.my_current_features
	# retreive value of vector
	current_features = self.features_vector
	print "*********************************"
	

	while(attempsNotImprouving != 0) :
		# Generate a random number 
		temp = random.uniform(0, 1)
	
		if(temp < Wp) :
			#Just any random solution
			self.my_current_features = self.randomSolution(self.my_current_features)
			list_attributes = self.build_features_list(current_features)
			vec = featureFormat(dictionary,list_attributes) 
			url_features, url_labels= targetFeatureSplit(vec)
			feature_train, feature_test, target_train, target_test = train_test_split(url_features, url_labels, test_size=0.1, random_state=42)
			new_accuracy = self.create_evaluate_model(feature_train,target_train,feature_test,target_test)
			#print new_accuracy

			if (new_accuracy < max_accuracy) :
				max_accuracy = new_accuracy
				attempsNotImprouving -=1
			else : 
				max_accuracy = new_accuracy

				
					

		else :
			#it has to be an improuved solution
			
			neighbour_accuracy = self.best_neighbour(pbest)
			if(neighbour_accuracy <= pbest): 
				attempsNotImprouving -=1
			else :
				attempsNotImprouving = 0
				pbest = neighbour_accuracy
						
	print (self.my_current_features)
	print pbest			






# Sbs = SBS()
# i = Sbs.random_feature_position()
# Sbs.Sbs_Method()

