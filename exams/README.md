# Final exam

## Finalità

Attraverso l'esercitazione finale l'allievo è chiamato a confrontarsi con **un lavoro di modellazione digitale di media
complessità** teso a mostrare i saperi acquisiti e le competenze maturate dallo studente durante il corso di
*Strumenti di modellazione dello spazio*.

In particolare lo studente dovrà dimostrare di possedere la capacità di **riprodurre tridimensionalmente uno spazio
progettato** rispettando i principi di **correttezza topologica** e le **prassi operative della modellazione mesh**.

## Tema del lavoro

L'oggetto dell'esercitazione consiste nella **modellazione di un interno architettonico reale** di recente
realizzazione e liberamente scelto dallo studente.   
L'ambiente deve essere **parte di un'architettura pubblicata nel 2018 (o successivamente) dal sito [_archdaily.com_](http://archdaily.com/)**
ed essere **sufficientemente documentato** da foto e disegni.

La scelta dell'ambiente da modellare dovrà essere **sottoposta preventivamente al docente affinché** venga verificata
la fattibilità del lavoro proposto, la coerenza con i temi trattati durante il corso e che il tema **non sia stato già
scelto da altri studenti**.   
Per proporre il tema scelto seguire le indicazioni riportate nella [pagina dedicata del corso su BeeP](https://beep.metid.polimi.it/web/2018-19-strumenti-di-modellazione-dello-spazio-marco-ferrara-/wiki/-/wiki/Main/Scelta+del+tema+d%27esame?&#p_36).

## Elaborati richiesti e modalità di consegna

Il lavoro è **individuale**.

L'ambiente dovrà essere rappresentato attraverso **due rendering monomaterici bianchi** che ricalchino,
nell'inquadratura e nei contenuti, **due fotografie esistenti dello spazio scelto**.
Al fine di garantire la leggibilità del modello è necessario che:

- lo sviluppo volumetrico del modello sia suggerito attraverso l'utilizzo di tecniche di **_ambient occlusion_**
evitando l'uso di sorgenti luminose (se non necessarie alla comprensione dello spazio)
- la **maglia topologica** sia resa evidente attraverso la **rappresentazione con tratto nero di tutti i bordi** del modello

Gli elaborati da produrre sono:

- i **due rendering monomaterici** sopra indicati: le due immagini dovranno rispettare il rapporto delle fotografie
usate come riferimento ed il più lungo dei due lati deve misurare **3508 px**. Dovranno essere salvate in **formato .png**
in file nominati secondo la forma **NUMEROMATRICOLA-1.png** e **NUMEROMATRICOLA-2.png**
- il **modello tridimensionale dell'ambiente** attraverso cui sono stati prodotti i due rendering: il file dovrà
essere salvato in **formato .obj** e nominato secondo la forma **NUMEROMATRICOLA.obj**. Nel caso in cui i due rendering rappresentassero due ambienti differenti è possibile produrre due diversi file obj denominati secondo la forma **NUMEROMATRICOLA-1.obj** e **NUMEROMATRICOLA-2.obj**

I due rendering ed il modello dovranno, inoltre, essere consegnati anche in **versione "low poly"** attraverso la
disattivazione dell'algoritmo di suddivisione. I file prodotti per la versione "low poly" dovranno mantenere le
stesse caratteristiche dei corrispettivi ad alta densità ed essere nominati secondo la forma:

- **NUMEROMATRICOLA-1-LP.png**
- **NUMEROMATRICOLA-2-LP.png**
- **NUMEROMATRICOLA-LP.obj** (*NUMEROMATRICOLA-1-LP.obj* e *NUMEROMATRICOLA-2-LP.obj* nel caso di ambienti separati)

Le **4 immagini png** prodotte dovranno essere **caricate nella cartella _exams_ del proprio repository _github_** ed
inoltrate al repository del corso tramite **_pull request_** entro i termini indicati dal documento relativo alle
modalità d'esame pubblicato sulla pagina _BeeP_ del corso.
I **modelli obj** dovranno invece essere **pubblicati sulla piattaforma _Sketchfab_** (https://sketchfab.com/)
attraverso l'attivazione di un account personale il cui indirizzo dovrà essere riportato in fase di scelta del tema
sulla pagina dedicata di BeeP.    
I 2 modelli dovranno essere **liberamente scaricabili** (vedi [indicazioni
relative](https://help.sketchfab.com/hc/en-us/articles/201368589-Downloading-Models#Allowing_Users_to_Download))
e non superare la dimensione di 50MB ciascuno.   
L'utilizzo della piattaforma Sketchfab è totalmente gratuito.

## Criteri di valutazione

**La valutazione del lavoro verrà effettuata esclusivamente sulla base dei 2 rendering richiesti**
(la consegna dei modelli 3d ha solo funzione di verifica ed analisi).
Si consiglia pertanto di concentrare la propria attenzione principalmente su ciò che risulta effettivamente
visibile nelle due foto.

Il modello prodotto per l'esercitazione finale verrà valutato secondo i seguenti criteri di giudizio:

- **completezza e fedeltà** rispetto allo spazio rappresentato ed all'inquadratura della foto di riferimento
- **correttezza topologica** della versione "low poly"\*

>\* Tutte le geometrie devono essere _semi-regular quad meshes_

**La somma delle valutazioni** ottenute per l'**esercitazione finale** e per le due **prove ex tempore** del
18.10 e 29.11 (ed eventuale recupero) costituirà **la valutazione finale del corso** di
_Strumenti di modellazione dello spazio_.   

