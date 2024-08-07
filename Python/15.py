try:
    f = open('Python\simple.txt','w')
    f.write("Test write to simple text!")
except IOError:
    print("ERROR : could not find file or read data")
finally:
    print("I am always going to work")