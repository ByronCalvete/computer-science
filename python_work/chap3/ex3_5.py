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
