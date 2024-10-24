import data
import hw1
import unittest
from data import Book
from data import Employee


# Write your test cases for each part below.

class TestCases(unittest.TestCase):

    # Part 1

    def test_vowel_count(self):
        input ='hello'
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected,result)

    def test_vowel_count_2(self):
        input = 'bruh'
        result = hw1.vowel_count(input)
        expected = 1
        self.assertEqual(expected, result)


    # Part 2
    def test_short_lists_1(self):
        input = [(1,2,3),(2,3),(43,22,11),[1],(2,2)]
        result = hw1.short_lists(input)
        expected = [(2,3),(2,2)]
        self.assertEqual(expected,result)

    def test_short_list_2(self):
        input = [(1,2),[1],(-1,-2),[333333333],(22,11)]
        result = hw1.short_lists(input)
        expected = [(1,2),(-1,-2),(22,11)]
        self.assertEqual(expected,result)


    # Part 3

    def test_ascending_pairs_1(self):
        input = [[1, 2], [1], [-1, -2],[333333333],[22, 11]]
        result = hw1.ascending_pairs(input)
        expected = [[2, 1], [-1, -2], [22, 11]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input = [[4, 3], [1], [-4, -2],[333333333],[2, 11]]
        result = hw1.ascending_pairs(input)
        expected = [[4, 3], [-2, -4], [11, 2]]
        self.assertEqual(expected, result)



    # Part 4

    def test_add_prices_1(self):
        result = hw1.add_prices(1, 50)
        expected = data.Price(1, 50)
        self.assertEqual(result, expected)

    def test_add_prices_2(self):
        result = hw1.add_prices(2, 150)
        expected = data.Price(3, 50)
        self.assertEqual(result, expected)

    # Part 5

    def test_rectangle_area(self):
        input = data.Rectangle(data.Point(1, 4), data.Point(4, 1))
        result = hw1.rectangle_area(input)
        expected = 9
        self.assertEqual(result, expected)

    def test_rectangle_area_2(self):
        input = data.Rectangle(data.Point(2, 5), data.Point(5, 3))
        result = hw1.rectangle_area(input)
        expected = 6
        self.assertEqual(result, expected)




    # Part 6
    def test_books_by_author_1(self):

        books = [
            Book(["Author A"], "The"),
            Book(["Author B"], "Book"),
            Book(["Author A"], "Of"),
            Book(["Author C"], "Life"),
            Book(["Author A", "Author B"], "Collaboration"),
        ]

        result = hw1.books_by_author("Author A", books)
        expected_titles = ["The", "Of", "Collaboration"]
        self.assertEqual([book.title for book in result], expected_titles)


    def test_books_by_author_2(self):

        books = [
            Book(["Author V"], "The"),
            Book(["Author B"], "Book"),
            Book(["Author C"], "Of"),
            Book(["Author C"], "Life"),
            Book(["Author D", "Author B"], "Collaboration"),
        ]

        result = hw1.books_by_author("Author A", books)
        expected_titles = []
        self.assertEqual([book.title for book in result], expected_titles)

    # Part 8

    def test_below_pay_average(self):
        employees = [
            Employee("Alice", 50000),
            Employee("Bob", 60000),
            Employee("Charlie", 40000),
            Employee("David", 70000),
            Employee("Eve", 55000)
        ]

        result = hw1.below_pay_average(employees)
        expected_names = ["Alice","Charlie"]
        self.assertEqual(result, expected_names)

    def test_below_pay_average_2(self):
        employees = [
            Employee("Alice", 60000),
            Employee("Bob", 60000),
            Employee("Charlie", 60000),
            Employee("David", 60000),
            Employee("Eve", 60000)
        ]

        result = hw1.below_pay_average(employees)
        expected_names = []
        self.assertEqual(result, expected_names)




if __name__ == '__main__':
    unittest.main()
