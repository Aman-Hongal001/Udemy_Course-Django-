arraycheck=[1,1,2,3,1]
#to check the oder of 1 2 3 in any size list
def arrayCheck(num):
    for i in range(len(num)-2):
        # print(num[i])
        if num[i]==1 and num[i+1]==2 and num[i+2]==3:
            return True
    return False

if(arrayCheck(arraycheck)):
    print("True")

#2 selecting every 2 element of the string
def stringBits(str):
    print(str[::2])

stringBits('Heeololeo')

#3 the if first string should be present in second then return ture else false
def end_other(a,b):
    a = a.lower()
    b = b.lower()
    return a[-(len(b)):] == b or a == b[-(len(a)):]
    # or
    # return (b.endswith(a) or a.endswith())

print("Ends with : ",end_other('Hiabc','abc'))


#4 print the double character of string 
def doubleChar(mystring):
    result = ''
    for char in mystring:
        result += char*2
    return result
print(doubleChar('The'))

#5 dont add the teen numbers 13 14 etc
def no_teen_num(a,b,c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

def fix_teen(num):
    if num in [13,14,15,16,17,18,19]:
        return 0
    else:
        return num

print(no_teen_num(13,2,5))


#6  return even integer in given array

def count_evens(num):
    count = 0
    for i in num:
        if i%2 == 0:
            count += 1
    return count

list_num = [1,2,4,34,6,321,43,8,5]
print(count_evens(list_num))