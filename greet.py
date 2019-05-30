
def greet():
    from time import localtime as lt
    a=list(lt())
    name = input('What\'s your name: ')
    if a[3] <9:
        print(f'Good Morning {name}')
        print('How was your Night?')
    elif a[3]>=9 and a[3] <12:
        print(f'Good Morning {name}')
        print('How you doing today?')
    elif a[3] >=12 and a[3] <16:
        print(f'Good Afternoon {name}')
        print('How you doing today?')
    elif a[3]>=16 and a[3] <22:
        print(f'Good Evening {name}')
        print('How you doing today?')
    else:
        print(f'How you doing tonight, {name}?')
        print(f'Good Night {name}')

def __main():
    # name1=input("Hello What's your name: ")
    greet()

if __name__ == '__main__':
    __main()
