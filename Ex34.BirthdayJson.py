## Birthday Json

# Save and reads birthdays to json file

import json

def save_to_file(dictionary):
    with open("birthdays.json", "w") as f:
        json.dump(dictionary, f)
        
def read_from_file():
    with open('birthdays.json', 'r') as f:
        info = json.load(f)
    
    return info


if __name__ == "__main__":
    
    dictionary = {
            'Albert Einstein': '03/14/1879',
            'Benjamin Franklin': '01/17/1706',
            'Ada Lovelace': '12/10/1815'
    }
    
    save_to_file(dictionary)
    birthdays = read_from_file()
       
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)
    
    answer = 'yes'
    
    answer = input('Do you wish to add a person\'s birthday?')
    while answer.lower() == 'yes':
        inp = input('Enter the name of the person\'s birthday you wish to enter:')
        date = input ('Enter their birthday in the format, MM/DD/YEAR:')
        birthdays[inp] = date
        save_to_file(birthdays)
        birthdays = read_from_file()
        
        for name in birthdays:
            print(name)
            
        answer = input('Do you wish to add another person\'s birthday?')
        