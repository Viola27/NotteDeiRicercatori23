import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

btnBottom = 0.02
btnW = 0.08
btnH = 0.06

def won():
    None

def lost():
    None
    
def checkSolution(clusterType, guess, guessed):
    def clickedButton(event):
        if clusterType == guess:
            print("True")
            guessed[0] = True
        else:
            guessed[0] = False
        plt.close()
    return clickedButton

def exitFunct():
    def exitClicked(event):
        plt.close()
        exit()
    return exitClicked

def drawTraceAndPlay(X, Y, tot, clusterType, guessed):
    guessed = np.array([False], dtype=bool)
    clusterHeight = max(X) - min(X) + 20
    clusterWidth = max(Y) - min(Y) + 20

    # Normalizza X e Y
    X = np.array(X) - min(X) + 5
    Y = np.array(Y) - min(Y) + 5

    clusterMatrix = np.zeros(shape=(clusterHeight, clusterWidth))
    for (x, y, t) in zip(X, Y, tot):
        clusterMatrix[x+4][y+4] += t

    # plt.xticks(range(-2, max(X)+10))
    # plt.yticks(range(-2, max(Y)+10))
    fig, (ax) = plt.subplots(1, 1)
    fig.set_figwidth(10)
    fig.set_figheight(5)

    ax.imshow(clusterMatrix / max(tot) * 10, cmap=plt.cm.Reds)

    btnElectron = plt.axes([0.05, btnBottom, btnW, btnH])
    elettrone = Button(btnElectron, 'Elettrone', color="orange")
    elettrone.on_clicked(checkSolution(clusterType, "Electron", guessed))

    btnMuon = plt.axes([0.15, btnBottom, btnW, btnH])
    muone = Button(btnMuon, 'Muone', color="magenta")
    muone.on_clicked(checkSolution(clusterType, "Muon", guessed))

    btnPhoton = plt.axes([0.25, btnBottom, btnW, btnH])
    fotone = Button(btnPhoton, 'Fotone', color="yellow")
    fotone.on_clicked(checkSolution(clusterType, "Photon", guessed))

    btnAlpha = plt.axes([0.35, btnBottom, btnW, btnH])
    alpha = Button(btnAlpha, 'Alpha', color="blue")
    alpha.on_clicked(checkSolution(clusterType, "Alpha", guessed))

    btnExit = plt.axes([0.65, btnBottom, btnW, btnH])
    exit = Button(btnExit, 'Exit', color="white")
    exit.on_clicked(exitFunct())

    plt.show()
#    return guessed