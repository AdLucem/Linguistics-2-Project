#!/usr/bin/python
# -*- coding: utf-8 -*-


#imports
import re, sys


#function to test for occurrence of Feature 1
def feature_1(s) :
        
    return re.search("#",s) 

            
#driver
if __name__ == '__main__' :

    tot_posts = 0
    count_occ = 0
    for i in range(1,4400) :
        try :
            f = "Article247_" + str(i) + ".txt"
            article = open(f,"r+")
            data = article.read()
            tot_posts +=  1
            if(feature_1(data)) :
                print(data)
                count_occ += 1
            article.close()
                
        except FileNotFoundError :
            continue
        
    print("\nTotal compiled data shows: ")
    print("Total number of posts: "+str(tot_posts))
    print("Total occurrences: "+str(count_occ))
    print("Total percentage: "+str(float(count_occ*100.0/float(tot_posts))))
            
