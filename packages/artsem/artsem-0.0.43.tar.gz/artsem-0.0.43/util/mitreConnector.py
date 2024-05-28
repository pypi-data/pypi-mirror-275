import json
import re
import requests
from bs4 import BeautifulSoup

"""
Check out docs/05-ttp-matrix/readme.md for more information 
about the intention and behavior of this script 
"""


# TODO: implement logging

def sanitize(txt):
    return re.sub("[\n\t\r\b]+", '', re.sub('\\s+', ' ', txt)).strip()


def get_ttp_info(table_index=0):
    assert int(table_index) >= 0, "Index out of range"
    soup = BeautifulSoup(requests.get('https://attack.mitre.org/#').text, 'html.parser')
    # soup = BeautifulSoup('\n'.join(open('mitre_page.html', 'r').readlines()), 'html.parser')
    buffer = list()
    table = soup.findAll('table', class_='techniques-table')[int(table_index)]
    counter = 0
    rows = table.findAll('td')
    while counter < len(rows):
        row = rows[counter]
        san = sanitize(row.text)
        if len(san) <= 1:
            counter += 1
        elif san.find(' (') != -1:
            buffer.append(
                {
                    'technique': re.sub(' \\([0-9]+\\)', '', san).strip(),
                    'subtechniques': re.sub('[\n\t\r\b]+', '&',
                                            re.sub('( {2,}|[\n\t\r\b]+$|^[\t\n\r\b]+)', '',
                                                   rows[counter + 3].text))[0:-1].split('&')
                }
            )
            counter += 4
        else:
            buffer.append({'technique': re.sub('([\n\t\r\b]+| {2,})', '', rows[counter].text), 'subtechniques': []})
            counter += 1
    return {'tactic': sanitize(soup.findAll('td', class_='tactic name')[int(table_index)].text), 'techniques': buffer}


if __name__ == '__main__':
    with open('../../docs/05-ttp-matrix/mitre_ttp.json', 'w') as outfile:
        json.dump(get_ttp_info(6), outfile, indent=2)
