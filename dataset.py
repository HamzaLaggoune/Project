import pickle
from dataset_vector import return_dataset 

# dataset_dict = {URL1:{'having_IP_Address':1,
# 					'URL_Length':1,
# 					'Shortining_Service ':1,
# 					'having_At_Symbol' : 1,
# 					'double_slash_redirecting':1,
# 					'Prefix_Suffix' : 1,
# 					'having_Sub_Domain' : 1,
# 					'SSLfinal_State' : 1,
# 					'Domain_registeration_length' :1,
# 					'Favicon' : 1,
# 					'port' : 1,
# 					'HTTPS_token':1,
# 					'Request_URL' :1,
# 					'URL_of_Anchor' :1,
# 					'Links_in_tags' :1,
# 					'SFH' : 1,
# 					'Submitting_to_email':1,
# 					'Abnormal_URL' :1,
# 					'Redirect':1,
# 					'on_mouseover' :1,
# 					'RightClick':1,
# 					'popUpWidnow' :1,
# 					'Iframe' :1,
# 					'age_of_domain':1,
# 					'DNSRecord':1,
# 					'web_traffic':1,
# 					'Page_Rank':1,
# 					'Google_Index':1,
# 					'Links_pointing_to_page':1,
# 					'Statistical_report':1,
# 					'Result':1},
# 					URL2:'url_attributes',URL3:'url_attributes'}

dataset_dict = {}
# return_dataset() function 'which you can fin in dataset_vector.py' reads 'dataset.txt' file and converts it from 'lines of strings' to a list of vectors 
dataset = return_dataset()
# each line of dataset contains values of attributes for a URL 
i = 0 
for line in dataset :
	url_attributes = {'having_IP_Address':line[0],
					'URL_Length':line[1],
					'Shortining_Service ':line[2],
					'having_At_Symbol' : line[3],
					'double_slash_redirecting':line[4],
					'Prefix_Suffix' : line[5],
					'having_Sub_Domain' : line[6],
					'SSLfinal_State' : line[7],
					'Domain_registeration_length' :line[8],
					'Favicon' : line[9],
					'port' : line[10],
					'HTTPS_token':line[11],
					'Request_URL' :line[12],
					'URL_of_Anchor' :line[13],
					'Links_in_tags' :line[14],
					'SFH' : line[15],
					'Submitting_to_email':line[16],
					'Abnormal_URL' :line[17],
					'Redirect':line[18],
					'on_mouseover' :line[19],
					'RightClick':line[20],
					'popUpWidnow' :line[21],
					'Iframe' :line[22],
					'age_of_domain':line[23],
					'DNSRecord':line[24],
					'web_traffic':line[25],
					'Page_Rank':line[26],
					'Google_Index':line[27],
					'Links_pointing_to_page':line[28],
					'Statistical_report':line[29],
					'Result':line[30]}
	dataset_dict['URL'+str(i)] = url_attributes
	i +=1 




#creating pickle file 
dataset_pickle_out = open("dataset_dict.pickle","w")
pickle.dump(dataset_dict, dataset_pickle_out)
dataset_pickle_out.close()