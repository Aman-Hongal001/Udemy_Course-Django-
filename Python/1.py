#string
s = 'django'
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])
# reverse
print(s[::-1])

#List
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print("\n\n List Starts here\n",l)


# to make it unique by using set 
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
s= set(mylist)
print("\n",s)

#dictionary
#need to grap hello from all
d1 = {'simple_key':'hello'}
print("\nDictionary here\n",d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])


#formating
age = 4
name = "Sammy"
print("hello my dog's name is {a} and he is {b} years old.".format(a=name,b=age))