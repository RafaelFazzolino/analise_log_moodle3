import csv


def read_students():
    students = {}
    with open('alunos.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            students[row[0]] = 0
    return students


def print_log_count(students):
    for k, v in students.items():
        print(k + ': ' + str(v))
