def main(): 
    csv = input()
    pattern = csv.replace('"', '')
    print(pattern.replace(',', ''))
    input()

if __name__ == '__main__':
    main()