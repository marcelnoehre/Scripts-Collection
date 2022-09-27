def main():
    print(input().replace('Ä', '&Auml;').replace('ä','&auml;').replace('Ö', '&Ouml;').replace('ö','&ouml;').replace('Ü', '&Uuml;').replace('ü','&uuml;').replace('ß', '&szlig;'))

if __name__ == '__main__':
    main()