# -*- coding: utf-8 -*-
"""To_do_list.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wTQ07oq8KU2sauufe-i7G1W8j5pShrEh
"""

To_do_list = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5']
print('My To-Do List from Monday to Friday:\n')
for Days in range(len(To_do_list)):
  if Days == 0 :
    Day1='Learn python on w3school'
    print(f'Monday:, {Day1}')

  if Days == 1 :
    Day2 = 'Attend Python class on Google meet'
    print(f'Tuesday: {Day2}')

  if Days == 2 :
    Day3 = 'Practise what was taught in Python Class'
    Wed = Day3 + ' and ' + Day2
    print(f'Wednessday: {Wed}')

  if Days == 3 :
    Thur = Day3 + ' and ' + Day2
    print(f'Thursday: {Thur}')

  if Days == 4 :
    print('Friday: Attend to Quiz on my Python programming platform')