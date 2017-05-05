#!/usr/bin/python
# -*- coding: utf-8 -*-


#imports
import re, sys


#to split a tag into words and return number of words
def wordlen(tag) :

    length = 0
    
    if(len(tag) == 0) :
        length = 0
    elif len(tag.split("_")) > 1 :
        length = len(tag.split("_"))
    else :
        try :
            wordlist = []
            word = ""
            for i in range(len(tag)) :
                word += tag[i]
                if(tag[i+1]) in "ABCDEFGHIJKLMNOPQRSTSUVWXYZ" and tag[i] in "abcdefghijklmnopqrstuvwxyz" :
                    wordlist.append(word)
                    word = ""
        except IndexError : 
            wordlist.append(word)
        finally :
            if len(wordlist) > 1 :
                length = len(wordlist)
            else :
                if(len(tag)>30) :
                    length = len(tag)
    return length

                   
#function to test for occurrence of Feature 1
def feature_1(tagstr) :

    
    flag = False
    tagset = tagstr.split("$^$")

    if len(tagset) > 0 :
        for i in tagset :
            if wordlen(i) > 2 :
                flag = True
                break
    return flag




#function to extract posts from file and search them
def search_file(data_list) :

    #testing for occurrences of feature 1
    count_f1 = 0
    num_posts = 0
    try:
        for iter in range(500) :
            num_posts += 1
            if(feature_1(data_list[iter])) :
                count_f1 += 1
    except IndexError :
        print("Not enough tweets")
        

    #returning total number of posts
    #and number of posts matching <feature>
    print("Number of posts: "+ str(num_posts-1))
    print("Occurrences: "+ str(count_f1))
    print("Percentage: ", str(float(count_f1*100.0/float(num_posts-1))))
    return num_posts-1, count_f1


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
    for i in range(1,11) :
        f = "twitags_" + str(i) + ".txt"
        print("\nFor data in "+f+" : ")
        data = extract_posts(f)
        posts, occ = search_file(data)
        tot_posts += int(posts)
        count_occ += int(occ)

    print("\nTotal compiled data shows: ")
    print("Total number of posts: "+str(tot_posts))
    print("Total occurrences: "+str(count_occ))
    print("Total percentage: "+str(float(count_occ*100.0/float(tot_posts))))
            
