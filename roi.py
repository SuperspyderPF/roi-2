class Calculator_ROI():
    def __init__(self):
        while True:
            try:
                total = int(input("What is the purchase price of the house ? ".title()))
                self.total = total
                print(f"Price of House ${total}".title())

            except ValueError:
                
                print("wrong! try again! ".title())
                continue
            break



    def calculations(self):
        Calculator_ROI.cash_flow(self)
        Calculator_ROI.roi(self)


   
    def income(self):
        while True:
            try:
                rental_income = int(input("Income From Rental?".title() ))
                print(f"Income From Rental: ${rental_income}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                misc = int(input("other sources of income".title()))
                print(f"added income: ${misc}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        
        total_income = rental_income + misc
        print(f"Your total income by month = ${total_income}".title())
        print(f"-"*100)
        return total_income



  
    def expenses(self):
        while True:
            try:
                mortgage = int(input("Mortgage Price ".title()))
                print(f"Mortgage price: ${mortgage}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                tax = int(input("property taxes? ".title()))
                print(f"taxes: ${tax}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                insurance = int(input("insurance on the house ".title()))
                print(f"Insurance price: ${insurance}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                utilities = int(input("utility costs ".title()))
                print(f"costs of utility: ${utilities}")
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                hoa = int(input("HOA fees?? "))
                print(f"HOA Fees: ${hoa}")
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                lawn_care = int(input("lawn fees? ".title()))
                print(f"Lawn fees ${lawn_care}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                vacancy = int(input("budget for vacancy? ".title()))
                print(f"Vacancy budget: ${vacancy}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                repairs = int(input("Repairs budget? ".title()))
                print(f"Repair savings: ${repairs}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
       
            break
        while True:
            try:
                management = int(input("property manager costs? ".title()))
                print(f"Property manager costs: ${management}")
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break

        total_expenses = mortgage + tax + insurance + utilities + hoa + lawn_care + vacancy + repairs + + management
        print(f"-"*100)
        print(f"Your monthly expenses = ${total_expenses}".title())
        return total_expenses
   
    def cash_flow(self):
        total_cash_flow = self.income() - self.expenses()
        self.total_cash_flow = total_cash_flow
        print(f"\nYour cash flow by month = ${total_cash_flow}".title())
        print(f"-"*100)
        return total_cash_flow
    
    def roi(self):
        while True:
            try:
                down_payment = int(input("Down payment??.title() "))
                print(f"Down payment: ${down_payment}")
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        while True:
            try:
                closing_cost = int(input("any closing costs? ".title()))
                print(f"Closing costs: ${closing_cost}")
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break

        while True:
            try:
                misc = int(input("repairs/Renovations budget?? ".title()))
                print(f"repairs budget: ${misc}".title())
            except ValueError:
                print("wrong! try again! ".title())
                continue
            break
        total_investment = down_payment + closing_cost + + misc
        annual_cash_flow = self.total_cash_flow * 12
        cash_roi = (annual_cash_flow / total_investment) * 100
        print(f"-"*100)
        print(f"Your Cash on Cash ROI for this property = {cash_roi}%")



def call_func():
    my_total = Calculator_ROI()
    my_total.calculations()

call_func()