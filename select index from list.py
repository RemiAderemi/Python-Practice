#Write a Python program to print a specified list after removing the 0th, 4th and 5th element in a list

color=['red','green','white','black','pink', 'yellow']
color=[x for(i,x) in enumerate(color) if x not in (0,4,5)]
print(color)