from datetime import datetime

# RETAIL STORE
# increase sales on Tuesday and Wednesday, the slowest sales days of the week.
# discount 10% of client's subtotal in case it's $50 or greater.


# Gets the subtotal from client 
subtotal = float(input("Inform the client subtota: "))
subtotalStrechActivitie = 0

# Gets the day of week
dt = datetime.now()
day_of_week = dt.weekday()

# if subtotal >= 50 then subtract 10% 

if  day_of_week in (1,2,6):
    if subtotal >= 50:
                discount = subtotal * 0.10
                subtotal =  subtotal -  discount
                print(f"Discount ammount: {discount:.2f}")
    else:
          subtotalStrechActivitie = 50
          discount = subtotalStrechActivitie * 0.10
          subtotalStrechActivitie =  subtotalStrechActivitie -  discount
          
    

# apply 6% over the sales tax amount
sales_tx = subtotal * 0.06
print(f"Sales taxes: {sales_tx:.2f}")
subtotal = subtotal + sales_tx
print(f"Total: {subtotal:.2f}")

if subtotal < 50 and day_of_week in (1,2,6):
       subtotalStrechActivitie = subtotalStrechActivitie + (subtotalStrechActivitie * 0.06)
       newSubtotal = subtotalStrechActivitie - subtotal
       print(f"You can have a discount of ${newSubtotal:.2f} if you purchase at least $50.")