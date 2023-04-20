
has_high_income = False
has_good_credit = True
no_criminal_record = True

# AND
if has_good_credit and has_high_income:
    print('Eligible for a loan')
else:
    print('Not eligible')

# OR
if has_good_credit or has_high_income:
    print('Eligible for a loan')
else:
    print('Not eligible')


# NOT
if has_good_credit and not no_criminal_record:
    print('Eligible for a loan')
else:
    print('Not eligible Criminal Records available')