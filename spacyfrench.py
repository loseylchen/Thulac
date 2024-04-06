##命令终端：cd /Users/lianchen/Documents    python3 spacyfrench.py


import spacy

nlp = spacy.load("fr_core_news_lg")#modèle de langue
#sentence="作为语言而言，为世界使用人数最多的语言，目前世界有五分之一人口做为母语."

f=open("texte_fr.txt","r")#fichier d'entrée
f_out=open("text_fr_tok_spacy.txt","w")#fichier de sortie
for line in f:
    doc = nlp(line)
    #print(doc.text)
    for token in doc:
        #print(token.text, token.pos_, token.dep_)
        f_out.write(token.text+"_"+token.pos_+" ")
    f_out.write("\n")

f.close()
f_out.close()
