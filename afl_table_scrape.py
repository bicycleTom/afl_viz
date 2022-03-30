#!/usr/bin/python

import itertools
import requests
from bs4 import BeautifulSoup

URL = 'https://afltables.com/afl/stats/games/2022/091620220325.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')

table = soup.find('table', class_='sortable')

table_rows = table.find_all('tr')

kicks = []

for tr in table_rows[2:-3]:
	td = tr.find_all('td')
	row = [i.text for i in td[2:3]]
	kicks.append(row)

print(list(itertools.chain(*kicks)))

"""
key
#=Jumper
GM=Games played
KI=Kicks
MK=Marks
HB=Handballs
DI=Disposals
DA=Disposal average
GL=Goals
BH=Behinds
HO=Hit outs
TK=Tackles
RB=Rebound 50s
IF=Inside 50s
CL=Clearances
CG=Clangers
FF=Free kicks for
FA=Free kicks against
BR=Brownlow votes
CP=Contested possessions
UP=Uncontested possessions
CM=Contested marks
MI=Marks inside 50
1%=One percenters
BO=Bounces
GA=Goal assist
%P=Percentage of game played
SU=Sub (On/Off)
↑=subbed on
↓=subbed off
"""