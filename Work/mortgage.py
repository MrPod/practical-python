# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 109
extra_payment = 1000
month = 0

while principal > 0:
    if extra_payment_start_month < month < extra_payment_end_month:
        p = payment + extra_payment
    else:
        p = payment

    if principal * (1+rate/12) - p > 0:
        principal = principal * (1+rate/12) - p
        total_paid += + p
    else:
        principal = 0
        total_paid += principal
    month += 1
    print(month, total_paid, principal)

print('Total paid', total_paid)
print('Total months', month)
