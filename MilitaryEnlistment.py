#Military Enlistment
birth_year = int(input('Enter your birth year:\n'))
enlistment_year = int(input('Enter the current year:\n'))
age = enlistment_year - birth_year
adult = 18

if age == adult:
	print('It is time for you to do your military enlistment!\n')
elif age < adult:
	print(f'You have {adult-age} years left until you enlist!\n')
elif age > adult:
	print(f'You should have enlisted {age-adult} years ago!\n')