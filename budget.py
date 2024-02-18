class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        pass

    def deposit(self, amount, description=''):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        self.amount = amount
        self.description = description

        if self.check_funds(amount):
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total_balance = 0
        for item in self.ledger:
            total_balance += item["amount"]
        return total_balance
    
    def transfer(self, amount, category):
        
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"Transfer to {category.name}"})
            category.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})
            print('yes')
            return True
        else:
            print('no')
            return False
        
    def check_funds(self, amount):

        if self.get_balance() > abs(amount):
            return True
        else:
            return False
    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.deposit(500, "crypto airdrop")
food.withdraw(-750, "sushi")
clothes = Category("Clothes")
clothes.deposit(5000, "gucci tshirt")
clothes.deposit(1000, "kalvin klein")
clothes.deposit(-850, "yellow jacket")
total_amount = clothes.get_balance()
total_amount = food.get_balance()
print(total_amount)
print(food.ledger)
print(clothes.ledger)
food.transfer(50, clothes)
print(total_amount)
print(food.ledger)
print(clothes.ledger)

def create_spend_chart(categories):
    pass