def checkMagazine(magazine, note):
    note_numbers = {}
    for word in note:
        if word in note_numbers:
            note_numbers[word] += 1
        else:
            note_numbers[word] = 1
    magazine_numbers = {}
    for word in magazine:
        if word in magazine_numbers:
            magazine_numbers[word] += 1
        else:
            magazine_numbers[word] = 1
    flag = True
    for word in note_numbers:
        if word not in magazine_numbers:
            flag = False
            break
        elif note_numbers[word] > magazine_numbers[word]:
            flag = False
            break
    print()
    if flag is True:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)