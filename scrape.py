import urllib
import re
from scrapy.selector import Selector
from tqdm import tqdm


def get_line_stations(url):
    bdi = u'<bdi>([\wß().\-–,/\' ]+)<\/bdi>'
    req = urllib.request.Request(url, headers={'User-Agent': "Chrome/35.0.1916.47"})
    html = urllib.request.urlopen(req).read()
    #html_response = HtmlResponse(url, body=html)
    #print(html_response)
    entry_list = Selector(text=html).xpath('//*[@id="sidebar_content"]/div[1]/ul[2]/li').extract()
    #print(entry_list)
    stations = []
    for entry in entry_list:
        #print(entry)
        if 'stop' in entry:
            #print(entry)
            station = re.findall(bdi, entry)
            if len(station):
                stations.append(station[0].replace(' ', '_'))
            #print(station)
    return stations


def make_lines(lines, name):
    edgelist = open(name + '.txt', 'w')
    for line in tqdm(lines):
        stations = get_line_stations(line)
        for num in range(1, len(stations)):
            edgelist.write(stations[num - 1] + ' ' + stations[num] + '\r\n')



#Nizhnii Novgorod
nizhnii_novgorod = ['https://www.openstreetmap.org/relation/283406', 'https://www.openstreetmap.org/relation/2580500']
make_lines(nizhnii_novgorod, 'NN')

#Hamburg
hamburg = ['https://www.openstreetmap.org/relation/1687358', 'https://www.openstreetmap.org/relation/60691',
           'https://www.openstreetmap.org/relation/1643324', 'https://www.openstreetmap.org/relation/2872789',
           'https://www.openstreetmap.org/relation/1687357', 'https://www.openstreetmap.org/relation/1687359']
make_lines(hamburg, 'HH')

#New York
new_york = ['https://www.openstreetmap.org/relation/364630', 'https://www.openstreetmap.org/relation/366783',
            'https://www.openstreetmap.org/relation/366784', 'https://www.openstreetmap.org/relation/366785',
            'https://www.openstreetmap.org/relation/366778', 'https://www.openstreetmap.org/relation/366777',
            'https://www.openstreetmap.org/relation/366765', 'https://www.openstreetmap.org/relation/366774',
            'https://www.openstreetmap.org/relation/366770', 'https://www.openstreetmap.org/relation/366775',
            'https://www.openstreetmap.org/relation/366771', 'https://www.openstreetmap.org/relation/366776',
            'https://www.openstreetmap.org/relation/366772', 'https://www.openstreetmap.org/relation/366764',
            'https://www.openstreetmap.org/relation/366782', 'https://www.openstreetmap.org/relation/366763',
            'https://www.openstreetmap.org/relation/366767', 'https://www.openstreetmap.org/relation/366768',
            'https://www.openstreetmap.org/relation/366769', 'https://www.openstreetmap.org/relation/366780',
            'https://www.openstreetmap.org/relation/366766', 'https://www.openstreetmap.org/relation/366809',
            'https://www.openstreetmap.org/relation/2623983', 'https://www.openstreetmap.org/relation/6942556',
            'https://www.openstreetmap.org/relation/366773']
make_lines(new_york, 'NYC')
