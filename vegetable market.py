# Initial Setup
print(" " * 10, "welcome to the vegetable market", " " * 10)
veg = ['tomato', 'onion', 'chilli', 'potato', 'brinjal']
quantity = [20, 30, 25, 15, 35]
price = [32, 26, 35, 30, 25]
cost_price = [15, 20, 35, 25, 30]

# Additional lists for cart, customer data, and profits
veg_sold = []
item_profit = []
quantity_sold = []
cart = []
cart_quantity = []
total_list = []
customer_name = []
customer_mobile = []
item_total = 0

# Main Program Loop
while True:
    choice = input('1. Owner Section, 2. Customer Section, 3. Exit: ')
    
    if choice == '1':  # Owner Section
        while True:
            print("\nMenu:")
            print("1. Add vegetable")
            print("2. Remove vegetable")
            print("3. Modify vegetable")
            print("4. View stock")
            print("5. View report")
            print("6. Total revenue")
            print("7. Exit")
            choice = int(input("Enter choice: "))
            
            if choice == 1:
                item = input('Which vegetable do you want to add: ')
                if item not in veg:
                    qty = int(input('How much quantity to add: '))
                    cst = int(input("Enter the cost price: "))
                    slt = int(input('Enter the selling price: '))
                    veg.append(item)
                    quantity.append(qty)
                    price.append(slt)
                    cost_price.append(cst)
                    print(item, 'added')
                else:
                    print(item, 'is already in stock')

            elif choice == 2:
                item = input('Which vegetable do you want to remove: ')
                if item in veg:
                    idx = veg.index(item)
                    veg.pop(idx)
                    quantity.pop(idx)
                    price.pop(idx)
                    cost_price.pop(idx)
                    print(item, 'removed from stock')
                else:
                    print(item, 'not found in stock')

            elif choice == 3:
                item = input('Enter vegetable name to modify: ')
                if item in veg:
                    idx = veg.index(item)
                    new_qty = int(input('Enter new quantity: '))
                    new_price = int(input('Enter new price: '))
                    new_cost_price = int(input('Enter new cost price: '))
                    quantity[idx] = new_qty
                    price[idx] = new_price
                    cost_price[idx] = new_cost_price
                    print(item, 'updated')
                else:
                    print(item, 'not found in stock')

            elif choice == 4:
                print("\nCurrent Stock:")
                for i in range(len(veg)):
                    print(veg[i], ' - ', quantity[i], 'kg - ', price[i], ' per kg')

            elif choice == 5:
                print("\nCustomer Details:")
                for i in range(len(customer_name)):
                    print(customer_name[i], ' - ', customer_mobile[i])
                print("\nItemized Profit:")
                for i in range(len(veg_sold)):
                    print(veg_sold[i], ' - Profit: ', item_profit[i])
                print("Total Profit: ", sum(item_profit))

            elif choice == 6:
                print("Total Revenue: ", sum(total_list))

            elif choice == 7:
                print('Exiting Owner Section')
                break

            else:
                print('Invalid choice. Please try again.')

    elif choice == '2':  # Customer Section
        print('\nWelcome to the market!')
        while True:
            print('\nAvailable items:')
            for i in range(len(veg)):
                print(veg[i], ': ', quantity[i], 'kg - ', price[i], ' per kg')
            
            print('\n1. View Cart')
            print('2. Add to Cart')
            print('3. Remove from Cart')
            print('4. Modify Cart')
            print('5. Checkout/Exit')

            choice = int(input('Choose an option: '))
            
            if choice == 1:
                if cart:
                    print("\nYour Cart:")
                    for i in range(len(cart)):
                        print(cart[i], ' - ', cart_quantity[i], 'kg')
                    print('Total Amount: ', item_total)
                else:
                    print('Your cart is empty.')

            elif choice == 2:
                item = input('Which item would you like to add: ')
                if item in veg:
                    qty = float(input('How much quantity do you want: '))
                    idx = veg.index(item)
                    if qty <= quantity[idx]:
                        quantity[idx] -= qty
                        if item not in cart:
                            cart.append(item)
                            cart_quantity.append(qty)
                        else:
                            cart_idx = cart.index(item)
                            cart_quantity[cart_idx] += qty
                        amount = qty * price[idx]
                        item_total += amount
                        profit = (price[idx] - cost_price[idx]) * qty
                        if item not in veg_sold:
                            veg_sold.append(item)
                            item_profit.append(profit)
                            quantity_sold.append(qty)
                        else:
                            veg_index = veg_sold.index(item)
                            quantity_sold[veg_index] += qty
                            item_profit[veg_index] += profit
                        print(item, 'added to cart.')
                    else:
                        print('Not enough stock available.')
                else:
                    print('Item out of stock.')

            elif choice == 3:  # Remove from Cart
                item = input('Which item would you like to remove: ')
                if item in cart:
                    idx = cart.index(item)
                    qty_to_remove = cart_quantity[idx]
                    veg_idx = veg.index(item)
                    quantity[veg_idx] += qty_to_remove  # Return quantity to stock
                    item_total -= qty_to_remove * price[veg_idx]  # Adjust total
                    cart.pop(idx)  # Remove item from cart
                    cart_quantity.pop(idx)  # Remove quantity from cart list
                    print(item, 'removed from cart.')
                else:
                    print('Item not found in cart.')

            elif choice == 4:
                item = input('Enter item to modify: ')
                if item in cart:
                    cart_idx = cart.index(item)
                    veg_idx = veg.index(item)
                    new_qty = float(input('Enter new quantity: '))
                    if new_qty <= (quantity[veg_idx] + cart_quantity[cart_idx]):
                        quantity[veg_idx] += cart_quantity[cart_idx] - new_qty
                        item_total += (new_qty - cart_quantity[cart_idx]) * price[veg_idx]
                        cart_quantity[cart_idx] = new_qty
                        print(item, 'quantity updated.')
                    else:
                        print('Not enough stock available.')
                else:
                    print('Item not found in cart.')

            elif choice == 5:
                customer_name_input = input('Enter your name: ')
                customer_mobile_input = input('Enter your mobile number: ')
                customer_name.append(customer_name_input)
                customer_mobile.append(customer_mobile_input)
                total_list.append(item_total)
                print('\nBill:')
                for i in range(len(cart)):
                    print(cart[i], ' - ', cart_quantity[i], 'kg')
                print('Total Amount: ', item_total)
                print('Thank you for shopping!')
                cart.clear()
                cart_quantity.clear()
                item_total = 0
                break

            else:
                print('Invalid option. Please try again.')

    elif choice == '3':  # Exit Program
        print('Thank you for using the vegetable market system.')
        break

    else:
        print('Invalid choice. Please try again.')
