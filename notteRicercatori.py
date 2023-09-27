import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
from time import sleep

btnLeft = 0.02
btnRight = 0.72
btnBottom = 0.12
btnTop = 0.52
btnW = 0.25
btnH = 0.35

def won():
    photo = np.genfromtxt("haiVinto.txt")
    plt.imshow(photo)
    plt.show()

def lost():
    photo = np.genfromtxt("haiPerso.txt")
    plt.imshow(photo)
    plt.show()
    
def checkSolution(fig, corr, err, clusterType, guess, guessed):
    def clickedButton(event):
        if clusterType == guess:
            corr.set_visible(True)
            fig.canvas.draw()
            plt.pause(1.5)
            guessed[0] = True
        else:
            err.set_visible(True)
            fig.canvas.draw()
            plt.pause(1.5)
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
    clusterHeight = max(X) - min(X) + 10
    clusterWidth = max(Y) - min(Y) + 10

    # Normalizza X e Y
    X = np.array(X) - min(X) + 5
    Y = np.array(Y) - min(Y) + 5

    clusterMatrix = np.zeros(shape=(clusterHeight, clusterWidth))
    for (x, y, t) in zip(X, Y, tot):
        clusterMatrix[x][y] += t

    # plt.xticks(range(-2, max(X)+10))
    # plt.yticks(range(-2, max(Y)+10))
    fig, (ax) = plt.subplots(1, 1)
    fig.set_figwidth(10)
    fig.set_figheight(5)

    ax.imshow(clusterMatrix / max(tot) * 10, cmap=plt.cm.Reds)
    corr = plt.text(1.2, 1, "Corretto!", fontsize=20)
    err = plt.text(1.2, 1, "Errato!", fontsize=20)
    corr.set_visible(False)
    err.set_visible(False)

    btnElectron = plt.axes([btnLeft, btnTop, btnW, btnH])
    elettrone = Button(btnElectron, 'Elettrone', color="springgreen")
    elettrone.label.set_fontsize(25)
    elettrone.on_clicked(checkSolution(fig, corr, err, clusterType, "Electron", guessed))

    btnMuon = plt.axes([btnLeft, btnBottom, btnW, btnH])
    muone = Button(btnMuon, 'Muone', color="cornflowerblue")
    muone.label.set_fontsize(25)
    muone.on_clicked(checkSolution(fig, corr, err, clusterType, "Muon", guessed))

    btnPhoton = plt.axes([btnRight, btnTop, btnW, btnH])
    fotone = Button(btnPhoton, 'Fotone', color="gold")
    fotone.label.set_fontsize(25)
    fotone.on_clicked(checkSolution(fig, corr, err, clusterType, "Photon", guessed))

    btnAlpha = plt.axes([btnRight, btnBottom, btnW, btnH])
    alpha = Button(btnAlpha, 'Alpha', color="orangered")
    alpha.label.set_fontsize(25)
    alpha.on_clicked(checkSolution(fig, corr, err, clusterType, "Alpha", guessed))

    btnExit = plt.axes([btnRight, btnBottom - 0.09, 0.08, 0.08])
    exit = Button(btnExit, 'Exit', color="grey")
    exit.label.set_fontsize(20)
    exit.on_clicked(exitFunct())

    plt.show()

    return guessed