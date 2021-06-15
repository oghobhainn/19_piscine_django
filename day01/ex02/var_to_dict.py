#! /usr/bin/env python3

def list_to_dic():
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
    ]
    my_dic = { }
    for item in d:
        if item[1] in my_dic:
            my_dic[item[1]] += " " + item[0]
        else:
            my_dic[item[1]] = item[0]
    for (date, musician) in my_dic.items():
        print("{0} : {1}".format(date, musician))

if __name__=='__main__':
    list_to_dic()
