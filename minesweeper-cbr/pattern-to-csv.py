def main():
    csv = ''
    for char in input():
        csv += '"' + char + '",'
    print(csv[:-1])

if __name__ == '__main__':
    main()