# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Constants
CAPITAL_GAIN_RATE = 0.5  # 50% of the capital gain will be taxed


def calculate_yearly_income_tax(income):
    """
    Refer: https://turbotax.intuit.ca/tips/an-overview-of-federal-tax-rates-286
    :param income: total income
    :return: tax
    """
    tax = 0
    total_income = income
    rest_income = income

    if rest_income > 48_535:
        tax += (48_535 * 0.15)
        rest_income -= 48_535
    if rest_income > 48_535:
        tax += (48_535 * 0.205)
        rest_income -= 48_535
    if rest_income > 53_404:
        tax += (53_404 * 0.26)
        rest_income -= 53_404
    if rest_income > 64_895:
        tax += (64_895 * 0.29)
        rest_income -= 64_895
    if rest_income > 64_895:
        tax += (64_895 * 0.29)
        rest_income -= 64_895
    if total_income > 214_368:
        tax += ((total_income - 214_368) * 0.33)

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
    print('Your total tax to pay is..')
    print('CAD', calculate_selling_property_tax())
