"""
Test case format:
    def test_<function_name>_<what_youre_testing>():
        # Set up data
        # Line break
        # Call the function
        # Line break
        # Assert the expected results
"""

def test_len_of_list():
    # Set up data
    test_list = [1, 2, 3, 4, 5]
    expected_result = 5

    # Call the function
    result = len(test_list)

    # Assert the expected results
    assert result == expected_result

"""
In an interview, you can do this more informally
(no function name, "print" instead of "assert")
"""

test_list = [1, 2, 3, 4, 5]

result = len(test_list)

print(result)