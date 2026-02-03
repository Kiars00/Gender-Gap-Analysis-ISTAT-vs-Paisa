import re
from collections import Counter

#===========================================================================================================================================================

def normalize(text, stopwords):  #Funzione per normalizzare: prende un testo e un file txt contenente le stopwords
    text = text.lower() #Rendo il testo tutto minuscolo
 
    text = re.sub(r"[’']", " ", text) #Sostituisco apostrofi con spazi
    
    text = re.sub(r"[^\w\s]", " ", text) #Sostituisco punteggiatura e simboli speciali con spazi
     
    text = text.strip() #Tolgo spazi all’inizio e alla fine
    
    tokens = text.split() #Divido in parole: tokenizzazione base
    
    tokens = [t for t in tokens if t not in stopwords] #Rimuovo stopwords
    
    return ' '.join(tokens) #Ritorno il testo “pulito” ricomposto in stringa

#===============================================================================================================================================================

def assegna_categoria(url,categorie_url):  #funzione per assegnare una categoria a partire da url
    for categoria, pattern in categorie_url.items():  #itero su tutte le coppie
        if re.search(pattern, url): #verifica se il pattern ricercato è presente
            return categoria
    return "altro"

#===============================================================================================================================================================

def stima_genere_solo_suffisso(parola):  #Funzione per stimare il genere grammaticale di una parola, basandosi solo sul suffisso
    #parola = parola.lower()
    suffissi_f = ['essa', 'trice', 'trici', 'esse', 'iera', 'a', 'ghe', 'che', 'ata', 'ate', 'stre']  #Definisco suffissi maschili e femminili
    suffissi_m = ['o','tore', 'iere', 'ico', 'ogo', 'tori', 'ghi', 'ici', 'ieri', 'ore', 'stri']
    
    if any(parola.endswith(suf) for suf in suffissi_f):  #se la parola termina in un suffissi_f allora è femminile, altrimenti maschile
        return 'femminile'
    elif any(parola.endswith(suf) for suf in suffissi_m):
        return 'maschile'
    else:
        return None

#===============================================================================================================================================================

def conta_settori_per_genere(df):  #Funzione per contare i settori divisi per genere delle professioni associate. Prende in input un dataframe
    conteggi = {} #dizionario per salvare i conteggi

    for i in range(len(df)):  #ciclo su tutta la lunghezza del dataframe di input, tramite l'indice
        settori = df.at[i, 'settori_estratti']  #accedo ai valori delle singole righe
        generi = df.at[i, 'generi_professioni']

        if not isinstance(settori, list) or not isinstance(generi, list): #se uno dei due valori non è una lista, salta
            continue

        for j in range(len(settori)):  #per ogni indice nelle liste
            s = settori[j]  #settore corrente
            g = generi[j]  #genere corrente

            if s is not None and g in ['maschile', 'femminile']:  #Se il settore è definito e il genere è maschile o femminile aggiorno il punteggio
                if s not in conteggi:  #se il settore non è ancora nel dizionario, lo inizializzo
                    conteggi[s] = {'maschile': 0, 'femminile': 0}
                
                conteggi[s][g] += 1  #incremento conteggio per settore e genere corrispondente

    return conteggi

#===============================================================================================================================================================

def calcola_gender_gap_settore(dati_settore, anno1=2012, anno2=2017): #Confronta gender gap per settore specifico, usando due anni
    dati_anno1 = dati_settore[dati_settore['Anno'] == anno1] #filtro i dati degli anni
    dati_anno2 = dati_settore[dati_settore['Anno'] == anno2]

    if dati_anno1.empty or dati_anno2.empty:  #Controllo se sono presenti dati per entrambi gli anni
        return None 

    perc_anno1_m = dati_anno1['% Maschi'].iloc[0] #Prendo le percentuali per ogni genere in ogni anno
    perc_anno1_f = dati_anno1['% Femmine'].iloc[0]
    perc_anno2_m = dati_anno2['% Maschi'].iloc[0]
    perc_anno2_f = dati_anno2['% Femmine'].iloc[0]

    gap_anno1 = perc_anno1_m - perc_anno1_f  #calcolo i gender gap per entrambi i generi
    gap_anno2 = perc_anno2_m - perc_anno2_f

    var_gap = gap_anno2 - gap_anno1 #Calcolo la variazione del gap
     
    direzione_gap = "aumentato" if abs(gap_anno2) > abs(gap_anno1) else "diminuito" #Indico la direzione del gap

    return { #output
        '% Maschi ' + str(anno1): round(perc_anno1_m, 2), #percentuali arrotondate a 2 decimali
        '% Femmine ' + str(anno1): round(perc_anno1_f, 2),
        '% Maschi ' + str(anno2): round(perc_anno2_m, 2),
        '% Femmine ' + str(anno2): round(perc_anno2_f, 2),
        'Gender Gap ' + str(anno1): round(gap_anno1, 2),
        'Gender Gap ' + str(anno2): round(gap_anno2, 2),
        'Var Gap (p.p.)': round(var_gap, 2),
        'Direzione Gap': direzione_gap
    }

#===============================================================================================================================================================

def conta_professioni_per_genere(df, col_prof='professioni_estratte', col_gen='generi_professioni'): #Funzione per contare quante volte una professione divisa per genere
    parole_per_genere = {  #dizionario per salvare le professioni in maschili e femminili
        'maschile': [],
        'femminile': []
    }

    for i in range(len(df)):   #ciclo su ogni riga del df, accendendo ad ogni riga per estrarre i dati
        profs = df.at[i, col_prof]
        generi = df.at[i, col_gen]

        if not isinstance(profs, list) or not isinstance(generi, list):  #Se sono liste vuote continua
            continue

        for j in range(len(profs)):  #ciclo su professioni e generi
            prof = profs[j]   #professione
            genere = generi[j]   #genere associato alla professione
            if genere in parole_per_genere:   #se il genere è tra quelli previsti, aggiungo la professione alla lista
                parole_per_genere[genere].append(prof)

    conteggi_per_genere = {} #Dopo aver trovato tutte le professioni, le conto, per genere
    
    for genere, parole in parole_per_genere.items():
        conteggi_per_genere[genere] = Counter(parole)
    
    return conteggi_per_genere
