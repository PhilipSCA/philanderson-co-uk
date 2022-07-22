# Friday 22/7/22
#   Assigning a default value to a parameter


def calc_tax(sales_total, tax_rate):
    print(sales_total * tax_rate)

calc_tax(sales_total = 101.37, tax_rate = .05)

# This displays 5.0685

# To make something the default value, you declare it when making the function
def calc_tax(sales_total, tax_rate = .04):
    print(sales_total * tax_rate)

calc_tax(sales_total = 101.37)
# Then you dont need it when you call the function, the tax_rate is already known as 0.4

# You can make an empty default parameter
def print_order(product, color, size, engraving_text=""):
    print(print_order)

