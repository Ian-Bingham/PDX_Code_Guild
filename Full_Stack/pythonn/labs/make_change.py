# make_change.py 6/13/18

def make_change(dollar_amt):
    coin_dict = {"quarter": 25, "dime": 10, "nickel": 5, "penny": 1}
    dollar_amt_in_pennies = dollar_amt * 100

    left_over = dollar_amt_in_pennies
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    while left_over != 0:
        if left_over // coin_dict["quarter"] != 0:
            num_quarters = left_over // coin_dict["quarter"]
            left_over %= (num_quarters *  coin_dict["quarter"])
        elif left_over // coin_dict["dime"] != 0:
            num_dimes = left_over // coin_dict["dime"]
            left_over %= (num_dimes *  coin_dict["dime"])
        elif left_over // coin_dict["nickel"] != 0:
            num_nickels = left_over // coin_dict["nickel"]
            left_over %= (num_nickels *  coin_dict["nickel"])
        elif left_over // coin_dict["penny"] != 0:
            num_pennies = left_over // coin_dict["penny"]
            left_over %= (num_pennies *  coin_dict["penny"])

    print(f"${dollar_amt} dollars was converted into {num_quarters} quarters, {num_dimes} dimes, {num_nickels} nickels, {num_pennies} pennies.")

dollar_amt = round(float(input("Please enter the dollar amount that you would like to convert to coins: $")), 2)
make_change(dollar_amt)
