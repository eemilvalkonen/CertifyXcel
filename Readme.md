**CertifyXcel** is an efficient tool designed to generate participation certificates directly from Excel data. By parsing participant information stored in an Excel spreadsheet, the application automatically creates personalized certificates, saving time and streamlining the process of certificate issuance. Whether for events, courses, or workshops, CertifyXcel ensures a seamless and professional certification experience.

# Installation Instructions

## 1. Installing Dependencies
Ensure that you have Python installed. The recommended version is Python 3.8 or newer.

Install the required dependencies with the following command:

```sh
pip install pandas fpdf openpyxl
```

## 2. Adding Fonts
The script uses custom fonts, which should be placed in the `fonts/` directory. Ensure that the following files are present:

- `fonts/ArialBlack.ttf`
- `fonts/ArialNova.ttf`
- `fonts/ArialNova-Bold.ttf`
- `fonts/ArialNovaCond.ttf`
- `fonts/Calibri.ttf`
- `fonts/Calibri-Bold.ttf`

## 3. Adding Images
The script uses images, which should be placed in the `images/` directory. Make sure the following files are available:

- `images/line-break-wide.png`
- `images/signature.png`
- `images/logo.png`

## 4. Setting the Input File
Ensure that the Excel file `Osallistujat.xlsx` is located in the default directory of the script (`../Osallistujat.xlsx`).

## 5. Running the Script
Once all dependencies, fonts, and images are in place, you can run the script with the following command:

```sh
python generateCertificates.py
```

## 6. Output Files
After the script runs, the participation certificates will be saved in the following directory:

```sh
../Certificates/
```
