"""
Shane Bacchus
Class: CS 521 - Fall 1
Final Project - Expense Management Application - Expense Class + Unit Tests

"""

class Expense:
    """Expense Class to track expenses input by file"""
    def __init__(self, **expenses):
        self.expenses = expenses

    def __repr__(self):
        """Returns Expenses as dictionary"""
        return str(self.expenses)

    def sort_dictionary_descending(self):
        """Returns Expenses Sorted Descending"""
        sorted_descending_dict = dict(sorted(self.expenses.items(),key=lambda item: item[1],reverse=True))
        return sorted_descending_dict

    def dictionary_sum(self):
        """Returns Sum of all values in dictionary"""
        values = self.expenses.values()
        total=sum(values)
        return total
    
    def sum_without_max(self):
        """Returns Sum of all values without highest expense"""
        max_value = max(self.expenses.values())
        return Expense.dictionary_sum(self)-max_value


if __name__ == "__main__":
    # Unit Tests 
    """
    Example Input from file:

    'Food': 20.33, 'Movies': 60.00, 'Clothes': 255.37, 'Coffee': 47.79

    Please copy over the below assert statements to the expense_management file for testing since a lot of code needs to be copied over to this class to get the statements to run

    These Unit Tests test the methods that perform calculations and return values

   
    """
    
     #  Testing dictionary sum method
    values = string_to_dictionary.values()
    total=sum(values)
    assert total == expense.dictionary_sum(),'Error, method does not return correct sum'
    # Testing sum without max method
    max_value = max(string_to_dictionary.values())
    sum_without_max = total-max_value
    assert sum_without_max == expense.sum_without_max(), 'Error, method does return sum - max value'


    