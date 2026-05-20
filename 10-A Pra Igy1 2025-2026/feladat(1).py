with open('./iras/keresztnevek.txt', 'w', encoding='utf-8') as nevek:
    a = 0
    while a != 5:
        b = input("Adj meg egy keresztnevet: ")
        print(b , file=nevek)
        a = a + 1