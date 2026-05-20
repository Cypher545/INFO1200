#Name: Ian Julander
#Class: INFO 1200
#Section: X01
#Professor: AlSobeh
#Date: 05/20/2026
#Assignment #: M02 Project
#By submitting this assignment, I declare that the source code contained in this assignment was written
#solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
#in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
#instructions, nor obtained from a subscription service. I understand that copying any source code,
#in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
#I will receive a zero on this project if I am found in violation of this policy.

firstName = 'Ian' # My name
print('Hello, my name is ' + firstName) # Print a greeting

school = 'Utah Valley University' # The name of my school
print('I go to ' + school) # Print the school I attend

credits = 3 # The number of credits per class
classes = 6 # The number of classes I am taking
totalCredits = credits * classes # The total number of credits I will be taking
creditsPerClass = 3 # The number of credits per class

print('If I take 6 classes this semester and all are three credits each I will be taking ' + str(totalCredits) + ' credits')
# Print the total number of credits I will be taking per semester

print('I would like to save money by taking this many credits.')
# Everyone likes to save money

maxCredits = 12 # The maximum number of credits I pay for
costPerClass = 350 # The cost per class
classFee = 20 # The class fee per class

totalCostPerSemester = ((totalCredits - maxCredits) / creditsPerClass) * (costPerClass + classFee)
# Calculates total cost per semester and assigns to variable
# Finds free credits, then converts that to number of free classes times cost

print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.')
# Displays the amount of money I will be saving per semester

totalCostPerYear = totalCostPerSemester * 3 # Calculates total cost per year and assigns to variable

print('That is a whopping $' + str(totalCostPerYear) + ' a year!')
# Almost saving enough to pay for a couple months of rent.

print('This was a very informative and worth while Python assignment!')
# Indeed it was
