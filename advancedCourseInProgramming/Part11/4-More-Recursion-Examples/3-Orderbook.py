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

    def __str__(self):
        status = "NOT FINISHED" if not self.status else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.__tasks = []

    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))
    
    def all_orders(self):
        return self.__tasks

    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
    
    def mark_finished(self, id: int):
        for order in self.__tasks:
            if order.id == id:
                order.status = True
                break
        else:
            raise ValueError("Wrong id")
        
    def finished_orders(self):
        return [order for order in self.__tasks if order.status == True]
    
    def unfinished_orders(self):
        return [order for order in self.__tasks if order.status == False]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)


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
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    # for order in orders.all_orders():
    #     print(order)
    # print()
    # for programmer in orders.programmers():
    #     print(programmer)


    # test 3
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    # orders.mark_finished(1)
    # orders.mark_finished(2)
    # for order in orders.all_orders():
    #     print(order)

    
    # test 4
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)
    orders.mark_finished(1)
    orders.mark_finished(2)
    status = orders.status_of_programmer("Adele")
    print(status)