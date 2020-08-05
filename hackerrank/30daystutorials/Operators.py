meal_cost = float(raw_input())
tip_percentage = int(raw_input())
tax_percentage = int(raw_input())

print "The total meal cost is %.0f dollars."%(meal_cost*(tip_percentage/100.0 + 1+ tax_percentage/100.0))