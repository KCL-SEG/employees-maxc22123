"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, commission = ()):
        self.name = name
        self.pay = pay
        self.commission = commission
        self.total = 0

    def get_pay(self):
        total = 0
        if len(self.pay) == 1:
            total += self.pay[0]

        else:
            total += self.pay[0] * self.pay[1]

        if self.commission:
            if len(self.commission) == 1:
                total += self.commission[0]
            else:
                total += self.commission[0] * self.commission[1]

        return total

    def __str__(self):
        str = f'{self.name} works on a '
        if len(self.pay) == 1:
            str += f'monthly salary of {self.pay[0]}'
        else:
            str += f'contract of {self.pay[1]} hours at {self.pay[0]}/hour'

        if self.commission:
            str += f' and receives a '
            if len(self.commission) == 1:
                str += f'bonus commission of {self.commission[0]}.'
            else:
                str += f'commission for {self.commission[1]} contract(s) at {self.commission[0]}/contract.'
        else:
            str += '.'

        str += f'  Their total pay is {self.get_pay()}.'

        return str



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', (4000,))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', (25,100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', (3000,), (200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', (25, 150), (220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', (2000,), (1500,))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', (30,120), (600,))

print(str(jan))
