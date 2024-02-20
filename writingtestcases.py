"""
Test case format:
    def test_<function_name>_<what_youre_testing>():
        # Set up data
        # Line break
        # Call the function
        # Line break
        # Assert the expected results
"""

# "_<function_name>" denotes private function
def _check_arrays_are_equal(output: list, expected: list) -> bool:
    if len(output) != len(expected):
        return False
    for i in range(len(output)):
        if output[i] != expected[i]:
            return False
    return True

def test_sorted_int_list_reversed():
    # Set up data
    test_list = [5,3,4,2,1]
    expected_result = [1,2,3,4,5]

    # Call the function
    result = sorted(test_list)

    # Assert the expected results
    assert _check_arrays_are_equal(result, expected_result)

"""
In an interview, you can do this more informally
(no function name, "print" instead of "assert")
"""

test_list = [5,4,3,2,1]

result = sorted(test_list)

print(result)