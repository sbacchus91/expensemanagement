"""
Shane Bacchus
Class: CS 521 - Fall 1
Final Project - Expense Management Application - Main Program

"""

from Person import *
from Expense import *

if __name__ == "__main__":
    #  Ask for and validate Personal info input
    while True:
        try:
            first, last = input("Please enter your First Name and Last Name separated by a space: ").split()
            break
        except: ValueError: print("You did not enter your First and Last Name separated by a space, please try again")
    
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age > 100:
                print("You are probably not over 100 years old. Try again")
                continue
            break
            
        except: ValueError: print("You did not enter a number. Please try again")
    
    while True:

        try: 
            income = float(input("Please enter your Income with no spaces or characters: "))
            tax_rate = float(input("Please enter your Estimated Tax Rate: "))
            break
        except: ValueError: print("Your Income or Tax Rate were entered incorreclty, please try again")

    
    #  Get file with expense records

    print('\n')
    print("Thank you for your personal information!")
    print('\n')

    print("Now, we are looking for your expenses in a file titled expenses.txt")
    print("Your expenses must be one line, in this format: 'Food': 20.33, 'Movies': 60.00")
    try:
        temp_file = open("expenses.txt","r") #  open the file for reading
        print("File Found! Moving on!")
    except FileNotFoundError: 
        print("File not found, program terminating")
        exit()
    
    def read_file(temp_file):
        """Read file and turn to list of lists"""
        line_string = ""
        for line in temp_file:
            line_string+=line
        return line_string


    file_to_string = read_file(temp_file) #  Call function to create string
    file_to_string = '{'+file_to_string+'}' #  add brackets for dict conversion
    string_to_dictionary = eval(file_to_string) # Convert to dictionary
    temp_file.close() # Close File

    #  Instantiate person and expense object
    expense = Expense(**string_to_dictionary)
    person = Person(first,last,age,income,tax_rate)

    #  Print Name and Age
    print('\n')
    print("Here's a summary of your financial picture and expenses")
    print('\n')
    name_age_dictionary = person.name_age_display()
    print('Your Name & Age:')
    for key, value in name_age_dictionary.items():
        print(key,':',value)

    #  Private method call - Print Income, Tax Rate, and After Tax Income
    income_tax_dictionary = person._Person__income_tax_display()
    print('Your Income, Tax Rate, and estimated after-Tax Income:')
    for key, value in income_tax_dictionary.items():
        print(key,':','{:,.2f}'.format(value))

    #  Print summary statistics of all Expenses
    print('\n')
    print("Here are your expenses in descending order:")
    x = expense.sort_dictionary_descending()
    print('\n'.join("{}: {}".format(k, v) for k, v in x.items()))
    print('\n')
    print("Here is the sum of all your expenses:")
    print('{:,.2f}'.format(expense.dictionary_sum()))
    print("Here is the sum of all your expenses without your greatest expense:")
    print('{:,.2f}'.format(expense.sum_without_max()))
    print("Assuming these expenses repeated once a month, here's how much you'd spend:")
    expenses_per_year = 12*expense.dictionary_sum()
    print('{:,.2f}'.format(expenses_per_year))
    expenses_as_percent_of_income = expenses_per_year/income_tax_dictionary['Estimated Income after Taxes']
    if expenses_as_percent_of_income < .2:
        print("Your projected expenses are less than 20% of your yearly income")
        print("That's great!")    
    else:
        print("Your projected expenses greater than 20% of your yearly income. It may be worth adjusting your spending")
    print('Here is that percentage: '+ str(round(expenses_as_percent_of_income*100)) + '%')
    print('\n')
    print("I hope you enjoyed this program!")

   

   
    