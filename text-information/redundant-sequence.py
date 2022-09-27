def main():
    print('text:')
    text = input().lower()
    print('\nsequence:')
    sequence = input().lower()
    print('\nresult:')
    print(text.replace(sequence, '\033[91m' + sequence + '\033[0m'))
    print('occurence:', text.count(sequence))

if __name__ == '__main__':
    main()