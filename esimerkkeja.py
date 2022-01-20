money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price
 
sandwich_price += sales_tax
money_in_wallet -= sandwich_price

print(sales_tax)
print(money_in_wallet)
#
fish_in_clarks_pond = 50
 
print("Catching fish")
 
number_of_fish_caught = 10
fish_in_clarks_pond = fish_in_clarks_pond - number_of_fish_caught

print(fish_in_clarks_pond)
#
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall += september_rainfall
annual_rainfall += october_rainfall
annual_rainfall += november_rainfall
annual_rainfall += december_rainfall
#
# this evaluates to 150:
float4 = 1.5e2 
#
cucumbers = 100
num_people = 6

whole_cucumbers_per_person = int(100/6)
print(whole_cucumbers_per_person)

float_cucumbers_per_person = float(cucumbers)/num_people
print(float_cucumbers_per_person)
#
