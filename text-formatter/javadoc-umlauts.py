def main():
    text = input()
    text = text.replace('Ä', '&Auml;')
    text = text.replace('ä','&auml;')
    text = text.replace('Ö', '&Ouml;')
    text = text.replace('ö','&ouml;')
    text = text.replace('Ü', '&Uuml;')
    text = text.replace('ü','&uuml;')
    print(text.replace('ß', '&szlig;'))
    input()

if __name__ == '__main__':
    main()