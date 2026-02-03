# Gender-Gap-Analysis-ISTAT-vs-Paisa
Analisi comparativa tra la distribuzione occupazionale reale in Italia (dati ISTAT) e i bias di genere nella rappresentazione linguistica delle professioni all'interno del Corpus Paisà.


# Analisi dei Bias di Genere tra Dati ISTAT e Corpus Paisà

Progetto di **Introduzione alla Programmazione** realizzato da **Chiara Mancuso**.

## Obiettivo della Ricerca
Il progetto analizza il rapporto tra la realtà occupazionale italiana e la sua rappresentazione linguistica, con un focus sulle disparità di genere. La domanda di ricerca è: il linguaggio scritto riflette la distribuzione reale dell'occupazione o mostra dei bias di genere?

## Metodologia
Il lavoro si articola in tre fasi principali:
1. **Analisi ISTAT:** Studio della distribuzione occupazionale per genere in 7 settori chiave (Sanità, Ricerca, Istruzione, ecc.) tra il 2012 e il 2017.
2. **Analisi Linguistica (Corpus Paisà):** Estrazione e quantificazione delle professioni nel corpus Paisà tramite espressioni regolari e euristiche personalizzate, distinguendo il genere grammaticale.
3. **Comparazione:** Confronto tra i valori di gender gap reali e quelli linguistici per evidenziare eventuali discrepanze.

## Gestione dei Dati
Il progetto utilizza il **Corpus Paisà** per l'analisi linguistica. A causa delle dimensioni elevate (>100MB), il file grezzo non è presente in questo repository.

* **Dataset Grezzo:** È possibile scaricarlo da [questo link su Google Drive](https://drive.google.com/file/d/1e77ZmvziskUIFKFIXA_2ft9kDdIVUG1f/view?usp=sharing).
* **Dataset Pulito:** Per permettere l'esecuzione immediata delle analisi successive, il file `paisa_pulito.csv` (già normalizzato) è incluso nella cartella `output_progetto/df_puliti/`.

## Setup per l'esecuzione
Per riprodurre l'analisi completa (dalla normalizzazione del testo alla comparazione finale):

1. **Dataset ISTAT:** Il file è già presente in `data/istat/dataset`.
2. **Corpus Paisà:** - Scarica il file originale dal link Drive indicato sopra.
   - Posiziona il file scaricato all'interno della cartella `data/paisa/`.
3. **Esecuzione:** Apri il notebook `Progetto.ipynb`. Il codice caricherà automaticamente i moduli da `Moduli/` e i dati dalle rispettive cartelle.

## Risultati Principali
Dall'analisi emerge che il **Corpus Paisà tende a sovrastimare la presenza maschile** rispetto ai dati ufficiali ISTAT, specialmente nei settori dove le donne rappresentano la maggioranza reale. Ciò suggerisce la persistenza di bias culturali che privilegiano le forme maschili nel discorso scritto.

## Tecnologie Utilizzate
* **Linguaggio:** Python
* **Librerie:** Pandas, Matplotlib, Seaborn, Regex (re)
* **Approccio:** Pipeline modulare con classi e funzioni personalizzate per la normalizzazione del testo e l'allineamento dei dati.

---
*Per i dettagli completi sulla pipeline e sui grafici prodotti, consultare la [Relazione Integrale](./Relazione_Chiara_Mancuso.pdf).*
