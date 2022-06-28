"""
    example04.py
    Python function basics
"""
def summary(customer: dict, amount: float = 0.0):
    return f'Customer: {customer.get("first")} {customer.get("last")}, amount: ${amount:,.2f}'


cust = {'first': 'James', 'last': 'Smith'}
results = summary(cust, 1108.23)
print(results)
