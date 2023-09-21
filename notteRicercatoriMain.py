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
        notteRicercatori.drawTraceAndPlay(xs, ys, tots, clusterType, guessed)
        if guessed[0]:
            print("Indovinato!")
            punteggio += 1
        else:
            print("Errore")
            errors += 1
    if punteggio == 10:
        notteRicercatori.won()
    if errors == 3:
        notteRicercatori.lost()




#     # Inizia un nuovo cluster
#     if line.startswith("# Cluster"):
#         # Salva il cluster "vecchio"
#         if len(clusterLines) > minClusterLen:
#             saveCluster(totMatrix, clusterLines, clusterFile, numcluster)
#         # Azzera la lista
#         clusterLines = []
#         numcluster += 1
#         # Riparte
#         continue

#     line = line.split()

#     # Riga di header
#     if line[0] == "X":
#         continue

#     # Aggiunge una lista con: X, Y, ToT
#     clusterLines.append([int(line[1]), int(line[2]), float(line[4])])

# # Salva l'ultimo cluster
# saveCluster(totMatrix, clusterLines, clusterFile, numcluster)

# clusterFile.close()
# f.close()
