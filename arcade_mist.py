#!/usr/bin/python3

# URL check:
#
# SELECT DISTINCT arcade_mist_url FROM arcade_mist;
# wget --spider -i spider.txt 2>&1 | grep -B 3 "404 Not Found"

import sqlite3
import urllib.parse

sep_start = '| '
sep = ' | '
sep_end = ' |'

sql_where = ''

con = sqlite3.connect('arcade_mist.sqlite')

cur = con.cursor()

all_arcade_count = 0
gehstock_arcade_count = 0
jotego_arcade_count = 0

res = cur.execute('SELECT arcade_name, genre_name, year, manufacturer_hardware, arcade_mist_url, arcade_museum_id, core_name, note FROM arcade_mist LEFT JOIN genre ON genre.genre_id = arcade_mist.genre_id ' + sql_where + ' ORDER BY arcade_name')

if res:
    print('| Arcade (mra link) | Genre | Year | Hardware (core [+ mra] link) | Arcade Museum |')
    print('|------|------|------|------|------|')
    for arcade in res:
        arcade_name, genre_name, year, manufacturer_hardware, arcade_mist_url, arcade_museum_id, core_name, note = arcade

        arcade_mist_url_lower = arcade_mist_url.lower()

        # Start separator
        print(sep_start, end = '')

        # Arcade [+ note] + separator
        if 'jotego' in arcade_mist_url:
            print('[' + arcade_name + ']' + '(' + arcade_mist_url.replace('/mist', '/mra') + ')', end = '')
            if note:
                print(' (' + note + ')', end = '')
            print(sep, end = '')
        else:
            print(arcade_name, end = '')
            if note:
                print(' (' + note + ')', end = '')
            print(sep, end = '')

        # Genre + separator
        print(genre_name + sep, end = '')

        # Year + separator
        print(year + sep, end = '')

        # Hardware + separator
        print('[' + manufacturer_hardware + ']' + '(' + urllib.parse.quote(arcade_mist_url, ':/'), end ='')
        if 'jotego' in arcade_mist_url_lower:
            print('/' + core_name + '.rbf', end = '');
        print(')' + sep, end = '')

        # Arcade museum link + separator
        if arcade_museum_id:
            print('[' + arcade_museum_id + ']' + '(https://www.arcade-museum.com/game_detail.php?game_id=' + arcade_museum_id + ')', end = '')

        # End separator
        print(sep_end)

        all_arcade_count += 1
        if 'jotego' in arcade_mist_url_lower:
            jotego_arcade_count += 1
        if 'gehstock' in arcade_mist_url_lower:
            gehstock_arcade_count += 1

con.close()

print('All Arcades count:', all_arcade_count)
print('\n')
print('Gehstock Arcades count:', gehstock_arcade_count)
print('\n')
print('Jotego Arcades count:', jotego_arcade_count)
