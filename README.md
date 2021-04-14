# scraper-onpe

Scraper ONPE Elecciones Generales 2021

Dos formas: API, WEB

## API

Para descargar a la carpeta `actas_json/` ejecute

```
pip3 install -r requirements.txt
python3 simple_loop.py # To check download check download_checker.py
```


## Web

Este método necesita:

- Chrome v90
- Chrome headers: `ChromeDriver 90.0.4430.24`

```
pip3 install -r requirements.txt
# Descarga header de Chrome
https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/
```


### Tutorials for this script

- https://thinkdiff.net/how-to-run-javascript-in-python-web-scraping-web-testing-16bd04894360
- https://stackoverflow.com/a/58347410/10491422