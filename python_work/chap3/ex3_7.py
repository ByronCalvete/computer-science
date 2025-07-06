guest_list = ['lebron james', 'steve jobs', 'nelson mandela']

print(f'Hey {guest_list[0].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[1].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[2].title()}! Do you want to have a dinner with me in Oslo?')
print('---')

guest_not_coming = 'lebron james'
guest_list.remove(guest_not_coming)

print(f'Upps!, at the end {guest_not_coming.title()} not coming to the dinner')
print('---')

guest_list.insert(0, 'luka doncic')

print(f'Hey {guest_list[0].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[1].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[2].title()}! Do you want to have a dinner with me in Oslo?')
print('---')

print('Big news, we have another table for tonight!')
print('---')

guest_list.insert(0, 'tom brady')
guest_list.insert(2, 'mick jagger')
guest_list.append('will guidara')

print(f'Hey {guest_list[0].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[1].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[2].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[3].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[4].title()}! Do you want to have a dinner with me in Oslo?')
print(f'Hey {guest_list[5].title()}! Do you want to have a dinner with me in Oslo?')
print('---')

print('Sorry, I could invite 2 people only!')
print('---')

guest_uninvited = guest_list.pop()
print(f"Sorry {guest_uninvited.title()} I couldn't invite you!")
guest_uninvited = guest_list.pop()
print(f"Sorry {guest_uninvited.title()} I couldn't invite you!")
guest_uninvited = guest_list.pop()
print(f"Sorry {guest_uninvited.title()} I couldn't invite you!")
guest_uninvited = guest_list.pop()
print(f"Sorry {guest_uninvited.title()} I couldn't invite you!")
print('---')

print(f'{guest_list[0].title()} you are still invited')
print(f'{guest_list[1].title()} you are still invited')
print('---')

del guest_list[0]
del guest_list[0]

print(guest_list)
