import datetime

def is_it_valid(pic: str) -> bool:
    # Check if the length of the PIC is correct
    if len(pic) != 11:
        return False

    control_characters = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    day, month, year, century_marker, identifier, control_char = pic[:2], pic[2:4], pic[4:6], pic[6], pic[7:10], pic[10]

    # Check if the date is valid
    try:
        if century_marker == '+':
            year = '18' + year
        elif century_marker == '-':
            year = '19' + year
        elif century_marker == 'A':
            year = '20' + year
        else:
            return False
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False

    # Check if the control character is valid
    remainder = int(day + month + year[-2:] + identifier) % 31
    if control_characters[remainder] != control_char:
        return False

    return True


# test
if __name__ == "__main__":
    print("correct:")
    print(is_it_valid("050827-906F")) # True
    print(is_it_valid("120488+246L")) # True
    print(is_it_valid("310823A9877")) # True
    print()
    print("day false:")
    print(is_it_valid("000827-906F")) # False
    print(is_it_valid("500827-906F")) # False
    print()
    print("month false:")
    print(is_it_valid("315523A9877")) # False
    print(is_it_valid("310023A9877")) # False
    print()
    print("year false:")
    print(is_it_valid("12040kA246L")) # False
    print()
    print("Century marker false:")
    print(is_it_valid("120423k246L")) # False
    print()
    print("control character false")
    print(is_it_valid("310823A987l")) # False
