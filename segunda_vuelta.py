import json
import cloudscraper

import pandas as pd
import random
import time
import os


URL_BASE='https://api.resultadossep.eleccionesgenerales2021.pe/mesas/detalle/'
RESULT_PATH='ACTAS/2/'
MY_USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
COOKIES=dict(cookies_are='working')

RANGO_ACTA_ACTUAL=range(900000,1000000) #200000 y 900000
errors=[]

my_session = cloudscraper.create_scraper()

for ACTA_ACTUAL in RANGO_ACTA_ACTUAL:

    ACTA_ACTUAL_ZERO_IZQ=str(ACTA_ACTUAL).zfill(6)
    ACTUAL_FILEPATH=f'{RESULT_PATH}{ACTA_ACTUAL_ZERO_IZQ}.json'
    print('Procesando ',URL_BASE+ACTA_ACTUAL_ZERO_IZQ)

    if ACTA_ACTUAL%100==0 and ACTA_ACTUAL!=0:
        print('Creando nueva sessión para API')
        my_session.close()
        my_session = cloudscraper.create_scraper()
        time.sleep(0.102+random.uniform(0, 0.014))

    if os.path.isfile(ACTUAL_FILEPATH):
        # Verificar si existe
        print(' Archivo existe, pasando al sgte...')
    else:
        # Descargar y guardar
        try:
            print(f'Descargando y guardando {URL_BASE+ACTA_ACTUAL_ZERO_IZQ}')
            response = my_session.get(URL_BASE+ACTA_ACTUAL_ZERO_IZQ,
                            headers={"User-Agent": MY_USER_AGENT})

            my_json=json.loads(response.text)
            my_json=my_json['procesos']['generalPre']['votos']

            df_acta=pd.DataFrame(my_json)
            df_acta.to_json(ACTUAL_FILEPATH)

        except Exception as e:
            print(f'Error in {ACTA_ACTUAL}:{e}')
            if 'generalPre' in str(e):
                pass
            else:
                errors.append(ACTA_ACTUAL)
        finally:
            time.sleep(0.0125+random.uniform(0, 0.001))



print(errors)