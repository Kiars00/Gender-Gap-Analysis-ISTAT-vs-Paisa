import re

categorie_url = {
    "wikipedia": r"(?:\b|\.)(wikipedia\.org|wikibooks\.org|wikiversity\.org|wikinews\.org|wikidata\.org)(?:\b|/|$)",
    
    "forum": r"(?:\b|\.)(indymedia\.org|/forum/|/comment(?:o|i)/|/discussione/|/community/|/tips/|comment\.php|boards\.|bbs\.)(?:\b|/|$)",
    
    "blog": r"(?:\b|\.)(blogspot\.com|wordpress\.com|splinder\.com|supereva\.it|ecoblog\.it|tvblog\.it|autoblog\.it|cineblog\.it|motoblog\.it|polisblog\.it|calcioblog\.it|06blog\.it|02blog\.it|travelblog\.it|blogapuntate\.it|queerblog\.it|soundsblog\.it|booksblog\.it|spettegola\.com|glamourage\.it|fashionblog\.it|mobileblog\.it|solotrend\.it|cineblog\.it|clickblog\.it|gdrzine\.com)(?:\b|/|$)",
    
    "news": r"(?:\b|\.)(ansa\.it|repubblica\.it|corriere\.it|ilgiornale\.it|rainews\.it|tgcom\.it|lucacoscioni\.it|ecowebnews\.it|businessonline\.it|webmasterpoint\.org|ninjamarketing\.it|impresalavoro\.eu|melablog\.it|queerblog\.it|calcioblog\.it|motorsportblog\.it|travelblog\.it|cineblog\.it)(?:\b|/|$)",
    
    "blog_femminili": r"(?:\b|\.)(alfemminile\.com|mammafelice\.it|donne\.it|pinkblog\.it|leiweb\.it|donnamoderna\.com|cosmopolitan\.it|grazia\.it|amando\.it|vanityfair\.it)(?:\b|/|$)",
}
#================================================================================================================================================================

settori_regex = {   # \b è per essere sicura che la parola sia una parola intera e non interna ad altre parole
    "SANITÀ E ASSISTENZA SOCIALE": [
        r"medic(?:o|a|i|he)\b",   #medico, medica, medici, mediche; escludo esami medici, visite mediche, medico veterinario
        r"infermier(?:e|a|i)\b",     #infermiere, infermiera, infermieri
        r"psicolog(?:o|a|i|he)\b",       #psicologo, psicologa, psicologhe
        r"chirurg(?:o|a|hi|he)\b"            #chirurgo, chirurga, chirurgi, chirurghe
    ],

    "ESTRAZIONE DI MINERALI DA CAVE E MINIERE": [
        r"minator(?:e|i)\b",      #minatore, minatori
        r"minatric(?:e|i)\b"      #minatrice, minatrici
    ],

    "RICERCA SCIENTIFICA E SVILUPPO": [
        r"ricercator(?:e|i)\b",    #ricercatore, ricercatori
        r"ricercatric(?:e|i)\b",   #ricercatrice, ricercatrici
        r"scienziat(?:o|a|i|e)\b"     #scienziato, scienziata, scienziati, scienziate
    ],

    "ATTIVITÀ EDITORIALI": [  
        r"redattor(?:e|i)\b",     #redattore, redattori
        r"redattric(?:e|i)\b",    #redattrice, redattrici
        r"editor(?:e|i)\b",    #editore, editori
        r"editric(?:e|i)\b",    #editrice, editrici
        r"scrittor(?:e|i)\b",             #scrittore, scrittori
        r"scrittric(?:e|i)\b"     #scrittrice, scrittrici
    ],

    "ATTIVITÀ LEGALI E CONTABILITÀ": [
        r"avvocat(?:o|a|i|e)\b",     #avvocato, avvocata, avvocati, avvocate
        r"avvocatess(?:a|e)\b",    #avvocatessa, avvocatesse
        r"ragionier(?:e|i|a)\b",     #ragioniere, ragionieri, ragioniera
        r"magistrat(?:a|e|o|i)\b"       #magistrata, magistrate, magistrato, magistrati
    ],

    "ISTRUZIONE": [
        r"professor(?:e|i)\b",    #professore, professori
        r"professoress(?:a|e)\b",   #professoressa, professoresse
        r"educator(?:e|i)\b",     #educatore, educatori
        r"educatric(?:e|i)\b",     #educatrice, educatrici
        r"maestr(?:a|e|o|i)"    #maestra, maestre, maestro, maestri; escludendo contesti specifici
    ],

    "ATTIVITÀ IMMOBILIARI": [
        r"intermediar(?:i|o|a)\b",     #intermediari, intermediario, intermediaria
        r"amministrator(?:e|i)\b",     #amministratore, amministratori
        r"amministratric(?:e|i)\b"    #amministratrice, amministratrici
    ]
}
settori_regex_compilati = {            #Creo un nuovo dizionario `settori_regex_compilati` in cui per ogni settore viene associata una lista di pattern regex già compilati (con re.compile)
    settore: [re.compile(pat, re.IGNORECASE) for pat in patterns] 
    for settore, patterns in settori_regex.items()  # Ciclo su ogni coppia (settore, pattern) nel dizionario `settori_regex`.
}
# Questo serve per ottimizzare le ricerche successive, perché compilare le regex una volta sola migliora la performance rispetto a compilarle ad ogni uso: perché l'estrazione dal corpus ha costi computazionali abbastanza alti, infatti ci metteva diverso tempo.

#==========================================================================================================================================================

parole_proibite_per_professione = {  #Creo dizionario con parole proibite per ogni settore, in maniera tale da non includerle nella ricerca e analisi
    "SANITÀ E ASSISTENZA SOCIALE": {
        "medico": ["campo", "famiglia", "esame", "visita", "errore", "veterinario"],
        "medici": ["de", "campi", "esami", "visite", "errori"],
        "medica": ["visita", "rivista"],
        "mediche": ["prestazioni"]
    },
    "ATTIVITÀ EDITORIALI": {
        "editrice": ["casa"],
        "editrici": ["case"]
    },
    "ISTRUZIONE": {
        "maestro": ["musicale", "regia", "arte", "musica", "orchestra", "vessicchio"]
    }
}