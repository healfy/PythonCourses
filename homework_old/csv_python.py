import csv

if __name__ == '__main__':
    with open('lesson5_2.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        data = [
            ['Column 1', 'Column 2', 'Column 3'],
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        for line in data:
            writer.writerow(line)
