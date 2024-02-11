def amounts():
    bill_amount = float(input("What is the bill? "))
    tip_percentage = float(input("What is the tip percentage? "))    
    
    return bill_amount, tip_percentage
    
def math(bill, tip):
    tip_amount = bill * (tip / 100)
    total = bill + tip_amount
    
    return tip_amount, total
    
def output(tip_amount, total_amount):
    print(f"The tip is ${tip_amount:.2f}")
    print(f"The total is ${total_amount:.2f}")
    
def main():
    bill, tip = amounts()
    tip_total, total = math(bill, tip)
    output(tip_total, total)
    
main()