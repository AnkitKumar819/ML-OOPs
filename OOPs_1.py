class Employee:
    #special/ magic/ dunder
    def __init__(self):
        
        self.id = 121
        self.salary = 50000
        self.designation = 'IT'
        pass 
    
    
    def travel(self, destination):
        print(f"Employee is now traveling to {destination}")
    
sam = Employee()
#print(sam.designation)

sam.travel("mumbai")