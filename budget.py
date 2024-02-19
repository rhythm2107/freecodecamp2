class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        left_stars = (30 - len(self.name)) // 2 # 12 for foods
        right_stars = 30 - len(self.name) - left_stars # 13 fod foods
        total = self.get_balance()

        header_line = f"{'*' * left_stars}{self.name}{'*' * right_stars}"
        total_line = f'Total: {total}'
        
        transactions = header_line + '\n'
        

        for item in self.ledger:
            description = item["description"]
            amount = str(item["amount"])
            if amount.count('.') == 0:
                amount += '.00'

            desc_len = 0
            if len(description) >= 23:
                desc_len = 23
            else:
                desc_len = len(description)
            
            ledger_line = f"{description[:23]}{' ' * (30-desc_len-len(amount))}{amount.rjust(1)}\n"
            transactions += ledger_line

        transactions += total_line

        return transactions

    def deposit(self, amount, description=''):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        self.amount = amount
        self.description = description

        if self.check_funds(amount):
            negated_amount = -amount
            self.ledger.append({"amount": negated_amount, "description": description})
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

        if self.get_balance() >= abs(amount):
            return True
        else:
            return False
    
food = Category("Food")
food.deposit(1000, "initial deposit and testing")
food.deposit(500, "crypto airdrop")
food.withdraw(750, "sushi")
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
print(food)

def create_spend_chart(categories):
    
    for category in categories:
        pass