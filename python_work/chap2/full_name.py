# f-commets are the best way to concatenate strings with variables
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name) # ada lovelace

message = f'Hello, {full_name.title()}!'
print(message) # Hello, Ada Lovelace!
