#question 1
# Given code snippet
a = 10
a = a + 2  # a = 12
print(a * 2)  # This prints 24, but does not affect 'a'
a = 19  # a is now set to 19
print(a + 3)  # This prints 22, but does not affect 'a'
a = a // 2  # Integer division: 19 // 2 = 9

# Final value of a
a


#question 2
print(2+3*6/2)

#question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#question 4
# Define the palindrome function
def palindrome(word):
    return word == word[::-1]

# Given numbers to check
numbers = [
    "2704702208931031198668911301398022074072",
    "7798338247658278460338648728567428338977",
    "4257304920394478392772938744930294037524",
    "0974101607733149676776769413377061014790"
]

# Check which number is NOT a palindrome
not_palindromes = [num for num in numbers if not palindrome(num)]
not_palindromes


#question 5
def find_pattern_occurrences(text):
    count = 0
    words = text.split()  # Split text into words
    for word in words:
        if word.startswith("C") and word.endswith("jeb"):
            count += 1
    return count

# Example usage
sample_text = "Some text with Cxxjeb and Cjeb patterns and some without."
print(find_pattern_occurrences(sample_text))


#question 6
#Explanation:
#Lists are mutable: You can change their contents without creating a new list.
#Strings are immutable: Any modification creates a new string instead of modifying the original.

#Code:
# Mutable example: List
my_list = [1, 2, 3]  # Creating a list
my_list.append(4)     # Adding an element
my_list[0] = 99       # Changing an element
print(my_list)        # Expected Output: [99, 2, 3, 4]


# Immutable example: String
my_string = "Hello"  # Creating a string
try:
    my_string[0] = "J"  # Attempt to modify (this will fail)
except TypeError:
    print("Strings are immutable!")  # Expected Output: "Strings are immutable!"


# Correct way to modify a string (creating a new string)
new_string = "J" + my_string[1:]
print(new_string)  # Expected Output: "Jello"


#question 7
import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Remove odd numbers and double the even numbers
filtered_numbers = []
for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        filtered_numbers.append(num * 2)  # Double the value

# Print the final modified list
print(filtered_numbers)


#question 8
def is_valid_url(url):
    # A valid URL should start with "http://" or "https://"
    if url.startswith("http://") or url.startswith("https://"):
        # A valid URL should have at least one "." after the protocol
        if "." in url[8:] or "." in url[7:]:  # Checking after "http://" (7 chars) or "https://" (8 chars)
            return True
    return False

# Example usage
print(is_valid_url("http://example.com"))  # True
print(is_valid_url("https://google.com"))  # True
print(is_valid_url("ftp://example.com"))   # False (wrong protocol)
print(is_valid_url("example.com"))         # False (missing http/https)


#question 9
def years_passed(birthday):
    # Extract year from the given birthday string "DD-MM-YYYY"
    day, month, year = birthday.split("-")
    year = int(year)  # Convert year to integer

    # Define the current year (2025)
    current_year = 2025

    # Calculate the number of whole years passed
    whole_years = current_year - year - 1  # Exclude birth year and current year

    # Return total number of days (whole years * 365)
    return whole_years * 365


# Example usage
print(years_passed("21-03-2005"))  # Output: Number of days passed since 2005, excluding birth and current year
