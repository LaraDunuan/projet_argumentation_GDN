#!/bin/env python3
#  Lara DUNUAN et Siyu WANG
#  Projet Argumentation Grand Débat National, Mai 2019 

import parsimonious, sys

def write_file(data, filename):
    file = open(filename,"w")
    for i in data:
        file.write(i)
        file.write("\n")
    file.close()

grammar1 = parsimonious.Grammar("""
	sent = prop
	prop = det adj? nom adj? verb
	det = tok"/"lemma"/DET"
	adj = tok"/"lemma"/ADJ"
	nom = tok"/"lemma"/NOM"
	verb = tok"/"lemma"/VER"
	word = tok"/"lemma"/"pos
	tok = ~r"[^/]*"
	lemma = ~r"[^/]*"
	pos = ~r"[^/]*"
""")

grammar2 = parsimonious.Grammar("""
	sent = prop
	prop = verb det adj? nom adj?
	det = tok"/"lemma"/DET"
	adj = tok"/"lemma"/ADJ"
	nom = tok"/"lemma"/NOM"
	verb = tok"/"lemma"/VER"
	word = tok"/"lemma"/"pos
	tok = ~r"[^/]*"
	lemma = ~r"[^/]*"
	pos = ~r"[^/]*"
""")

print("Execution de gramargs.py. Patientez, ce programme prend beaucoup de temps...")

for sent in sys.stdin:
	sent = sent.strip()
	
	senttoks = sent.split(' ')
	for i in range(len(senttoks)):
		sentpart = ' '.join(senttoks[i:])
		try:
			sentpartmatch1 = grammar1.match(sentpart)
			print('INPUT:', sent)
			# print('MATCH: at token', i)
			print(sentpartmatch1)
		except parsimonious.exceptions.ParseError:
			pass
		try:
			sentpartmatch2 = grammar2.match(sentpart)
			print('INPUT:', sent)
			# print('MATCH: at token', i)
			print(sentpartmatch2)
		except parsimonious.exceptions.ParseError:
			pass
