# Emmanuel Cruz 

# Nov 5, 2024

 #  # Define the range

    


def lets_see(number):
    lower_limit = 30
    upper_limit = lower_limit + 10
    if lower_limit <= number <= upper_limit:
        print(f"{number} is in the range of {lower_limit} to {upper_limit}.")
        return True
    else:
        print(f"{number} is not in the range of {lower_limit} to {upper_limit}.")
        return False



# if __name__ == "__main__":
#    print(a_num_func())


def main():
    print("this only happens when I run the file directly")


print("I will always get printed")

if __name__ == " __main__":
    main()