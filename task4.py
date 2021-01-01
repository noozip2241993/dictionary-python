"""Write a Python program to check whether a given key already exists in a dictionary."""
def main():
    dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    checking_existence_key(dict1)
def checking_existence_key(dict1):
    if len(dict1) != 0:
        print(f'Key is present in the dictionary')
    else:
        print(f'Key is not present in the dictionary')
main()