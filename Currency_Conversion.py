# A Quick Currency Conversion with forex_python.

import forex_python.converter
# import CurrencyRates

# Create an instance of CurrencyRates class from forex_python.converter
converter = forex_python.converter.CurrencyRates()
try:

    # Get the amount to be converted from the user
    amount = int(input('Enter the desired amount you want to convert:\n'))

    # Get the currency code that has to be converted from the user
    from_currency = input(
        'Enter the currency code that has to be converted:\n').upper()

    # Get the currency code to convert to from the user
    to_currency = input('Enter the currency code to convert:\n').upper()

    # Print the conversion details
    print('You are converting', amount, from_currency, 'to', to_currency, '.')

    # Perform the conversion and store the result in variable output
    output = converter.convert(from_currency, to_currency, amount)

    # Print the converted rate
    print(f'The converted rate is {output}')

except Exception as e:
    print("An error occurred: ", str(e))
