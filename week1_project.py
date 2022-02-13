
import math


try:
  
    inputNum = int(input("Enter an integer number: "))

    def perfect_square(num):

      n = int(math.sqrt(num))
      return n * n == num

    def  check_febonacci(inputNum):
 
      if inputNum < 0:

        print("Please Enter a valid Number")

      else:

        perfect_sqr1 = perfect_square(5 * inputNum * inputNum + 4)
        perfect_sqr2 = perfect_square(5 * inputNum * inputNum - 4)

        if (perfect_sqr1 or perfect_sqr2) == True:

          print(f"{inputNum} Is Febanacci Number" )

        if( perfect_sqr1 or perfect_sqr2) != True:

          print(f"{inputNum} Is Not Febanacci Number" )

    check_febonacci(inputNum)
    
except ValueError:

    print("Please input integer only...")  
    



