def Eligible(age):
    # Check if the age is less than 12 or greater than 50 (exclusive)
	if age < 12 or age > 50:
		print('eligible')
	else:
		print('not eligible')

# Declare age variable
age = int(input('Enter your age:\n'))
# Call the CheckAge function
Eligible(age)

