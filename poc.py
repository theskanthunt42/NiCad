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
    for i in GPXObject['gpx']['trk']['trkseg']:
        for tmp in GPXObject['gpx']['trk']['trkseg'][1]['trkpt']:
            pnt = (GPXObject['gpx']['trk']['trkseg'][1]['trkpt'][tmp]['@lat'], GPXObject['gpx']['trk']['trkseg'][1]['trkpt'][tmp]['@lon'])
            if CheckTrkPt(GPXObject) < count:
                x_pnt = (GPXObject['gpx']['trk']['trkseg'][1]['trkpt'][tmp+1]['@lat'], GPXObject['gpx']['trk']['trkseg'][1]['trkpt'][tmp+1]['@lat'])
                d_pnt = geodesic(pnt, x_pnt).kilometers
            else:
                d_pnt = 0
                pass
            distance = distance + d_pnt
            count = count + 1
    return distance




GPXObj = FileRead("11-Nov-2025-1704.gpx")

Track = GPXObj['gpx']['trk']
