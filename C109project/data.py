import pandas as pd
import statistics
import csv

df =pd.read_csv("data.csv")
math = df["math score"].tolist()
read = df["reading score"].tolist()
write = df["writing score"].tolist()

math_mean = statistics.mean(math)
read_mean = statistics.mean(read)
write_mean = statistics.mean(write)

print ("The mean for math score is " + str(math_mean))
print ("The mean for reading score is " + str(read_mean))
print ("The mean for writing score is " + str(write_mean))

print ("The median for math score is " + str(statistics.median(math)))
print ("The median for reading score is " + str(statistics.median(read)))
print ("The median for writing score is " + str(statistics.median(write)))

print ("The mode for math score is " + str(statistics.mode(math)))
print ("The mode for reading score is " + str(statistics.mode(read)))
print ("The mode for writiing score is " + str(statistics.mode(write)))

math_std = statistics.stdev(math)
read_std = statistics.stdev(read)
write_std = statistics.stdev(write)

print ("The standard deviation for math score is " + str(math_std))
print ("The standard deviation for reading score is " + str(read_std))
print ("The standard deviation for writing score is " + str(write_std))

math_start,math_end = math_mean-math_std, math_mean+math_std
read_start,read_end = read_mean-read_std, read_mean+read_std
write_start, write_end =write_mean-write_std, write_mean+write_std

math_start_2,math_end_2 = math_mean-(2*math_std), math_mean+(2*math_std)
read_start_2,read_end_2 = read_mean-(2*read_std), read_mean+(2*read_std)
write_start_2, write_end_2 =write_mean-(2*write_std), write_mean+(2*write_std)

math_start_3,math_end_3 = math_mean-(3*math_std), math_mean+(3*math_std)
read_start_3,read_end_3 = read_mean-(3*read_std), read_mean+(3*read_std)
write_start_3, write_end_3 =write_mean-(3*write_std), write_mean+(3*write_std)

print(math_start,math_end)
print(read_start,read_end)
print(write_start, write_end) 

print(math_start_2,math_end_2)
print(read_start_2,read_end_2)
print(write_start_2, write_end_2)

print(math_start_3,math_end_3)
print(read_start_3,read_end_3)
print(write_start_3, write_end_3)

count_1=[]
for i in math:
    if(i>=math_start and i<=math_end):
        count_1.append(i)
print("The percentage in math test is "+str(len(count_1)/1000*100))

count_2=[]
for i in read:
    if(i>=read_start and i<=read_end):
        count_2.append(i)
print("The percentage in reading test is "+str(len(count_2)/1000*100))

count_3=[]
for i in write:
    if(i>=write_start and i<=write_end):
        count_3.append(i)
print("The percentage in writing test is "+str(len(count_3)/1000*100))

count_4=[]
for i in math:
    if(i>=math_start_2 and i<=math_end_2):
        count_4.append(i)
print("The percentage in math test is "+str(len(count_4)/1000*100))

count_5=[]
for i in read:
    if(i>=read_start_2 and i<=read_end_2):
        count_5.append(i)
print("The percentage in reading test is "+str(len(count_5)/1000*100))

count_6=[]
for i in write:
    if(i>=write_start_2 and i<=write_end_2):
        count_6.append(i)
print("The percentage in writing test is "+str(len(count_6)/1000*100))

count_7=[]
for i in math:
    if(i>=math_start_3 and i<=math_end_3):
        count_7.append(i)
print("The percentage in math test is "+str(len(count_7)/1000*100))

count_8=[]
for i in read:
    if(i>=read_start_3 and i<=read_end_3):
        count_8.append(i)
print("The percentage in reading test is "+str(len(count_8)/1000*100))

count_9=[]
for i in write:
    if(i>=write_start_3 and i<=write_end_3):
        count_9.append(i)
print("The percentage in writing test is "+str(len(count_9)/1000*100))