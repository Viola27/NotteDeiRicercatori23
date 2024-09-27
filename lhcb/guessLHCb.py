import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button

btnLeft = 0.02
btnBottom = 0.05
btnTop = 0.8
btnW = 0.20
btnH = 0.10

spiegazioni = {
    "VeLo.png": "VErtex LOcator: fornisce\n\
misure estremamente precise\n\
delle coordinate delle particelle\n\
vicino al punto di interazione\n\
dei protoni.", 

    "Rich.png": "Ring-Imaging CHerenkov detector:\n\
misura la massa delle particelle,\n\
permettendone quindi l'identificazione.",

    "Magnet.png": "Magneti: curvano la\n\
traiettoria delle particelle cariche,\n\
in modo da permettere agli altri\n\
rivelatore di misurarne le proprietà\n\
(es. momento, massa, ...)", 

    "Tracker.png": "Tracker: ricostruisce il percorso\n\
delle particelle cariche permettendo\n\
anche di ricostruirne il momento", 

    "Calorimetro.png": "Calorimetri: misurano\n\
l'energia delle particelle attraverso\n\
i fenomeni chiamati 'sciame\n\
elettromagnetico e adronico'", 

    "MuonSystem.png": "Muon System:\n\
discrimina i muoni\n\
dalle altre particelle"
}

filenames = ["VeLo.png", "Rich.png", "Magnet.png", "Tracker.png", "Calorimetro.png", "MuonSystem.png"]

def checkSolution(guess, guessed):
    def clickedButton(event):
        if guessed == guess.strip().split('.')[0]:
            corr = plt.text(-2, 5.0, "Corretto!", fontsize=20, color='green', backgroundcolor='white')
            corr.set_visible(True)
            # fig.canvas.draw()
            plt.pause(1) 
            corr.set_visible(False)
            spiegazione = plt.text(-2, 3.0, spiegazioni[guess], fontsize=15, color='midnightblue', backgroundcolor='white')
            spiegazione.set_visible(True)
            plt.waitforbuttonpress() 
            spiegazione.set_visible(False)
        else:
            err = plt.text(-2, 5.0, "Errato!", fontsize=20, color='red', backgroundcolor='white')
            err.set_visible(True)
            # fig.canvas.draw()
            plt.pause(1.5)
            err.set_visible(False)
        plt.close()
    return clickedButton

while(True):
    for filename in filenames:
        # fig, (ax) = plt.subplots(1, 1)
        img = mpimg.imread(filename)
        imgplot = plt.imshow(img)
        plt.axis('off')

        btnMagnet = plt.axes([btnLeft, btnTop, btnW, btnH])
        magnet = Button(btnMagnet, 'Devia le\nparticelle cariche', color="slategrey")
        magnet.label.set_fontsize(10)
        magnet.on_clicked(checkSolution(filename, "Magnet"))

        btnCal = plt.axes([btnLeft + btnW * 1.5, btnTop, btnW, btnH])
        cal = Button(btnCal, "Misura l'energia\ndelle particelle", color="y")
        cal.label.set_fontsize(10)
        cal.on_clicked(checkSolution(filename, "Calorimetro"))

        btnTT = plt.axes([btnLeft + btnW * 3, btnTop, btnW, btnH])
        tracker = Button(btnTT, 'Rivela momento\ne percorso', color="mediumorchid")
        tracker.label.set_fontsize(10)
        tracker.on_clicked(checkSolution(filename, "Tracker"))

        btnVELO = plt.axes([btnLeft, btnBottom, btnW, btnH])
        velo = Button(btnVELO, 'Rivela i vertici\ndi decadimento', color="deepskyblue")
        velo.label.set_fontsize(10)
        velo.on_clicked(checkSolution(filename, "VeLo"))

        btnMuon = plt.axes([btnLeft + btnW * 1.5, btnBottom, btnW, btnH])
        muon = Button(btnMuon, 'Rivela\ni muoni', color="orange")
        muon.label.set_fontsize(10)
        muon.on_clicked(checkSolution(filename, "MuonSystem"))

        btnRich = plt.axes([btnLeft + btnW * 3, btnBottom, btnW, btnH])
        rich = Button(btnRich, 'Identifica\nle particelle\ncariche', color="springgreen")
        rich.label.set_fontsize(10)
        rich.on_clicked(checkSolution(filename, "Rich"))
        
        
        plt.show()
