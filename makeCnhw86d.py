# -*- coding:utf-8 -*-
#パナソニックのナビCN-HW860D用の行き先データを作ります。

from __future__ import unicode_literals
import codecs
import binascii
import struct
import geocoder

def lnglat_to_data(title,lng,lat):
    #title='カラス'
    title_data=title.encode('shift-jis')


    lng_data=int(lng*36000)
    lat_data=int(lat*36000)

    geo=geocoder.google([lat,lng],language='ja',method='reverse')
    pt_add=geo.address[13:33]
    add_name=pt_add.encode('shift-jis')
    
    f=codecs.open('./carnav3.dcf','r+b')
    f.seek(0x200)
    f.write(struct.pack('>i',lng_data))
    f.seek(0x204)
    f.write(struct.pack('>i',lat_data))
    
    f.seek(0x210)
    f.write(add_name)
    
    f.seek(0x830)
    f.write(title_data)

def title_to_data(title):
    
    geo=geocoder.google(title)
    title_data=title.encode('shift-jis')
    lng=geo.lng
    lat=geo.lat
    lng_data=int(lng*36000)
    lat_data=int(lat*36000)

    geo=geocoder.google([lat,lng],language='ja',method='reverse')
    pt_add=geo.address[13:33]
    add_name=pt_add.encode('shift-jis')
    
    f=codecs.open('./carnav3.dcf','r+b')
    f.seek(0x200)
    f.write(struct.pack('>i',lng_data))
    f.seek(0x204)
    f.write(struct.pack('>i',lat_data))
    
    f.seek(0x210)
    f.write(add_name)
    
    f.seek(0x830)
    f.write(title_data)
