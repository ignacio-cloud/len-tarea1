if __name__ == '__main__':
    lista = []
    verificar = set()
    r = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name, score])
        verificar.add(score)
    mini = sorted(list(verificar))[1]
    r.extend(r[0] for r in lista if mini in r)
    print(*sorted(r), sep='\n')
