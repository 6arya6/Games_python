import csv

grade = []
credits = []

with open('grades.csv') as grades:
    csv_reader = csv.reader(grades, delimiter=',')
    count = 0
    for row in csv_reader:
        if count == 0:
            count += 1
        elif row[3] != '-':
            grade.append(int(row[3]))
            credits.append(int(row[2]))
            count += 1
    #print(f'Processed {line_count} lines.')

sum = 0
total_credits = 0
for i in range(len(grade)):
    sum += grade[i] * credits[i]
    total_credits += credits[i]

avg = sum/total_credits

row = ["#", "AVERAGE", str(total_credits) ,str(round(avg,1)),]

with open('grades.csv', "a") as grades:
    csv_writer = csv.writer(grades)
    csv_writer.writerow(row)
    grades.close()
    