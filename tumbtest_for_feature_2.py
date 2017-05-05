#!/usr/bin/python
# -*- coding: utf-8 -*-


#imports
import re, sys


#function to test for occurrence of Feature 2
def feature_1(tagstr) :

    flag = False
    tagset = tagstr.split("$^$")

    if len(tagset) > 0 :
        for i in tagset :
            if len(i.split()) > 2 :
                flag = True
                break
    return flag
    

#function to extract posts from file and search them
def search_file(data_list) :

    #testing for occurrences of feature 1
    count_f1 = 0
    for data in data_list :
        if(feature_1(data)) :
            count_f1 += 1

    #returning total number of posts
    #and number of posts matching <feature>
    print("Number of posts: "+ str(len(data_list)-1))
    print("Occurrences: "+ str(count_f1))
    print("Percentage: ", str(float(count_f1*100.0/float(len(data_list)-1))))
    return len(data_list)-1, count_f1


#function to extract posts from file
def extract_posts(scrape_file):
    L = []
    f = open(scrape_file)
    data = f.read().split("@#@")
    f.close()
    return data

            
#driver
if __name__ == '__main__' :

    tot_posts = 0
    count_occ = 0

    for i in range(1, 11) :
        f = "tags" + str(i) + ".txt"
        print("\nFor data in "+f+" : ")
        data = extract_posts(f)
        posts, occ = search_file(data)
        tot_posts += int(posts)
        count_occ += int(occ)

    print("\nTotal compiled data shows: ")
    print("Total number of posts: "+str(tot_posts))
    print("Total occurrences: "+str(count_occ))
    print("Total percentage: "+str(float(count_occ*100.0/float(tot_posts))))

