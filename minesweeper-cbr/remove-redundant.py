from csv import reader


def main():
    with open('C:/Users/Marcel/cbr-workspace/Minesweeper-CBR-Backend/src/main/webapp/WEB-INF/resources/CaseBase.csv') as file:
        data = list(filter(lambda x: 'True' in x, [row for row in file]))
    with open('C:/Users/Marcel/cbr-workspace/Minesweeper-CBR-Backend/src/main/webapp/WEB-INF/resources/CaseBase.csv', 'a') as file:
        file.seek(0)
        file.truncate()
        for row in list(dict.fromkeys(data)):
            file.write(row)

if __name__ == '__main__':
    main()