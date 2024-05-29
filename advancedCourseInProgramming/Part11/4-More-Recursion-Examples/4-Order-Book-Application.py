class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False
    
    def is_finished(self):
        return self.finished 
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 
class OrderBook:
    def __init__(self):
        self.__tasks = []
 
    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.__tasks
 
    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))
 
    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)
    
# program
def software_app():
    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")
    print()

    # Initialize the order book
    orders = OrderBook()

    command = int(input("command: "))
    while command != 0:
        if command == 1:
            description = input("description: ")
            programmer_workload = input("programmer and workload estimate: ")
            programmer = programmer_workload.split()[0]
            workload = int(programmer_workload.split()[1])
            orders.add_order(description, programmer, workload)
            print("added!")
            print()
        elif command == 2:
            tasks_finished = orders.finished_orders()
            if len(tasks_finished) == 0:
                print("no finished tasks")
            else:
                for order in tasks_finished:
                    print(order)
            print()
        elif command == 3:
            tasks_finished = orders.unfinished_orders()
            if len(tasks_finished) == 0:
                print("no unfinished tasks")
            else:
                for order in tasks_finished:
                    print(order)
            print()
        elif command == 4:
            order_id = int(input("id: "))
            orders.mark_finished(order_id)
            print("marked as finished")
            print()
        elif command == 5:
            programmers = orders.programmers()
            for programmer in programmers:
                print(programmer)
            print()
        elif command == 6:
            programmer = input("programmer: ")
            programmer_info = orders.status_of_programmer(programmer)
            print(f"tasks: finished {programmer_info[0]} not finished {programmer_info[1]}, hours: done {programmer_info[2]} scheduled {programmer_info[3]}")


        command = int(input("command: "))


software_app()

# test
if __name__ == "__main__":
    pass  # Add your test code here
