import os
import csv
import sys


def create_object_file():
    object_list = []
    text = open("object.csv").read()
    #print (text)
    object_list.append([])
    row = 0
    for i in text:
        if i == "\n":
            object_list.append([])
            row += 1
        else:
            object_list[row].append(i)
    return object_list


def print_object_file(object_list, a_start_row , b_end_row):
    for row in object_list[a_start_row:b_end_row]:
        print("".join(row))

object_list=create_object_file()
print_object_file(object_list,1,11) #tree
print_object_file(object_list,12,16) # mage
print_object_file(object_list,17,22) #bush
print_object_file(object_list,23,31) #house
print_object_file(object_list,32,35) #magic_staff
#print_object_file(object_list,36,39) #sword
