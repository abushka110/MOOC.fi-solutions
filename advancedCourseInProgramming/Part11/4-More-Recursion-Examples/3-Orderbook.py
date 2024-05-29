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

# test
if __name__ == "__main__":
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)
