# #!#/usr/bin/env python
# # coding:utf-8
#
# import sqlite3
# import requests
# from bs4 import BeautifulSoup
# import time
#
# def get_data(url,i):
#     req = requests.get(url, i)
#     soup = BeautifulSoup(req.text, 'lxml')
#     try:
#         table = soup.select("#ContentPlaceHolder1_lbldata table table")[0].find_all("td")
#         for j in table:
#             print (j)
#         year = str(i)
#         province = table[0].find("b").string
#         type_db = table[3].string
#         crop = table[6].string
#         account = str(table[7].string)
#         push_data(year, province, crop, type_db, account)
#     except:
#         return False
#
# def push_data(year, province, crop, type_db, account):
#     conn = sqlite3.connect('/Users/austin/Documents/farming/farming/db.sqlite3')
#     cur = conn.cursor()
#     try:
#         cur.execute('INSERT INTO mysite_farmdata (year,province,crop,type_db,account) VALUES (?,?,?,?,?)',(year,province,crop,type_db,account))
#         conn.commit()
#         cur.close()
#         conn.close()
#     except sqlite3.Error as e:
#         print ('error!', e.args[0])
#
#
# if __name__ == "__main__":
#     for i in range(2015, 2016):
#         for j in range(11, 66):
#             for k in range(2, 3):
#                 for v in range(1, 2):
#                     url = "http://202.127.42.157/moazzys/nongqing_result.aspx?year={0}&prov={1}%20%20%20&item={2}&type={3}&radio=1&order1=year_code&order2=prov_code&order3=item_code".format(i, j, k, v)
#                     get_data(url, i)
#                     time.sleep(1)
