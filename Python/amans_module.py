

# def func_in_module():
#     print("I am inside aman's module")

def func():
    print("func() in amans_module.py")

print("TOP level amans_module.py")

if __name__ == '__main__':
    print("amans_module.py is being run directly")
else:
    print("Amans_module.py is been imported")