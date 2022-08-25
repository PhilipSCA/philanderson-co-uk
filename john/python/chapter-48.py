date = "Thursday 25/08/22"
print(date)

# Condensing code
def calc_tax(sales_total, tax_rate):
  tax = sales_total * tax_rate
  print(tax)

# Instead of writing:
sales_tax = calc_tax(sales_total=101.37, tax_rate=.05)
print(sales_tax)

# Write this:
print(calc_tax(sales_total=101.37, tax_rate=.05))

# Another example
def add_numbers(first_number, second_number):
  return first_number + second_number

def subtract_numbers(first_number, second_number):
  return first_number - second_number

# Instead of writing:
result_of_adding = add_numbers(1, 2)
result_of_subtracting = subtract_numbers(3, 2)
sum_of_results = result_of_adding + result_of_subtracting

# You could make it into 1 simple line - Write this:
sum_of_results = add_numbers(1, 2) + subtract_numbers(3, 2)