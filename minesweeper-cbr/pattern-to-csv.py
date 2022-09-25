def main():
    pattern = input()
    csv = ''
    for char in pattern:
        csv += '"' + char + '",'
    print(csv[:-1])
    input()

if __name__ == '__main__':
    main()