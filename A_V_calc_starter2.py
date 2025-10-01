'''
TPRG 2131 Fall 202* Assignment 1
Sept 30, 2025
Cole L <cole.levi@durhamcollege>

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''


class calc:
    def __init__(self, input1, input2):
        self.input1 = 0
        self.input2 = 0
        
    def calc_Area_Square(self):
        return math.pow(self.input1, 2)
    
print("Enter Q/q to quit - select either will gracefull close the application and cancel the calculated view option, if set.\nEnter V/v to change the calculated view or D/d for default")

num1 = int(input("input #1 for square area calulator: "))
calculator = calc(num1, 0)
areaSquare = calc_Area_Square(num1, 0)
print(areaSquare)





