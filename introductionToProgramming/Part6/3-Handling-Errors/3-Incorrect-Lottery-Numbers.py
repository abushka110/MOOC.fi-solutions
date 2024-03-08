# solution
def filter_incorrect():
    with open("lottery_numbers.csv") as file_read, open("correct_numbers.csv", "w") as file_write:
        for line in file_read:
            line = line.replace("\n", "")
            week = line.split(" ")[1].split(";")[0]
            try:
                if int(week) < 0:
                    continue
            except:
                continue

            numbers = line.split(" ")[1].split(";")[1].split(",")
            if len(numbers) != 7:
                continue
            valid_numbers = True
            for num in numbers:
                try:
                    num = int(num)
                except ValueError:
                    valid_numbers = False
                    break
                if num < 1 or num > 39:
                    valid_numbers = False
                    break
                if numbers.count(str(num)) > 1:
                    valid_numbers = False
                    break
            if valid_numbers:
                file_write.write(f"{line}\n")
                print(line)
            
# test
if __name__ == "__main__":
    filter_incorrect()
