def check_vowels():
    txt = input("Ingresa algo: ")

    a = ("a" in txt or "A" in txt)
    b = ("e" in txt or "E" in txt)
    c = ("i" in txt or "I" in txt)
    d = ("o" in txt or "O" in txt)
    e = ("u" in txt or "U" in txt)
    print(f'\n Contiene a: {a} \n Contiene e: {b} \n Contiene i: {c} \n Contiene o: {d} \n Contiene U: {e}')
check_vowels()
