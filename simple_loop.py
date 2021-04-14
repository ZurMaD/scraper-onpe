import json
from urllib.request import Request, urlopen

import pandas as pd
import random
import time




URL_BASE='https://api.resultados.eleccionesgenerales2021.pe/mesas/detalle/'

LIMA_LIM_MIN=34421 #34244
LIMA_LIM_MAX=48838
MY_USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'


RANGO_ACTA_ACTUAL=range(LIMA_LIM_MIN,LIMA_LIM_MAX)

for ACTA_ACTUAL in RANGO_ACTA_ACTUAL:
    print('Procesando ',ACTA_ACTUAL)


    ACTA_ACTUAL_ZERO_IZQ=str(ACTA_ACTUAL).zfill(6)

    try:
        req = Request(URL_BASE+ACTA_ACTUAL_ZERO_IZQ,     
                        headers={'User-Agent': MY_USER_AGENT})
        webpage_json = urlopen(req).read().decode("utf-8")
    except Exception as e:
        print(e)
        time.sleep(2)
        req = Request(URL_BASE+ACTA_ACTUAL_ZERO_IZQ,     
                        headers={'User-Agent': MY_USER_AGENT})
        webpage_json = urlopen(req).read().decode("utf-8")

    # print(type(webpage_json))

    my_json=json.loads(webpage_json)

    time.sleep(0.2+random.uniform(0, 0.2))


    df_acta_congresal=pd.DataFrame()


    for i in range(20):
        my_row_from_json=my_json['procesos']['generalCon']['votos'][0]
        df_acta_congresal=df_acta_congresal.append(my_row_from_json, 
                            ignore_index=True)


    df_acta_congresal.to_json(f'actas_json/{ACTA_ACTUAL_ZERO_IZQ}.json')