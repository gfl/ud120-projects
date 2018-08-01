#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "Enron size: ", len(enron_data)
s = 0
for k,v in enron_data.items():
    s = s + len(v)
avg_num_features = s/len(enron_data)
print "AVG num features: ", avg_num_features

pois = {k: v for k, v in enron_data.iteritems() if v[0]["poi"] = True}
print "Number of POIs: ", len(pois)

import re

names = [ line for line in open("../final_project/poi_names.txt", "r") if re.match("\(.\)(.*)", line)]
print "Total names: ", len(names)

print "James Prentice stock: ", enron_data['PRENTICE JAMES']['total_stock_value']

num_with_salary = len({k:v for k,v in enron_data.items() if v['salary'] != 'NaN'})
print "Number of people with a qualified salary: ", num_with_salary
num_with_email = len({k:v for k,v in enron_data.items() if v['email_address'] != 'NaN'})
print "Number of people with an email address: ", num_with_email

percentage_people_without_total_payments = len({k:v for k,v in enron_data.items() if v['total_payments'] == 'NaN'})*100/len(enron_data)
print "Percentage of people that have 'NaN' for their total paiments: ", percentage_people_without_total_payments

pois = {k:v for k,v in enron_data.items() if v['poi'] == True}
pois_without_total_payments = {k:v for k,v in pois.items() if v['total_payments'] == 'NaN'}
