# Faktaark for tilstandsregnskap

Faktaark med informasjon om indikatorene i nasjonalt tilstandsregnskap.

## Legg inn et nytt faktaark

### 1. Opprett en branch

Opprett en ny branch fra `main`..

Eksempel:
`faktaark-oter`, eller `faktaark-elver`

Gjør alle endringene knyttet til det nye faktaarket/faktaarkene i denne branchen.
Det er ikke så farlig hva den heter, den skal slettes etterpå. Du kan godt legge inn flere faktaark i samme branch. 


### 2. Legg inn PDF-filen

Legg PDF-filen i:

`assets/pdf/`

PDF-filen skal ha indikator-ID-en som filnavn.

Eksempel:

`assets/pdf/NO_NIPR_002.pdf`

**Viktig:** Filnavnet må være det samme som verdien som senere legges inn som `kode` i Markdown-filen. PDF-en kobles automatisk til riktig indikatorside ved hjelp av denne koden.


### 3. Opprett mappe for økosystemet ved behov

Hvis mappen allerede finnes, går du videre til steg 4.

Hvis det ikke allerede finnes en mappe for økosystemet, må vi opprette den. Det gjør vi ved å lage en ny fil med sti til den mappen. Finn en annen index.md, feks `elver/index.md`, og kopier innholdet (fra redigeringsmodus). Index.md trengs for å lage hierarki på nettsiden. Opprett en ny fil, og legg inn /økosystem-navn/index.md i filnavnet. Dette vil automatisk opprette mappen hvis den ikke finnes. Bruk et kort og beskrivende navn for økosystemet, uten mellomrom.

Eksempel:
`elver/index.md`

Mappenavnet blir en del av URL-en til økosystemsiden, for eksempel:

`https://miljodirektoratet.github.io/faktaark-tilstandsregnskap/elver/`

Lim inn innholdet fra en annen index.md, og endre metadata øverst.

Fyll ut:

- **`title`**: Navnet på indikatoren slik det skal vises på nettsiden.
  - Eksempel: `Oter`
- **`kode`**: Indikator-ID.
  - Eksempel: `NO_NIPR_002`
  - Må samsvare nøyaktig med navnet på PDF-filen, uten `.pdf`.
- **`parent`**: Økosystemet indikatoren tilhører.
  - Eksempel: `Elver, bekker og kanaler`
  - Må samsvare nøyaktig med `title` i økosystemets `index.md`.
- **`nav_order`**: Bestemmer rekkefølgen på indikatorene innenfor økosystemet.

**Ikke** endre andre felter. 

### 4. Opprett Markdown-fil for indikatoren

Kopier `testark.md` og legg kopien i riktig økosystemmappe. Gi filen samme navn som indikator-ID-en.

Eksempel:
```text
elver/NO_NIPR_002.md
```

Fyll ut:

- **`title`**: Navnet på indikatoren slik det skal vises på nettsiden.
  - Eksempel: `Oter`
- **`kode`**: Indikator-ID. Må samsvare nøyaktig med navnet på PDF-filen, uten `.pdf`.
  - Eksempel: `NO_NIPR_002`
- **`parent`**: Økosystemet indikatoren tilhører. Må samsvare nøyaktig med `title` i økosystemets `index.md`.
  - Eksempel: `Elver, bekker og kanaler`
- **`nav_order`**: Bestemmer rekkefølgen på indikatorene innenfor økosystemet.
- 

### 5. Lag pull request og merge

Før du lager en pull request, kontroller særlig følgende:

- **`kode` → PDF:** `kode: NO_NIPR_002` gjør at nettsiden finner `assets/pdf/NO_NIPR_002.pdf`.
- **`parent` → økosystem:** `parent: Elver, bekker og kanaler` gjør at faktaarket plasseres under økosystemsiden med `title: Elver, bekker og kanaler`.

Når du er klar:

1. Opprett en pull request mot `main`.
2. Kontroller endringene i pull requesten.
3. Merge til `main`.

Merge til `main` starter deployment som oppdaterer nettsiden.

Slett branchen etterpå. 

### 6. Kontroller nettsiden

Når deployment er ferdig, kontroller at:

- økosystemet vises på riktig sted
- indikatoren vises under riktig økosystem
- indikatornavn og indikator-ID er riktige
- lenken til indikatorsiden fungerer
- riktig PDF vises
- **Åpne faktaarket i ny fane** åpner riktig PDF


## Små endringer

Mindre rettelser kan gjøres direkte på `main`. 

