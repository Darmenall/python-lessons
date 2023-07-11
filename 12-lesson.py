"""

    Python: 10-lesson

    Avtor: Darmen Allambergenov

    Tema:  san tap oyni

"""









import random


def santap(x=10):
    shama_san = random.randint(1, x)
    print(f"Men 1 den {x} shekem san oyladim. Tawalasizba?", end="")
    shamalar = 0
    while True:
        shamalar += 1
        shama = int(input(">>>"))
        if shama < shama_san:
            print("Ulkenlew san aytin':", end="")
        elif shama > shama_san:
            print("Kichilew san aytin:", end="")
        else:
            print("You win!")
            break

    print(f"Qutliqlayman. {shamalar} marte shama menen towdin'iz!")
    return shamalar


def santap_pc(x=10):
    input(f"1 den {x} shekem san oylan' ha'm qalegen tuymeni basin'. Men tawaman.")
    tomen = 1
    joqari = x
    shamalar = 0
    while True:
        shamalar += 1
        if tomen != joqari:
            shama = random.randint(tomen, joqari)
        else:
            shama = tomen
        juwap = input(
            f"Siz {shama} sonin' oyladin'iz: duris bolsa (t),"
            f"men oylagan san budan ulken bolsa (+), yaki kichi bolsa (-)".lower()
        )
        if juwap == "-":
            joqari = shama - 1
        elif juwap == "+":
            tomen = shama + 1
        else:
            break
    print(f"Men {shamalar} marte shama menen tawdim!")
    return shamalar


def play(x=10):
    jane = True
    while jane:
        shamalar_pc = santap_pc(x)
        shamalar_user = santap(x)

        if shamalar_user > shamalar_pc:
            print(f"Men {shamalar_pc} shama menen tawdim ha'm  uttim!")
        elif shamalar_user < shamalar_pc:
            print(f"Siz {shamalar_user} shama menen tawdin'iz ha'm uttin'iz!")
        else:
            print("Dosliq jen'di!")
        jane = int(input("jane oynaymizba? awa(1)/yaq(0):"))


play()
