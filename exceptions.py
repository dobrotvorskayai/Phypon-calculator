

#def test(lst):
    #a = str(lst[0])
    #b = str(lst[1])

    #if a.isdigit() and b.isdigit():
    #    return True
    #print("Error: incorrect data")
    ## return False
    #lst = []
    #x = int(input("Enter first number to create first complex number: "))
    #y = int(input("Enter second numbers to create first complex number: "))
    #z = int(input("Enter two numbers to create second complex number: "))
    #w = int(input("Enter second numbers to create second complex number: "))
    #a = lst.append(complex(x, y))
    #b = lst.append(complex(z, w))
    #test_nums(lst)

def div_by_zero(lst):
    if lst[1] == 0:
        print("Error: division by zero!")
        return False
    return lst

#def isfloat(lst):
 #   
  #      try: 
   #         float(lst[i])
    #    except ValueError: 
     #       print("Error: incorrect data")
      #      return False
       # return True

def test(x):
    while True:
        try:
            x = float
            return x
        except ValueError:
             print("Error: : incorrect data")
             return False
          
