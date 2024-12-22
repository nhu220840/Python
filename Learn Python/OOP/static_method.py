# Static method = A method that belong to a class rather than any obj from that class (instance)
#                 Usually used for general utility functions
        
# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    
employee1 = Employee("Nhu", "Manager")
employee2 = Employee("Vezyl", "Cashier")
employee3 = Employee("Cun", "Cook")
    
print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Rocket"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

