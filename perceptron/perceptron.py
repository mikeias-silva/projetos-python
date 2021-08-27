import csv
# C:\Users\Mikeias\repositories\gitHub\python\perceptron\housevotes84RNAc.csv
# C:\Users\Mikeias\Downloads\housevotes84RNAc.csv
filepath = 'perceptron/housevotes84RNAc.csv'


def lerFile(filepath):
    with open(filepath, encoding='utf-8') as csv_file:
        leitor = csv.reader(csv_file, delimiter=',')
        # csv_reader.__next__()
        for row in leitor:
            print(row)


lerFile(filepath)
