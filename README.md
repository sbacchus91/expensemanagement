# expensemanagement
Expense Management Application

# Background and Motivation
There are many Expense Management tools in market. The need is obvious – we all need to be able to effectively manage our resources. It is very easy to plug in our Credit Card or Bank information to port over all of our transactions and get a summary view of our financial picture. We can easily determine where we can cut down our spending. Some applications will also give us recommendations on ways to reduce spending, or projections to help us understand the long term impact of continued spending or changes in our spending behavior.  It is often also helpful to be able to track our expenses in relation to our Post-tax income. I wanted to build a version of these type of applications (simple now, but will improve in the future). Financial health is very important to me as it is for many others, which is why I decided on this topic. 

# What this program does
My program will accept user input on their personal info – Name, Age, Income, and estimated Tax Rate. This information will be displayed back to the user in an organized fashion, with Post-Tax Income calculated. 
Furthermore, a file of Expense records will also be accepted. The Expenses will be displayed in an organized fashion, and summary statistics of these expenses + these expenses in relation to your Post-Tax income will be calculated and displayed. 

# Program Structure:
There are 4 components necessary to run this program: 
•	expense_management.py (main program)
•	Person.py (Class file used to track personal information the user enters into our application)
•	Expense.py (Class file used to track the expenses the user enters via file input)
•	expenses.txt (file that stores sample expenses to be stored and analyzed)

# Instructions on how to run Code 
Running the code is as simple as running the expense_management.py file, and ensuring the expense file (expenses.txt) is present in the same directory with the expense records in the correct format, else the program will terminate. There are no third-party modules that are present. 
Unit Tests were provided in the ‘main’ program in the Class files. That code can be copied over to expense_management.py to confirm that no assertion errors are thrown and that the Unit Tests are passed.  
