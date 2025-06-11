print ('welcome to number teller!')
number = int(input("please enter a number between 1 and 9 "))
if number == 1: 
    print("you have entered Number one ") 
elif number == 2: 
    print("you have entered Number two") 
elif number == 3:
    print("you have entered Number three") 
elif number == 4:
    print("you have entered Number four ")
elif number == 5: 
    print("you have entered Number five") 
elif number == 6:
    print("you have entered Number six") 
elif number == 7:
    print("you have entered Number seven")
elif number == 8:
    print("you have entered Number eight") 
elif number == 9:
    print("you have entered Number nine")
else:
    print("invalid,please enter a number between 1 and 9")
    #TODO
print("assigned grades to students marks")
number = int(input("Enter your marks (0 to 100): "))
# Check if the marks are within valid range
if number < 0 or number > 100:
    print("Invalid input! Marks should be between 0 and 100.")
else:
    # Grade classification using if statements
    if number >= 90:
        print("Grade: A")
    elif number>= 80:
        print("Grade: B")
    elif number >= 70:
        print("Grade: C")
    elif number >= 60:
        print("Grade: D")
    elif number >= 50:
        print("Grade: E")
    else:
        print("Grade: F (Fail)")
