#Done by M Harish AIML-A 231501058
try:
    num = int(input())
    if 1 <= num <= 100:
        print("Valid input.")
        
    else:
        print("Error: Number out of allowed range")
except ValueError:
    print("Error: invalid literal for int()")


try:
    a=int(input())
    b=int(input())
    print(a/b)
    
except ValueError:
    print("Error: Non-numeric input provided.")
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")


try:
    num = int(input())
    if 1 <= num <= 100:
        print("Valid input.")
        
    else:
        print("Error: Number out of allowed range")
except ValueError:
    print("Error: invalid literal for int()")


try:
    a=int(input())
    if a>=0:
        print("The square root of %.1f is %.2f"%(float(a),float(a**0.5)))
    else:
        print("Error: Cannot calculate the square root of a negative number.")
except:
    print("Error could not convert string to float")


try:
    n=int(input())
    if n>=1:
        
        print("You are",n,"years old.")
    else:
        print("Error: Please enter a valid age.")
except:
    print("Error: Please enter a valid age.")
#Done by M Harish AIML-A 231501058