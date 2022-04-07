"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program XX, Part X


Functions could combined and use an bool parameter to determine
whether a list is sorted or if a copy of the list made and the
copy is returned
"""


def my_sort(my_list):
    for target_index in range(0, len(my_list) - 1):
        for i in range(target_index + 1, len(my_list)):
            if my_list[target_index] > my_list[i]:
                temp = my_list[i]
                my_list[i] = my_list[target_index]
                my_list[target_index] = temp

    return my_list

0
def my_sort_copy(my_list):
    new_list = my_list.copy()
    for target_index in range(0, len(new_list) - 1):
        for i in range(target_index + 1, len(new_list)):
            if new_list[target_index] > new_list[i]:
                temp = new_list[i]
                new_list[i] = new_list[target_index]
                new_list[target_index] = temp

    return new_list


def main():
    some_list = ["a", "c", "F", "h", "L", "G", "Z", "y"]
    # my_sort(some_list)
    new_list = my_sort_copy(some_list)
    print(some_list)
    print(new_list)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.
