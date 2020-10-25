import sys


# Constants
CAPITAL_GAIN_RATE = 0.5  # 50% of the capital gain will be taxed


def calculate_yearly_income_tax(income):
    """
    Refer: https://turbotax.intuit.ca/tips/an-overview-of-federal-tax-rates-286
    :param income: total income
    :return: tax
    """

    print('Calculating yearly income tax..')
    tax = 0
    rest_income = income
    income_taxed_portions = [48_535, 48_535, 53_404, 63_895, sys.float_info.max]
    income_portion_tax_rates = [0.15, 0.205, 0.26, 0.29, 0.33]

    for index, portion in enumerate(income_taxed_portions):
        actual_taxable_portion = rest_income if 0 < rest_income < portion else portion
        tax += actual_taxable_portion * income_portion_tax_rates[index]
        rest_income = (rest_income - portion) if rest_income > portion else 0
        print(f'For the next portion: CAD {portion}, you have taxable income: CAD {actual_taxable_portion}, '
              f'need to pay tax amount: CAD {actual_taxable_portion * income_portion_tax_rates[index]} = ({actual_taxable_portion} * {income_portion_tax_rates[index]}), '
              f'now total tax to pay is CAD {tax}, you still have payable income amount CAD: {rest_income}')
        if rest_income <= 0:
            break  # no need to calculate next portion
    return tax


def calculate_selling_property_tax():
    print('Enter your yearly employment income (in unit of thousands. e.g.: enter 80 for yearly income CAD 80,000):')
    employment_income = float(input()) * (10 ** 3)

    print('Enter your property purchase price (in unit of million. e.g.: enter 1 for purchase price CAD 1,000,000):')
    property_purchase_price = float(input()) * (10 ** 6)

    print('Enter your property sold price (in unit of million. e.g.: enter 1 for sold price CAD 1,000,000):')
    property_sold_price = float(input()) * (10 ** 6)

    # Validation

    # Calculation
    gain = property_sold_price - property_purchase_price
    if gain <= 0:
        print('Sold price must be greater than purchase price!')

    taxable_gain = gain * CAPITAL_GAIN_RATE

    yearly_total_income = taxable_gain + employment_income

    yearly_income_tax = calculate_yearly_income_tax(yearly_total_income)

    return yearly_income_tax


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total_selling_property_tax = calculate_selling_property_tax()
    print('Your total tax to pay is..')
    print('CAD', total_selling_property_tax)
