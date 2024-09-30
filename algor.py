# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:21:42 2023

@author: Sai Krishna
"""

import pandas as pd
import timeit
import matplotlib.pyplot as plt

# Read the csv files into a dataframe
def read_into_df():
    file_names = [f'AN6007_Quiz{i:02}.csv' for i in range(1, 11)]
    aggregated_dataframes = {}
    #Read the csv files and load into a list
    for i, file_name in enumerate(file_names, start=1):
        df = pd.read_csv(file_name, encoding='utf-8')
        # Creating a new column containing Quiz No value
        df['Quiz No'] = i
        aggregated_dataframes[f'df_{i}'] = df
    # Merging the csv files into one dataframe
    merged_df = pd.concat(aggregated_dataframes.values(), ignore_index=True)
    return merged_df

def pandas_method():
    merged_df = read_into_df()
    merged_df['Score'] = pd.to_numeric(merged_df['Score'], errors='coerce')
    for index, row in merged_df.iterrows():
        if merged_df.loc[index,'Score'] >= 50:
            merged_df.loc[index,'Pass'] = 1
        else:
            merged_df.loc[index,'Pass'] = 0

    merged_df = merged_df.groupby(['Student ID', 'Quiz No']).agg({'Quiz No': 'count', 'Pass': 'sum', 'Score': 'mean'}).round(2)
    merged_df.columns = ['Attempts', 'Passed', 'Average Score']
    merged_df.reset_index()

    
    
    return merged_df

def dict_method():
    merged_df = read_into_df()
    results = {}  # {(student_id, quiz_number): [total_attempts, total_marks]}

   # Iterate through each row of the DataFrame
    for index, row in merged_df.iterrows():
       student_id = row['Student ID']
       quiz_number = row['Quiz No']
       marks_obtained = row['Score']

       # Create a unique key for each student and quiz combination
       key = (student_id, quiz_number)

       # Initialize or update the dictionary entry
       if key not in results:
           results[key] = {'total_attempts': 0, 'total_marks': 0}
       results[key]['total_attempts'] += 1
       results[key]['total_marks'] += marks_obtained

   # Calculate the average score and pass status
    final_results = {}
    for key, data in results.items():
        student_id, quiz_number = key
        total_attempts = data['total_attempts']
        total_marks = data['total_marks']
        average_score = total_marks / total_attempts
        passed = average_score > 50
        final_results[key] = {'total_attempts': total_attempts, 
                              'average_score': average_score, 
                              'passed': passed}
       
    return final_results

def time_calc(approach):
    SETUP_CODE = f'''from __main__ import {approach}'''
    TEST_CODE = f"{approach}()"
    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=5,number=10, globals=globals())
    return min(times)

# Choosing the best approach and printing it out
def best_approach():
    pandas_method = time_calc('pandas_method')
    dict_method = time_calc('dict_method')

    if pandas_method < dict_method:
        print(f"The best approach is the Pandas approach as the time taken: {pandas_method}, is lesser than time taken by Dictionary approach: {dict_method}")
        return 'pandas_method'
    else:
        print(f"The best approach is the Dictionary approach as the time taken: {dict_method}, is lesser than time taken by Pandas approach: {pandas_method}")
        return 'dict_method'

# Function to get the bar graph to see the time taken by the two methods
def graphical_representation():
    pandas_method = time_calc('pandas_method')
    dict_method = time_calc('dict_method')
    times = {'DataFrame': pandas_method, 'Dictionary': dict_method}
    # Plotting the time taken for the two methods in question
    plt.bar(times.keys(), times.values())
    plt.ylabel('Time (seconds)')
    plt.title('Time Consumed')
    plt.show()
    