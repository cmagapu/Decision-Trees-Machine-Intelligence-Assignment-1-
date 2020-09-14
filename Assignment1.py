'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
    col = df.keys()[-1]  
    entropy = 0
    values = df[col].unique()
    for value in values:
        fraction = df[col].value_counts()[value]/len(df[col])
        entropy += -fraction*np.log2(fraction)
    return entropy



'''Return entropy of the attribute provided as parameter'''
	#input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
	#output:int/float/double/large
def get_entropy_of_attribute(df,attribute):
    entropy_of_attribute = 0  
    target = df.keys()[-1]
   
    new_df = df[[attribute,target]]
    new_df.groupby(attribute)
    a = dict(new_df[attribute].value_counts())
   
    for i in a:
            x = new_df.loc[df[attribute]==i]
            sum = 0
            e=0
            categories = dict(x[target].value_counts())            
            for j in categories:              
                sum+=categories.get(j)
                if categories.get(j) == 0 or categories.get(j)==len(x[target]):
                    e = 0
                else:
                    fraction = categories.get(j)/len(x[target])
                    #print(fraction)
                    e += -fraction*np.log2(fraction)
            entropy_of_attribute += sum/len(df)*e
    return entropy_of_attribute



'''Return Information Gain of the attribute provided as parameter'''
	#input:int/float/double/large,int/float/double/large
	#output:int/float/double/large
def get_information_gain(df,attribute):
    information_gain = 0
    e = get_entropy_of_dataset(df)
    i = get_entropy_of_attribute(df,attribute)
    information_gain = e - i
    return information_gain

''' Returns Attribute with highest info gain'''  
	#input: pandas_dataframe
	#output: ({dict},'str')     
def get_selected_attribute(df):
    information_gains={}
    selected_column=''
    target = df.keys()[-1]
    '''Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected
    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')'''
    for i in df.columns:
        if i!=target:
            gain = get_information_gain(df,i)
            #print(gain)
            information_gains[i]=gain
    #print(information_gains)
    selected_column = max(information_gains, key=lambda x:information_gains[x])
    #print(selected_column)
    return (information_gains,selected_column)






'''
------- TEST CASES --------
How to run sample test cases ?

Simply run the file DT_SampleTestCase.py
Follow convention and do not change any file / function names

'''