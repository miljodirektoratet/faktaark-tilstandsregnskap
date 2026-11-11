# Faktaark for tilstandsregnskap
Faktaark med informasjon om indikatorene i nasjonalt tilstandsregnskap. 

## Legg inn nytt ark
1. Opprett en ny branch fra "main", feks faktaark1
2. Legg pdf-filen i assets/pdf, feks assets/pdf/NO_NIPR_002.pdf. Det er viktig at navnet på pdf-en kun er indikator-ID-en.
3. Hvis ikke økosystemet har en mappe enda, opprett en mappe for økosystemet. Navnet på denne mappen vil bli med i linken til hjemmesiden, feks https://miljodirektoratet.github.io/faktaark-tilstandsregnskap/elver/
4. Denne mappen trenger også en index.md. Kopier innholdet i en av disse fra et annet økosystem og endre title, nav_order (rekkefølge i listen på nettsiden), og permalink. 
5. Kopier innholdet i testark.md til en ny fil og navngi den som /økosystem/id.md, feks /elver/NO_NIPR_002.md
6. Endre: title (navn på indikatoren, feks Oter), kode (feks NO_NIPR_002), og parent (navn på økosystemet).
7. Lag en pull request og merge. Dette skal starte deployment som oppdaterer nettsiden.
8. Sjekk at det ser ok ut på nettsiden. 
9. Slett branchen når alt er merget.

Hvis det må gjøres små endringer etterpå er det helt ok å arbeide direkte på main. 
