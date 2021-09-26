"""September 26th, 2021"""

from typing import Any, List


def main():
    """executes the print module"""

    items: List[int] = [1, 2, 3, 4, 5]
    items_string: list = ["1", "2", "3"]

    values: tuple[Any] = ("Christien", "Python", 6)

    # 0. 
    # print(items)

    # print(f"{items}")

    # for item in items:
    #     print(item)

    # 1. separator (* == destructuring list.)
    # print(*items, sep= ", ")

    # 2. join
    # print("Is a valid number \n".join(map(str, items)))

    # 3. Special characters
    print("Employee %s \nWorks as a %s Developer \nAnd is %d feet tall." % values)

    # %d number
    # %s string
    # %g general number
    # %f float


    
if __name__ == '__main__':
    main()


















    