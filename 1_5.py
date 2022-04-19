revenue = float(input("Enter your revenue: "))
costs = float(input("Enter your costs: "))

if (revenue > costs):

    print(f"\nThe company is making a profit of {revenue - costs}") 
    print(f"And with profitability of {(revenue - costs) / revenue:.2}\n")

    employees = int(input("Enter number of employees: "))
    print("Profit per an employee is %.2f\n" % ((revenue - costs) / employees))

else:

    print("The firm is unprofitable!\n")
