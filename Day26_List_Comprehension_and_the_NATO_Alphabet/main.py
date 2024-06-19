# list comprehension
# new_list = [item_operation for item in list]

number = [1,2,3]
new = [n*2 for n in number]

# conditional comprehension
# new_list = [item_operation for item in list if test]

c_num = [n*n for n in number if n % 2 == 0]

# dictionary comprehension
# new_dict = {new_key:new_value for item in list}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c * 9/5) +32  for (day,temp_c) in weather_c.items()}

print(weather_f)


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)
    print()

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print()

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row["score"])
    print()

    #Access row.student or row.score
    pass