# solution
class Task:
    id_counter = 1
    def __init__(self, description, programmer, workload):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.status = False

    def is_finished(self):
        return self.status
    
    def mark_finished(self) -> bool:
        self.status = True

    def __str__(self) -> str:
        id = self.id
        description = self.description
        programmer = self.programmer
        workload = self.workload
        if self.status == True:
            return f"{id}: {description} ({workload} hours), programmer {programmer} FINISHED"
        else:
            return f"{id}: {description} ({workload} hours), programmer {programmer} NOT FINISHED"

class OrderBook:
    def __init__(self):
        self.orders = []
        self.programmers_with_orders = []

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        if order not in self.orders:
            self.orders.append(order)
            
        if order.programmer not in self.programmers_with_orders:
            self.programmers_with_orders.append(order.programmer)

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return self.programmers_with_orders
    

# test
if __name__ == "__main__":
    # test 1
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)


    # test 2
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)