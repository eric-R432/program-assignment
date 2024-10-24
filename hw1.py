import data
from data import Price, Rectangle


# Write your functions for each part in the space below.

# Part 1

def vowel_count(s:str):
    tally = 0
    vowels = 'aeiou'
    for vowel in s:
        if vowel in vowels:
            tally += 1
    return tally

# Part 2

def short_lists(big_list:list[list[int]]):
    return [small_list for small_list in big_list if len(small_list) == 2]

# Part 3

def ascending_pairs(big_list: list[list[int]]) -> list[list[int]]:
        result = []
        for small_list in big_list:
            if len(small_list) == 2:
                small_list = sorted(small_list, reverse=True)
                result.append(small_list)
        return result

# Part 4


def add_prices(dollars:int, cents: int ):
    total_cents = dollars * 100 + cents
    total_dollars = total_cents // 100
    left_over = cents % 100
    return Price(total_dollars, left_over)

# Part 5

def rectangle_area(rectangle: Rectangle):
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    area = width * height
    return area


# Part 6
from data import Book
def books_by_author(author_name:str, books:list[Book]):
    return [book for book in books if author_name in book.authors]

#part 8
from data import Employee
def below_pay_average(employees: list[Employee]) -> list[str]:
    if len(employees) == 0:
        return []

    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)
    below_average_employees = [employee.name for employee in employees if employee.pay_rate < average_pay]

    return below_average_employees
