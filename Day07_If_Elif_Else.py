# Structure

# if condition1:
#    code

#elif condition2:
#    code

#elif condition3:
#    code

#else:
#   code

# Example 1

marks = int(input("Enter your marks : "))
if marks >= 90:
    print("Grade A")
elif marks >=70:
    print ("Grade B")
elif marks >=50:
    print("Grade c")
else:
    print("Fail")

# Example 2

test_results = input("Enter you results: ")
if test_results == "PASS":
    print("Test Passed")
elif test_results == "FAIL":
    print("Test Failed")
elif test_results == "SKIP":
    print("Test Skipped")
else:
    print("Invalid results")

# Example 3

Salary = 60000
if Salary >= 100000:
    print("High")
elif Salary >= 50000:
    print("Medium")
elif Salary >= 30000:
    print("Low")
else:
    print("Lowest")
