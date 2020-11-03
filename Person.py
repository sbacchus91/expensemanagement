"""
Shane Bacchus
Class: CS 521 - Fall 1
Final Project - Expense Management Application - Person Class + Unit Tests

"""

class Person:
  """Person Class to track personal info such as age, income, and tax rate"""
  def __init__(self, first="", last="",age="",income="",tax_rate=""):
    self.first_name = first
    self.last_name = last
    self.age = age
    self.__income = income #  Private attribute
    self.___tax_rate = tax_rate #  Private attribute
    

  def __repr__(self):
    """Returns Person Attributes as dictionary"""
    return {'Name':self.first_name +' '+ self.last_name, 'Age':self.age, 'Income': self.__income, 'Tax Rate': self.___tax_rate}
  
  def name_age_display(self):
    """Returns Public Person Attributes as dictionary"""
    return {'Name':self.first_name +' '+ self.last_name, 'Age':self.age}

  def __income_tax_display(self): #  Private Method
    """Private Method that Returns Private Person Attributes as dictionary"""
    self.__income_after_taxes = self.__income -(self.__income*(self.___tax_rate/100.0))
    return {'Income': self.__income, 'Tax rate': self.___tax_rate, 'Estimated Income after Taxes': self.__income_after_taxes}



  if __name__ == "__main__":
    # Unit Tests 
    """
    Example Input:
    Name: Shane Bacchus
    Age: 28
    Income: 100000
    Tax Rate: 35

    Unit Tests do not take formatting into consideration. 
    Example, we will test for income == 100000.0, not 100,000.00

    You can copy & paste the below uncommented lines of code into 
    expense_management.py 

    """

    #person = Person(first,last,age,income,tax_rate)
    person_dictionary = person.__repr__()
    #income_tax_dictionary = person._Person__income_tax_display()
    assert person_dictionary['Name'] == 'Shane Bacchus', 'Error, Name is not correct'
    assert person_dictionary['Age'] == 28, 'Error, Age is not correct'
    assert person_dictionary['Income'] == 100000.0, 'Error, Income is not correct'
    assert person_dictionary['Tax Rate'] == 35.0, 'Error, Tax Rate is not correct'
    assert income_tax_dictionary['Estimated Income after Taxes'] == 65000.0, 'Error, income after tax calculation is incorrect'