import csv

with open ('scores.csv')as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

with open('scores.csv', 'r') as file:
    
    next(reader)  # Skip the header row
    student_count = sum(1 for row in reader)
    print(student_count)

