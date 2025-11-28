import xmltodict
from geopy.distance import geodesic
import os
import datetime

def FileRead(path: str) -> dict:
    with open(path, 'r') as f:
        try:
            XmlObj = xmltodict.parse(f.read())
            return XmlObj
        except SystemError:
            raise SystemError
        

def SegParse(Seg: dict) -> dict:
    dummy = dict()
    return dummy

def CheckGPX(GPXObject: dict) -> dict:
    dummy = {"isGPX": bool, "creator": "", "version": ""}
    if bool(GPXObj['gpx']) and bool(GPXObj['gpx']['@creator']):
        dummy['isGPX'] = True
        dummy['creator'] = GPXObj['gpx']['@creator']
        dummy['version'] = GPXObj['gpx']['@version']
    else:
        dummy['isGPX'] = False
    return dummy

def CheckTrkPt(GPXObject: dict) -> int:
    count = 0
    for i in GPXObject['gpx']['trk']['trkseg']:
        for tmp in GPXObject['gpx']['trk']['trkseg'][1]['trkpt']:
            count = count + 1
    return count

def TimePassed(GPXObject: dict):
    print("placeholder")

def DistanceTravelCount(GPXObject: dict) -> float:
    count = 0
    distance = 0
    d_pnt = 0
    p_pnt = ()
    p_time = ""
    for i in GPXObject['gpx']['trk']['trkseg']:
        # Debug only
        # print(type(i))
        # print(i)
        # Debug end
        for tmp in i['trkpt']:
            # Debug only
            # print(type(tmp))
            # print(tmp)
            pnt = (tmp['@lat'], tmp['@lon'])
            # print(type(pnt))
            # print(pnt)
            # Debug end
            if p_pnt is not pnt:
                d_pnt = geodesic(p_pnt, pnt).kilometers
                # You could use a tuple here btw
                p_pnt = pnt
                #print(d_pnt)
                distance = distance + d_pnt
            else:
                pass
            # print(distance)
    
            # print(count)
        count = count + 1
    return distance




GPXObj = FileRead("11-Nov-2025-1704.gpx")

Track = GPXObj['gpx']['trk']
