# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: azouaiga <azouaiga@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/13 04:15:19 by azouaiga          #+#    #+#              #
#    Updated: 2022/01/29 09:18:07 by azouaiga         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests as req
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

html = req.get("https://www.worldometers.info/coronavirus/")
parsed = BeautifulSoup(html.content, features="html.parser")
table = parsed.find('table', attrs={'id': 'main_table_countries_today'})
rows = table.find_all("tr")
data = []
for x in rows:
    data.append(x.text.strip().split("\n")[1:13])

df = pd.DataFrame(data[9:232], columns = data[0])
time = datetime.today().isoformat().split("T")[0].replace("-","_")
filename = "covid_data_" + time + ".xlsx"
df.to_excel(filename)
