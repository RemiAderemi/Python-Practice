#Write a Python program to count the number of characters (character frequency) in a string


def char_frequency(strl):
   
    dict={}
    for n in strl:
       # keys=dict.keys()
        if n in dict:
            dict[n]+=1
        else:
            dict[n]=1
    return dict