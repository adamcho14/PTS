sutaz = {}  # udrziava zoznam a body
juniors = {}  # oznacenie, ci je junior

# nacitame vstup
pwd = input("Zadajte heslo: ")
print("Vase heslo je \'" + pwd + "\'.")


# dekorator, ktory si vyziada a overi heslo pre uskutocnenim prikazu
def password(f):
    global pwd

    def inner_func(*args):
        if pwd == input("Zadajte vase heslo: "):
            f(*args)
        else:
            print("Zle heslo. Zadajte prikaz znova:")
    return inner_func


#funkcie zo zadania. viac v README
@password
def points(name, number):
    if name in sutaz:
        sutaz[name] += number
    else:
        sutaz[name] = number
        juniors[name] = False
    print("Hrac", name, "s poctom bodov", str(sutaz[name] + "."))


@password
def reduce(number):
    for name in sutaz:
        sutaz[name] -= number
    print("Vsetkym hracom odobrate", number, "bodov.")


@password
def junior(name):
    if name in juniors:
        juniors[name] = True
    print("Hrac", name, "oznaceny ako junior.")


def ranking():
    por = 1
    a = sorted(sutaz.keys(), key=sutaz.__getitem__, reverse=True)
    print("Poradie vsetkych hracov:")
    for i in a:
        print(str(por)+".", i, sutaz[i])
        por+=1


def ranking_junior():
    por = 1
    a = sorted(sutaz.keys(), key=sutaz.__getitem__, reverse=True)
    print("Poradie juniorov:")
    for i in a:
        if juniors[i]:
            print(str(por)+".", i, sutaz[i])
            por += 1


@password
def quit():
    print("Program ukonceny.")
    exit(0)


# citanie a vykonavanie jednotlivych prikazov podla vstupu
while True:
    do = input().split(" ")
    if do[0] == 'points':
        points(do[1], int(do[2]))
    elif do[0] == 'reduce':
        reduce(int(do[1]))
    elif do[0] == 'junior':
        junior(do[1])
    elif do[0] == 'ranking':
        if len(do) > 1:
            if do[1] == 'junior':
                ranking_junior()
            else:
                pass
        else:
            ranking()
    elif do[0] == 'quit':
        quit()
