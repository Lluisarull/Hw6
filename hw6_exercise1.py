###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

class Patient:
    def __init__(self, name:str, symptoms:list):
        self.name = name
        self.symptoms = symptoms

patient_1 = Patient('Joan',['febre','tos'])
patient_2 = Patient('Nuria',['congestió','gastroenteritis'])
patient_3 = Patient('Marti',['fever', 'cough', 'ansomia'])

print(patient_1.name)
print(patient_2.name)
print(patient_3.name)
print(patient_1.symptoms)
print(patient_2.symptoms)
print(patient_3.symptoms)

#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.


def add_test(self, test_name:str, test_result:bool):
    self.test_name = test_name
    self.test_result = test_result


#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']


def has_covid(self):
    try:
        if self.test_name == "covid":
            prob = 0.99 if self.test_result == True else 0.01
    except AttributeError:
        prob = 0.05 
        for i in range(len(self.symptoms)):
            covid_symptoms = ['fever', 'cough', 'anosmia']
            if self.symptoms[i] in covid_symptoms:
                    prob += 0.1
    return prob


