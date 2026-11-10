# Faktaark for tilstandsregnskap
Faktaark med informasjon om indikatorene i nasjonalt tilstandsregnskap. 

## Legg inn nytt ark
1. Opprett en ny branch fra "main", feks faktaark1
2. Legg pdf-filen i assets/pdf, feks assets/pdf/faktaark1.pdf
3. Kopier innholdet i testark.md til en ny fil og navngi den som pdf-filen, feks faktaark1.md
4. Endre: title (navn på indikatoren, feks Oter), permalink (url-en, feks /NO_NIPR_002/), kode (feks NO_NIPR_002), parent (navn på økosystemet), og pdf (sti til pdf-en, /assets/pdf/faktaark1.pdf)
6. Lag en pull request og merge. Dette skal starte deployment som oppdaterer nettsiden.
7. Sjekk at det ser ok ut på nettsiden. 
8. Slett branchen når alt er merget.

Hvis det må gjøres små endringer etterpå er det helt ok å arbeide direkte på main. 
