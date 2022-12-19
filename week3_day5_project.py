import random
class House:
    def __init__(self,house_price):
        self.house_price = house_price
        print('this is the house price',house_price)
    def get_income(self):
        #self.rental_income = self.house_price *.01 * random.uniform(0,.02)
        self.rental_income = self.house_price *.01 * random.uniform(0,.02)
        #self.misc_rental_income = self.house_price *.0025
        self.misc_rental_income = self.house_price * random.uniform(0,.01)
        self.total_income = self.rental_income + self.misc_rental_income
        print('this is the rental income',self.total_income)
        return self.total_income
    def expenses(self):
        #self.expensess = House.get_income(self) *.825
        self.expensess = House.get_income(self) * random.uniform(.55,.9)
        print('this is the expenses',self.expensess)
        return self.expensess
    def cash_flow(self):
        self.cash_floww = House.get_income(self) - House.expenses(self)
        print('this is the cash flow',self.cash_floww)
        return(self.cash_floww)
    def return_on_investment(self):
        #self.down_payment = self.house_price * .20
        self.down_payment = self.house_price * random.uniform(.10,.30)
        #self.closing_cost = self.house_price * .0125
        self.closing_cost = self.house_price * random.uniform(.01,.0125)
        #self.rehab_budget = self.house_price *.03
        self.rehab_budget = self.house_price  * random.uniform(0,.05)
        self.total_house_initial_investment = self.down_payment + self.closing_cost + self.rehab_budget
        self.return_on_investment_calculated = round(((House.cash_flow(self)*12) / self.total_house_initial_investment) * 100,2) 
        print('this is the ROI per year:' ,self.return_on_investment_calculated,'%')
        return self.return_on_investment_calculated
house = House(200000)
house.return_on_investment()
