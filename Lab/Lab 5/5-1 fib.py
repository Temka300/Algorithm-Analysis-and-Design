import unittest

def fibonacci(n, cache=None):
    # Initialize cache if not provided
    if cache is None:
        cache = {}
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Check if result is in the cache
    if n in cache:
        return cache[n]
    
    # Otherwise, calculate the Fibonacci number and store it in the cache
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    
    return cache[n]


# class TestInsertionSort(unittest.TestCase):

#     def test(self):
#         with open("Algorithm\\LAB\\test.txt", 'r') as f:
#             line = f.readline()
#             unsorted_str, sorted_str = line.split('    ')
#             unsorted_arr = eval(unsorted_str)
#             sorted_arr = eval(sorted_str)

#         self.assertEqual(insertion_sort(unsorted_arr), sorted_arr)


# if __name__ == "__main__":
#     unittest.main(verbosity=2)


class TestFibonacci(unittest.TestCase):
    def test(self):
        with open("Algorithm\\LAB\\5-1.txt", 'r') as f:
            line = f.readline()
            input, output = line.split(',')
            input_arr = eval(input)
            output_arr = eval(output)

        self.assertEqual(fibonacci(input_arr), output_arr)    


# Run the unit tests
if __name__ == "__main__":
    unittest.main()
