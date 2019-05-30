
from greet import greet
from datetime import datetime
from difflib import get_close_matches

datestamp = datetime.utcnow()
costlist = dict()
day_cost = [datestamp, costlist]
cost_cat = list(costlist)
# name = input('Hello, What\'s your name: ')


def log(*msg, dt=None):
    dt = dt or datetime.utcnow()

    return ('{0}: {1}'.format(dt, msg))


def cost(amount, item):
    if item in costlist.keys():
        costlist[item] += amount
    else:
        costlist[item] = amount

def main():
    on = 1
    global cost_cat
    greet()
    while on:
        do = input('Did you spend another fund today? yes/no: ').strip().lower()
        if do == 'yes':

            try:
                amount = float(input('How much did you spend today?: '))
                amt = format(amount, '.2f')
                item = input(f'What did you use ${amt} for: ').strip().title()
            except ValueError:
                continue
            if len(get_close_matches(item, cost_cat)) > 0:
                for d in get_close_matches(item, cost_cat):
                    closeans = d
                    ans = input(f'Do you mean {closeans}? yes/no: ').strip().lower()
                    if ans == 'yes':
                        item = closeans
                        break
                    if ans == 'no':
                        cost_cat.append(item)
                    else:
                        print('Invalid Input')
            cost(amount,item)
            *cost_cat, = costlist
            *dc, =  costlist.values()
            daily_cost = sum(dc)
            # cost_cat = set(cost_cat)
            print(day_cost)
            print(cost_cat)
            print(daily_cost)

        elif do == 'no':
            daily_amt = format(daily_cost, '.2f')
            print(f'You spent a total of ${daily_amt} today')
            print('Have a nice day! and Spend Wisely')
            on = 0


        else:
            print('Invalid Input')


if __name__ == '__main__':
    main()
