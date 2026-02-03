# Gender-Gap-Analysis-ISTAT-vs-Paisa
Analisi comparativa tra la distribuzione occupazionale reale in Italia (dati ISTAT) e i bias di genere nella rappresentazione linguistica delle professioni all'interno del Corpus Paisà.


# Analisi dei Bias di Genere: ISTAT vs. Corpus Paisà

Progetto di **Introduzione alla Programmazione** (a.a. 2024-2025) realizzato da **Chiara Mancuso**.

## Obiettivo della Ricerca
Il progetto analizza il rapporto tra la realtà occupazionale italiana e la sua rappresentazione linguistica, focalizzandosi sulle disparità di genere. 
L'obiettivo è verificare se il linguaggio scritto rifletta la distribuzione reale dell'occupazione o se mostri dei bias di genere che influenzano la percezione delle professioni.

## Metodologia
Il lavoro si articola in tre fasi principali:
1. **Analisi ISTAT:** Studio della distribuzione occupazionale in 7 settori chiave (Sanità, Ricerca, Istruzione, Editoria, Attività di Estrazione Mineraria, Attività Legali e Contabilità, Attività Immobiliari) tra il 2012 e il 2017.
2. **Analisi Linguistica (Corpus Paisà):** Estrazione e quantificazione delle professioni tramite espressioni regolari e euristiche personalizzate, distinguendo il genere grammaticale.
3. **Comparazione:** Confronto tra i valori di gender gap reali e quelli linguistici per evidenziare le discrepanze tra realtà sociale e linguaggio.

## Struttura del Repository
Il lavoro è organizzato in una struttura modulare per garantire leggibilità e riproducibilità:

* **Progetto.ipynb**: Notebook principale con le analisi e le visualizzazioni grafiche.
* **Moduli/**: Contiene gli script Python personalizzati (`euristiche.py`, `mie_funzioni.py`, `classe.py`).
* **output_progetto/**: Cartella dedicata agli output salvati, divisa in sottocartelle per analisi ISTAT, Paisà e comparative.
* **data/**: Cartelle segnaposto per i dataset in ingresso.



## Gestione dei Dati e File Pesanti
A causa delle dimensioni elevate (>100MB), alcuni file non sono inclusi direttamente nel repository:

* **Dataset Grezzo (Corpus Paisà):** Deve essere scaricato da [questo link su Google Drive](https://drive.google.com/file/d/1e77ZmvziskUIFKFIXA_2ft9kDdIVUG1f/view?usp=sharing) e posizionato in `data/paisa/`.
* **Dataset Puliti:** Il file `paisa_pulito.csv` e i DataFrame di analisi vengono generati automaticamente dal codice durante l'esecuzione delle fasi di normalizzazione e analisi.

## Setup per l'esecuzione
Per riprodurre l'analisi completa:
1.  **Dataset ISTAT:** Assicurarsi che i dati siano presenti in `data/istat/`.
2.  **Corpus Paisà:** Scaricare il file grezzo dal link Drive e inserirlo in `data/paisa/`.
3.  **Esecuzione:** Eseguire il notebook `Progetto.ipynb`. La prima fase di normalizzazione creerà automaticamente i file necessari nella cartella `output_progetto/df_puliti/`.

## Risultati Principali
Dall'analisi emerge che il **Corpus Paisà tende a sovrastimare la presenza maschile** rispetto ai dati ufficiali ISTAT, specialmente nei settori a maggioranza femminile. Questo fenomeno riflette la persistenza di bias culturali e linguistici che privilegiano le forme maschili nel discorso scritto.

## Tecnologie Utilizzate
* **Linguaggio:** Python.
* **Librerie:** Pandas, Matplotlib, Seaborn, Regex.
* **Strumenti:** Jupyter Notebook per l'analisi interattiva.

---
*Per un'analisi approfondita della metodologia e dei grafici, consultare la [Relazione Integrale](./Relazione_Chiara_Mancuso.pdf).* 

##  Download Rapido
Se desideri scaricare l'intero progetto pronto all'uso (inclusi i dataset pesanti >100MB e la struttura delle cartelle già configurata), puoi scaricare il pacchetto completo da Google Drive:

> [**Scarica la cartella del progetto da One Drive**](https://liveunibo-my.sharepoint.com/:u:/g/personal/chiara_mancuso5_studio_unibo_it/EY601zz6Rh9As1x2hhGOyjkBP1mPfg2IObVUNZZElVxjLQ?e=7i1Frx)
