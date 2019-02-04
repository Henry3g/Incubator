
"""
Created on Sat Feb  2 16:38:36 2019

@author: Henry
"""
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

linkedin = pd.read_csv('temp_datalab_records_linkedin_company.csv')
linkedin = np.array(linkedin)
date = linkedin[:,1]
company_name = linkedin[:,2]
num = len(company_name)
#followers_count = linkedin[:,3]
employees_on_platform = linkedin[:,4]
industry = linkedin[:,6]

Banking_Names = []
Banking_employees = []
Banking_date = []

for i in range(num):
    if industry[i] == 'Banking':
        Banking_Names.append(company_name[i])
        Banking_employees.append(employees_on_platform[i])
        Banking_date.append(date[i])
#print(len(Banking_Names))
num_banking = len(Banking_Names)

class company():
    def __init__(self, linkedin,name_str):
        self.name = name_str
        num_all = len(linkedin[:,2])
        self.as_of_date = []
        self.employees = []
        self.followers = []
        self.date_updated = []
        
        for i in range(num_all):
            if linkedin[i,2] == self.name:
                self.industry = linkedin[i,6]
                break
        for i in range(num_all):
            if linkedin[i,2] == self.name:
                self.as_of_date.append(linkedin[i,1])
                self.followers.append(linkedin[i,3])
                self.employees.append(linkedin[i,4])
                self.date_updated.append(linkedin[i,8])

def name_depuplication(bank_names, bank_employees):
    names_simplified = []
    employees_simplified = []
    d = {}
    for i in range(len(bank_names)-1,-1,-1):

        if bank_names[i] not in d:
            d[bank_names[i]] = 1
            names_simplified.append(bank_names[i])
            employees_simplified.append(bank_employees[i])
    names_simplified.reverse()
    employees_simplified.reverse()  
    return names_simplified, employees_simplified

Recently_banking_names,Recently_banking_employees = name_depuplication(Banking_Names, Banking_employees)

def find_order_max(List,order):
    list_max = np.max(List)
    index_max = List.index(list_max)
    list_order = [list_max]
    list_order_index = [index_max] 
    for j in range(order-1):
        a = 0
        for i in range(len(List)):
            if List[i] < list_order[j] and List[i] > a:
                a = List[i]
        list_order.append(a)
        b = List.index(a)
        list_order_index.append(b)
    return list_order, list_order_index
    
employees, index = find_order_max(Recently_banking_employees,3)

count_recent = Counter(Recently_banking_names)

print(Recently_banking_names[index[0]])
print(Recently_banking_names[index[1]])
print(Recently_banking_names[index[2]])

###############################################################################
#results: Bank of America(BOA), Banco Santander(BS),RBS

BOA = company(linkedin, 'Bank of America')
BS = company(linkedin, 'Banco Santander')
RBS= company(linkedin, 'RBS')

plt.figure(1)
plt.scatter(BOA.as_of_date, BOA.employees)
plt.show()
             
rate = []
for i in range(len(BOA.employees)-1) :
    rate.append(BOA.employees[i+1] - BOA.employees[i])
plt.figure(2)
BOA.as_of_date.pop()
plt.scatter(BOA.as_of_date, rate)
plt.show()
###############################################################################
index_list = []
for i in range(num_banking):
    if  Banking_Names[i] == 'Bank of America' :
        index_list.append(i)
Rate_BOA = []
x = []
date_share = []
for k in range(1,len(index_list)):
    #print(k)
    x.append(k)
    i = index_list[k]
    date_share.append(Banking_date[i])
    Temp_names,temp_employees = name_depuplication(Banking_Names[0:i], Banking_employees[0:i])
    BOA_num = Banking_employees[i]
    sum_num = np.sum(temp_employees)
    Rate_BOA.append(BOA_num/sum_num)

plt.figure(3)
plt.scatter(date_share, Rate_BOA)
plt.show()



