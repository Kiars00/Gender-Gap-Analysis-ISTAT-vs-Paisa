import re
from collections import Counter

class EstrazioneProfessioniSettori:
    def __init__(self, regex_dict, parole_proibite_per_professione=None, finestra=3):  #Inizializzo la classe
        self.regex_dict = regex_dict
        self.parole_proibite_per_professione = parole_proibite_per_professione or {}
        self.finestra = finestra


    def filtra_match_per_contesto(self, testo, match, parole_proibite):  #Funzione per verificare pattern tra parole nel testo e, le parole_proibite, in una finestra di 3 parole (definite in euristiche)
        parole = testo.split() #per sicurezza imposto il testo in minuscolo e lo splitto in tokens
        match = match.lower() #converte la parola da cercare match in minuscolo (per sicurezza)

        for i, p in enumerate(parole): #ciclo su ogni parola del test con indice i
            if p == match: #se la parola corrente è uguale alla parola cercata
                contesto = parole[max(0, i - self.finestra): i] + parole[i + 1: i + 1 + self.finestra] #seleziono le parole prima e dopo il contesto
            
                if any(parola in contesto for parola in parole_proibite): #Verifico se incontro una delle parole proibite: se vero ritorna False, perché non va bene
                    return False
        return True
        

    def estrai_professioni_e_settori(self, testo): #Funzione che prende come argomento: testo, un dizionario di espressioni regolari, il parametro (opzionale) parole_proibite_per_professione (per non avere match sbagliati) e finestra, per il contesto
        professioni_trovate = [] #lista per raccogliere le professioni trovate nel testo
        settori_trovati = set()  #set per i settori trovati nel testo
    

        for settore, patterns in self.regex_dict.items():  #Ciclo su ogni settore i pattern di espressioni regolari
            if settore in self.parole_proibite_per_professione:  #Recupero le parole proibite associate a quel settore e poi professione (essendo un dizionario)(se presenti)
                parole_proibite = self.parole_proibite_per_professione[settore]  #definisco parole_proibite
            else:
                parole_proibite = []  #nessuna parola proibita per settore
        
            for pattern in patterns: #ciclo su ogni espressione regolare per il settore corrente
                    for match_obj in pattern.finditer(testo):  #per avere anche le professioni, ciclo per ogni occorrenza nel pattern
                        match = match_obj.group()  #Estraggo testo corrispondente con match: .grpoup restituisce la stringa esatta
                    
                        if isinstance(parole_proibite, dict) and match in parole_proibite:
                            proibite = parole_proibite[match]  #recupero le parole proibite per quel match
                        else:
                            proibite = []  #nessuna parola proibita per il match corrente
                    
                        if not self.filtra_match_per_contesto(testo, match, proibite):  #se il contesto contiene parole proibite scarto il match
                            continue
                    
                        professioni_trovate.append(match)  #aggiungo le professioni trovate, con tutti i filtri
                     
                        settori_trovati.add(settore)   #aggiungo i settori trovati

        return professioni_trovate, list(settori_trovati)


    def estrai_contesto(self, tokens, parola, finestra=5): #Funzione per estrarre contesti in cui compare una parola (contesto di 5 parole: finestra). Prende token, una parola, e la finestra
        risultati = [] #lista per raccogliere i risultati del ciclo per i contesti trovati
    
        for i, token in enumerate(tokens): 
            if token == parola:  #Calcolo intervallo della finestra intorno ala parola trovata: per prendere parole prima di i e quelle dopo
                start = max(i - finestra, 0)
                end = min(i + finestra + 1, len(tokens))
            
                contesto = " ".join(tokens[start:end]) #Ricostruisce il contesto dai token come stringa 
                risultati.append(contesto) #aggiungo il contesto alla lista dei risultati
    
        return risultati
