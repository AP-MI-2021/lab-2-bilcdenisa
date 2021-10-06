def is_antipalindrome(n):
    #determina daca un numar este antipalindrom
    #input: n: int
    #output: true-daca n este antipalindrom, false in caz contrar
    if n<=9:
        return True
    cifre_int_lst = []
    while n>0:
        cifre_int_lst.append(n%10)
        n = n//10
    ok = 1
    index = 0
    for i in cifre_int_lst:
        if(i == cifre_int_lst[len(cifre_int_lst)-1-index]):
            ok = 0
        if len(cifre_int_lst) % 2 != 0:
            if (len(cifre_int_lst) - 1 - index) == ((len(cifre_int_lst)) // 2):
                ok = 1
        index = index+1

    if ok == 1:
        return True
    else:
        return False


def get_base_2(n):
    #transforma un numar din baza 10 in baza 2
    #input: n: str
    #output: numar in baza 2:str
    n = int(n)
    rezultat = 0
    putere = 1
    while n!=0:
        rest = n%2
        rezultat = rezultat + rest*putere
        putere = putere*10
        n = n//2
    rezultat = str(rezultat)
    return rezultat

def test_is_antipalindrome():
    assert is_antipalindrome(2) == True
    assert is_antipalindrome(15) == True
    assert is_antipalindrome(121) == False
    assert is_antipalindrome(1234) == True
    assert is_antipalindrome(55) == False
    assert is_antipalindrome(123) == True
    assert is_antipalindrome(2783) == True

def test_get_base_2():
    assert get_base_2(106) == '1101010'
    assert get_base_2(123) == '1111011'
    assert get_base_2(9) == '1001'
    assert get_base_2(333) == '101001101'

def main():
    while True:
        print('1. Determină dacă un număr este antipalindrom')
        print('2. Transforma un numar din baza 10 in baza 2')
        print('x. Iesire din program')
        optiune = input('Alege optiunea')
        if optiune == '1':
            n = int(input('Dati numarul'))
            variabila = is_antipalindrome(n)
            if variabila == True:
                print('Numarul este antipalindrom')
            else:
                print('Numarul nu este antipalindrom')
        elif optiune == '2':
            n = input('Dati numar in baza 10')
            n_baza_2 = get_base_2(n)
            print('Numarul in baza 2 este',n_baza_2)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')

test_get_base_2()
test_is_antipalindrome()
main()
