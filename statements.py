has_good_credit = False
has_bad_credit = False
property_price = 1000000

if has_good_credit:
    property_price = property_price * (10 / 100)
    print(f' has good credit')
elif has_bad_credit:
    property_price = property_price * (20 / 100)
    print(f' has bad credit')
else:
    print(f' not eligible')

print(f' buyer should give a down payment of : Ksh {property_price}')