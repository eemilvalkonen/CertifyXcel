CertifyXcel is an efficient tool designed to generate participation certificates directly from Excel data. By parsing participant information stored in an Excel spreadsheet, the application automatically creates personalized certificates, saving time and streamlining the process of certificate issuance. Whether for events, courses, or workshops, CertifyXcel ensures a seamless and professional certification experience.

# Asennusohjeet

## 1. Riippuvuuksien asentaminen
Varmista, että sinulla on Python asennettuna. Suositeltava versio on Python 3.8 tai uudempi.

Asenna tarvittavat riippuvuudet komennolla:

```sh
pip install pandas fpdf openpyxl
```

## 2. Fonttien lisääminen
Skriptissä käytetään mukautettuja fontteja, jotka tulee sijoittaa `fonts/`-hakemistoon. Varmista, että seuraavat tiedostot ovat olemassa:

- `fonts/ArialBlack.ttf`
- `fonts/ArialNova.ttf`
- `fonts/ArialNova-Bold.ttf`
- `fonts/ArialNovaCond.ttf`
- `fonts/Calibri.ttf`
- `fonts/Calibri-Bold.ttf`

## 3. Kuvien lisääminen
Skriptissä käytetään kuvia, jotka tulee sijoittaa `images/`-hakemistoon. Tarkista, että seuraavat tiedostot löytyvät:

- `images/line-break-wide.png`
- `images/line-break.png`
- `images/signature.png`
- `images/logo.png`

## 4. Lähdetiedoston asettaminen
Varmista, että Excel-tiedosto `Osallistujat.xlsx` sijaitsee skriptin oletuspolussa (`../Osallistujat.xlsx`).

## 5. Skriptin suorittaminen
Kun kaikki riippuvuudet, fontit ja kuvat ovat paikoillaan, voit suorittaa skriptin komennolla:

```sh
python generateCertificates.py
```

## 6. Tulostiedostot
Skriptin suorittamisen jälkeen osallistumistodistukset tallennetaan hakemistoon:

```sh
../Osallistumistodistukset/
```