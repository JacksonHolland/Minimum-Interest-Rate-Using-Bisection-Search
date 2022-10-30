##############################################
##############################################
initial_deposit = float(input('Enter the initial deposit: '))
cost_of_house = float(input('Enter the cost of the house: '))
portion_of_house = (float(input('Enter the down payment percentage: '))/100)
number_of_years = float(input('Enter the number of years until down payment: '))

#########################################################################
#########################################################################
cost_of_down_payment = cost_of_house * portion_of_house
months = number_of_years * 12

lower_bound = cost_of_down_payment - 100
upper_bound = cost_of_down_payment + 100

upper = 1
lower = 0
r = .5

final_savings = (initial_deposit * ((1+r/12)**months))

control = True
steps = 0

##################################################################################################
##################################################################################################
if initial_deposit >= lower_bound:
    r = 0
    print(f'Best savings rate: {r} [or very close to this number]')
    control = False

if initial_deposit * (1+1/12)**months < lower_bound:
    r = None
    print('The initial deposit is not high enough to pay the down payment after three years.')
    control = False

while control:
    if final_savings < lower_bound:
        lower = r
    elif final_savings > upper_bound:
        upper = r
    else:
        print(f'Best savings rate: {r} [or very close to this number]')
        print(f'Steps in bisection search: {steps} [or very close to this number]')
        control = False
    r = (upper + lower) / 2
    steps += 1
    final_savings = (initial_deposit * ((1+r/12)**months))

