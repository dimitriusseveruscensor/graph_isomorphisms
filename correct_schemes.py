def correct_transfers(file, replace_dict, corr_file):
    stations = open(file, 'r')
    corr_stations = open(corr_file, 'w')
    for line in stations:
        for key in replace_dict.keys():
            if key in line:
                line = line.replace(key, replace_dict[key])
        corr_stations.write(line)


correct_transfers('HH.txt', {'Hauptbahnhof_Süd': 'Hauptbahnhof_Nord', 'Rathaus': 'Jungfernstieg'}, 'HH_corr.txt')
correct_transfers('NYC.txt', {'Jackson_Heights–Roosevelt_Avenue': '74th_Street–Broadway',
                              '42nd_Street–Port_Authority_Bus_Terminal': '42nd_Street–Times_Square',
                              '42nd_Street–Bryant_Park': '5th_Avenue', '14th_Street–6th_Avenue': '14th_Street',
                              'Lorimer_Street': 'Metropolitan_Avenue', 'Chambers_Street': 'Park_Place',
                              'WTC_Cortlandt': 'Park_Place', 'Court_Street': 'Borough_Hall'}, 'NYC_corr.txt')