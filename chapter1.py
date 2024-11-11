# Emmanuel Cruz 

# Nov 5, 2024

# make a random number between 0 and 1 
# evaluating wehether the number is less than 0.5





import random
import resources

def say_my_name(string):
    random_number = random.random()
    if random_number < 0.5:
        print(f"Hello {string}")
    else:
        print(f"Don't talk to me, {string}")

say_my_name("Emmanuel Cruz")

# Assuming lets_see returns an integer that specifies a threshold
threshold = resources.lets_see(31)

def multiply_if():
    # Generate a list of 10 random numbers between 0 and 100
    random_numbers = [random.randint(0, 100) for _ in range(10)]
    
    # Update the list based on the threshold
    updated_list = [num * 5 if num <= threshold else num for num in random_numbers]
    
    return updated_list

def unique_elements(input_list):
    unique_list = []  # Create an empty list to store unique elements
    for element in input_list:
        if element not in unique_list:  # Check if the element is already in the list
            unique_list.append(element)  # If not, append it to the unique_list
    unique_list.sort()  # Sort the list in ascending order
    return unique_list  # Return the list of unique elements

# Example usage of unique_elements function
test_list = [1, 3, 3, 3, 6, 2, 3, 5]
unique_result = unique_elements(test_list)
print("Unique elements sorted:", unique_result)

# Example usage of multiply_if function
result = multiply_if()
print("Updated list:", result)