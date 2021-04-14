import os


directories = os.listdir('actas_json')

LIMA_LIM_MIN=34244
LIMA_LIM_MAX=48838

err=[]

for acta in range(LIMA_LIM_MIN,LIMA_LIM_MAX):

    acta_json=str(acta).zfill(6)+'.json'

    if acta_json in directories:
        print(acta_json, 'Found')
    else:
        print(acta_json,' Not found')

        err.append(acta)

print(err)