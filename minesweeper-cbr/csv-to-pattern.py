def main(): 
    csv = input()
    print(csv.replace('"', '').replace(',', ''))
    input()

if __name__ == '__main__':
    main()