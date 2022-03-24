from bs4 import BeautifulSoup
import requests

url = "https://www.nairaland.com"
req = requests.get(url)

soup = BeautifulSoup(req.text, 'lxml')

tds = soup.findAll("td", class_="l")

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table style="margin-left:auto; margin-right: auto; font-size: 20px;">
        <tr>
            <th>
                Section
            </th>
            <th>
                Forum
            </th>
            <th>
                Forum Url
            </th>
        </tr>
    </table>
</body>
</html>
'''

soup1 = BeautifulSoup(html, 'lxml')

for td in tds:
    anchors = td.find_all('a')
    iteration = 1
    section_name = ''
    for anchor in anchors:
        link = anchor['href']
        abs_link = f'{url}{link}'
        fname = anchor.b.string

        if iteration == 1:
            section_name = fname
        else:

            forum_td = soup1.new_tag('td')
            forum_td.string = fname

            link_td = soup1.new_tag('td')

            link_a = soup1.new_tag('a', href=f'{abs_link}')
            link_a.string = abs_link

            link_td.append(link_a)
        # print(abs_link, fname)

            section_td = soup1.new_tag('td')
            section_td.string = section_name

            section_name = ''

            tr = soup1.new_tag('tr')

            tr.append(section_td)
            tr.append(forum_td)
            tr.append(link_td)

            soup1.table.append(tr)

        iteration += 1

with open('forums.html', 'w') as html_file:
    html_file.write(soup1.prettify())
# print(len(tds))