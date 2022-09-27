def main():
    text = input()
    print(text.replace('Ä', '&Auml;').replace('ä','&auml;').replace('Ö', '&Ouml;').replace('ö','&ouml;').replace('Ü', '&Uuml;').replace('ü','&uuml;').replace('ß', '&szlig;'))
    input()

if __name__ == '__main__':
    main()