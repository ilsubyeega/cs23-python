student0_name = input('Student 0 Name: ').strip()
student0_score = int(input('Student 0 Score: '))
student1_name = input('Student 1 Name: ').strip()
student1_score = int(input('Student 1 Score: '))

print(f'{student0_name:>10} : {"*" * (student0_score // 10)}({student0_score})')
print(f'{student1_name:>10} : {"*" * (student1_score // 10)}({student1_score})')
