import csv


def process_csv(path):
    with open('Ankieta dla biegaczy.csv') as csv_responses_file:
        csv_reader = csv.reader(csv_responses_file, delimiter=',')
        line_count = 0
        for row in csv_responses_file:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(row)