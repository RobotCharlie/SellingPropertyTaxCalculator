import sys


# Constants
CAPITAL_GAIN_RATE = 0.5  # 50% of the capital gain will be taxed


def calculate_yearly_income_tax_fed(income):
    """
    Refer: https://turbotax.intuit.ca/tips/an-overview-of-federal-tax-rates-286
    :param income: total income
    :return: tax
    """

    tax_fed = 0
    rest_income = income
    income_taxed_fed_portions = [48_535, 48_534, 53_404, 63_895, sys.float_info.max]
    income_portion_fed_tax_rates = [0.15, 0.205, 0.26, 0.29, 0.33]

    for index, portion in enumerate(income_taxed_fed_portions):
        actual_taxable_portion_fed = rest_income if 0 < rest_income < portion else portion
        tax_fed += actual_taxable_portion_fed * income_portion_fed_tax_rates[index]
        rest_income = (rest_income - portion) if rest_income > portion else 0
        print(f'For the portion: CAD {portion}, you have taxable income: CAD {actual_taxable_portion_fed}, '
              f'need to pay federal tax amount: CAD {actual_taxable_portion_fed * income_portion_fed_tax_rates[index]} = ({actual_taxable_portion_fed} * {income_portion_fed_tax_rates[index]}), '
              f'now total federal tax to pay is CAD {tax_fed}, you still have payable income amount CAD: {rest_income}')
        if rest_income <= 0:
            break  # no need to calculate next portion
    return tax_fed

def calculate_yearly_income_tax_ont(income):
    """
    Refer: https://turbotax.intuit.ca/tips/an-overview-of-federal-tax-rates-286
    :param income: total income
    :return: tax
    """

    tax_ont = 0
    rest_income = income
    income_taxed_ont_portions = [44_740, 44_742, 60_518, 70_000, sys.float_info.max]
    income_portion_ont_tax_rates = [0.0505, 0.0915, 0.1116, 0.1216, 0.1316]

    for index, portion in enumerate(income_taxed_ont_portions):
        actual_taxable_portion_ont = rest_income if 0 < rest_income < portion else portion
        tax_ont += actual_taxable_portion_ont * income_portion_ont_tax_rates[index]
        rest_income = (rest_income - portion) if rest_income > portion else 0
        print(f'For the portion: CAD {portion}, you have taxable income: CAD {actual_taxable_portion_ont}, '
              f'need to pay Ontario tax amount: CAD {actual_taxable_portion_ont * income_portion_ont_tax_rates[index]} = ({actual_taxable_portion_ont} * {income_portion_ont_tax_rates[index]}), '
              f'now total Ontario tax to pay is CAD {tax_ont}, you still have payable income amount CAD: {rest_income}')
        if rest_income <= 0:
            break  # no need to calculate next portion
    return tax_ont

def calculate_selling_property_tax():
    print('Enter your yearly employment income (in unit of thousands. e.g.: enter 80 for yearly income CAD 80,000):')
    employment_income = float(input()) * (10 ** 3)

    print('Enter your property purchase price (in unit of million. e.g.: enter 1 for purchase price CAD 1,000,000):')
    property_purchase_price = float(input()) * (10 ** 6)

    print('Enter your property sold price (in unit of million. e.g.: enter 1 for sold price CAD 1,000,000):')
    property_sold_price = float(input()) * (10 ** 6)

    print('Calculating your yearly income tax..')

    # Validation

    # Calculation
    gain = property_sold_price - property_purchase_price
    if gain <= 0:
        print('Sold price must be greater than purchase price!')

    taxable_gain = gain * CAPITAL_GAIN_RATE

    yearly_total_income = taxable_gain + employment_income

    return (
        round(calculate_yearly_income_tax_fed(yearly_total_income), 2),
        round(calculate_yearly_income_tax_ont(yearly_total_income), 2)
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tax_fed, tax_ont = calculate_selling_property_tax()
    print(f'Your total tax to pay: CAD {tax_fed + tax_ont}')
    print('Federal tax portion: CAD', tax_fed)
    print('Ontario tax portion: CAD', tax_ont)
