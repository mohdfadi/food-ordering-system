#creating a food ordering system...
class Products():
    def __init__(self,Chicking,Pizza_ricotta,juicy,):
        self.Chicking = Chicking 
        self.Pizza_ricotta = Pizza_ricotta
        self.juicy =juicy


    @staticmethod
    def printMenu(hotel_Object):
        print('------Menu------')

        count = 1
        
        for x in hotel_Object:
            print(f'{count}. {x[0]} = {x[1]}')
            count += 1

        maxLength = len(hotel_Object)

        while True:
            orders = input("Enter your order numbers : ")
            spaceRemovedOrders = ''
            info = ''
            for i in orders.strip():
                if i != ' ' and i.isnumeric() == False:
                    info = 'non-numeric-error'
                    break
                elif i.isnumeric() and int(i) > maxLength: 
                    info = 'maxlength-exceeded'
                    break
                elif i != ' ':
                    spaceRemovedOrders += i

            if info == 'non-numeric-error':
                print("Error : Orders should be of numeric value")
                continue
            elif info == 'maxlength-exceeded':
                print("Error : Invalid order number")
                continue
            
            finalOrder = {}
            for i in spaceRemovedOrders:
                try:
                    finalOrder[i] += 1
                except:
                    finalOrder[i] = 1
            break

        # printing Bill
        total = 0
        billText = ''
        for key, value in finalOrder.items():
            billText += f'{hotel_Object[int(key) - 1][0]} x {value} = {value * hotel_Object[int(key) - 1][1]}\n' 
            total += value * hotel_Object[int(key) - 1][1]

        print(billText) 
        print(total,u"\u20B9")
        order_checkout = input('Order Item!' ' ' 'Enter:')
        if order_checkout == 'yes':
            print('Order Placed!')
            print('Thank You')  


Items = Products(
    [
        ['6 piece chicken + garlic dip + 1 Drink', 1199,],
        ['3 piece wings + 2 leg + 2 bun', 899],
        ['12 piece chicken + 4 bun + 2 coleslaw', 1300]
    ],
    [
        ['Chicken pepperoni large ', 570],
        ['Mushroom chicken large', 560 ],
        ['BBQ Cheesy Bites large', 540]   
    ],
    [
        ['tender malaba', 100],
        ['chikku malba', 100],
        ['chicken sandwich', 80],
        ['chicken roll', 80]
    ]      
)

print('WELCOME TO EAT AND DRINK')
customer = int(input(
   'You can order only from 1 shop at a time\n'
   'from which shop would you like order?\n'
   '1.Chicking\n2.Juicy\n3.pizza Ricotta\nEnter: '
))
orderfrom = None

if customer == int(1):
    orderfrom = Items.Chicking

elif customer == int(2):
    orderfrom =Items.juicy

elif customer == int(3):
    orderfrom = Items.Pizza_ricotta

ordering = input('would you like to order something?\nEnter: ')      

if ordering == 'yes':
    Items.printMenu(orderfrom)  
# developed by fadhi and ali izzath