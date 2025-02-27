class MenuItem:
    def __init__(self, itemID, name, price) -> None:
        self.itemID = itemID
        self.name = name
        self.price = price

    def getItemDetails(self):
        return f"{self.itemID}, {self.name}, {self.price}"
    

class Order:
    def __init__(self, orderID, items, tableNumber) -> None:
        self.orderID = orderID
        self.items = items
        self.tableNumber = tableNumber
        

    def addItem(self, item):
        self.items.append(item)

    def calculateTotal(self):
        total = 0
        for i in self.items:
            total += i.price
        return total


class OrderManager:
    def __init__(self, orders) -> None:
        self.orders = orders

    def createOrder(self, order):
        self.orders.append(order)

    def cancelOrder(self, orderID):
        for i in self.orders:
            if orderID == i.orderID:
                self.orders.remove(i)
            return True
        return False


    def getOrder(self, orderID):
        for i in self.orders:
            if orderID == i.orderID:
                return i
        return None











def main():
# Create menu items
    item1 = MenuItem(1, "Burger", 8.5)
    item2 = MenuItem(2, "Fries", 3.0)
    item3 = MenuItem(3, "Soda", 2.0)

    # Create an order and add items
    order = Order(101, [], 5)
    order.addItem(item1)
    order.addItem(item2)
    order.addItem(item3)
    total = order.calculateTotal()
    print("Calculated total:", total)

    # Remove an item and recalc total
    # removed = order.removeItem(2)
    # print("Item 2 removed:", removed)
    # print("New total after removal:", order.calculateTotal())

    # Test OrderManager functionality
    om = OrderManager([])
    om.createOrder(order)
    retrieved_order = om.getOrder(101)
    print("Retrieved order for table", retrieved_order.tableNumber)
    cancelled = om.cancelOrder(101)
    print("Order cancellation status:", cancelled)

    
if __name__ == '__main__':
    main()