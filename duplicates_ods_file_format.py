import pyexcel_ods3
import csv


FILE_PATH = '/home/rtm/Desktop/crow.ods'
ods_data = pyexcel_ods3.get_data(FILE_PATH)
crow_tr = [item[0] for item in ods_data['Наши'] if item]
adv_tr = [item[0] for item in ods_data['Адверт'] if item]
dif = [tr for tr in adv_tr if tr not in crow_tr]
adv_row_dif = list()
for row in ods_data['Адверт']:
    if row:
        if row[0] in dif:
            adv_row_dif.append(row)


with open('tr_difference.csv', 'w') as dif_f:
    writer = csv.writer(dif_f, delimiter=';')
    writer.writerows(adv_row_dif)
