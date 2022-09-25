from csv import reader

def main():
    with open('C:/Users/Marcel/cbr-workspace/Minesweeper-CBR-Backend/src/main/webapp/WEB-INF/resources/CaseBase.csv') as file:
        csv_reader = reader(file)
        if next(csv_reader) != None:
            casebase = []
            for row in csv_reader:
                casebase.append(row)
    print([x for n, x in enumerate(casebase) if x in casebase[:n]])

if __name__ == '__main__':
    main()