import notteRicercatori


# Main
punteggio = 0
errors = 0
clusterFile = open("clusterFile.dat", "r")
clusterType = ""

for line in clusterFile.readlines():
    xs = []
    ys = []
    tots = []
    guessed = [False]
    # Righe con l'etichetta
    if not line.startswith('['):
        clusterType = line.strip()
    # Righe con i dati del cluster
    else:
        points = line.strip()[1:-1]
        # Per tutti i punti del cluster
        for point in points.split(']'):
            if point == '':
                break
            point = point.split('[')[1]
            (x, y, tot) = point.split(',')
            xs.append(int(x))
            ys.append(int(y))
            tots.append(float(tot))
        # xs = tutte le x dei punti del cluster
        # ys = tutte le y dei punti del cluster
        # tots = tutti i tot dei punti del cluster
        guessed = notteRicercatori.drawTraceAndPlay(xs, ys, tots, clusterType, guessed)
        if guessed[0]:
            punteggio += 1
        else:
            errors += 1
    if punteggio == 10:
        notteRicercatori.won()
        exit()
    if errors == 3:
        notteRicercatori.lost()
        exit()
