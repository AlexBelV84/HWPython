import string

calls = 0

def count_calls():
    global calls
    calls = calls+1


def string_info(Str):
        count_calls()
        return (len(Str),Str.upper(),Str.lower())


def is_contains(string,list_to_search):

    is_get = False
    count_calls()
    string.upper()
    for i in range(len(list_to_search)):
             if list_to_search[i].upper() == string.upper():
                is_get = True
    return is_get

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

