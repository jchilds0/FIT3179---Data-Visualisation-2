import csv

def format_csv(file):
    csv_reader = csv.reader(file)
    lst = [row for row in csv_reader]
    return [[row[0], row[1], row[2], row[3], row[4], row[5], float(row[6]), float(row[7])] for row in lst[1:]]

def split_into_penguins():
    with open("data/adelie_penguin_telemetry.csv", "r") as file:
        adelie_penguin_csv = format_csv(file)
        
        

if __name__ == "__main__":
    split_into_penguins()