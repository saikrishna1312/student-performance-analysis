# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:48:50 2023

@author: Sai Krishna
"""
"""

This final.py script compares the algorithm efficiency and shows the output of best fit algorithm.


               Class : MSc. Business Analytics - Group B
               Name :  Sai Krishna Swamy WUdali
               Matriculation Number : G2301302E
               Email : SAIKRISH004@e.ntu.edu.sg
               Video link : https://drive.google.com/file/d/11Kntqt0_wLRUC0RogmM1pmOPG6VKrIgW/view?usp=sharing
               Password :              
"""

from algor import *

def main():
    try:
        final_approach = best_approach()
        if final_approach == 'pandas_method':
            tabular_dataframe()
        else:
            tabular_dict()

    except Exception as e:
        print(f"An error occurred: {e}")
    graphical_representation()

def tabular_dict():
    try:
        results_df = dict_method()
        print("_" * 81)
        print("| {:^10} | {:^10} | {:^10} | {:^20} | {:^15} |".format("Std ID", "Quiz no", "attempts",
                                                                      "passed",
                                                                      "average score"))
        print("_" * 81)

        student_ids = list(results_df.keys())
        student_ids.sort()

        for student_id, quiz_number in student_ids:
            data = results_df[student_id, quiz_number]
            print("| {:^10} | {:^10} | {:^10} | {:^20} | {:^15} |".format(
                student_id,
                quiz_number,
                data['total_attempts'],
                data['passed'],
                data['average_score']
            ))

        print("_" * 81)

    except Exception as e:
        print(f"An error occurred: {e}")

def tabular_dataframe():
    try:
        results_df = pandas_method()
        print("_" * 81)
        print("| {:^10} | {:^10} | {:^10} | {:^20} | {:^15} |".format("Std ID", "Quiz no", "attempts",
                                                                      "Passed",
                                                                      "average score"))
        print("_" * 81)

        for index, row in results_df.iterrows():
            print("| {:^10} | {:^10} | {:^10} | {:^20} | {:^15} |".format(
                int(row['Student ID']),
                int(row['Quiz No']),
                row['total_attempts'],
                int(row['Passed']),
                row['average_score']
            ))

        print("_" * 81)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()