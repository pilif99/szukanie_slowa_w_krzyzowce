def sprawdz(slowo, kolum_wiers):
    if slowo in ''.join(kolum_wiers):
        print('YES')
        exit()
    elif slowo[::-1] in ''.join(kolum_wiers):
        print('YES')
        exit()
    else:
        return False
    
tablica = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]

slowo = 'kgc'

for i in tablica:
    if sprawdz(slowo, i):
        pass

for i in range(4):
    if sprawdz(slowo, [wiersz[i] for wiersz in tablica]):
        pass
