import unittest
import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(absolute_path), "test.txt")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



class TestInsertionSort(unittest.TestCase):

    def test(self):
        with open(file_path, 'r') as f:
            line = f.readline()
            unsorted_str, sorted_str = line.split('    ')
            unsorted_arr = eval(unsorted_str)
            sorted_arr = eval(sorted_str)

        self.assertEqual(insertion_sort(unsorted_arr), sorted_arr)


if __name__ == "__main__":
    unittest.main(verbosity=2)






















# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# def read_list_from_file(filename):
#     with open(filename, 'r') as f:
#         line = f.readline().strip()  # Read the first line and strip any trailing newlines
#         arr = eval(line)  # Convert string representation of list into actual list
#         return arr


# class TestInsertionSort(unittest.TestCase):

#     def test(self):
#         arr_from_file = read_list_from_file('test.txt')
#         sorted_arr = insertion_sort(arr_from_file)
#         self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

# if __name__ == "__main__":
#     unittest.main(verbosity=2)
