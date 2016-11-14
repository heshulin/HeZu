import httplib2
import json
import math


def get_distance(origins, destination):
    conn = httplib2.Http()
    resp, content = conn.request(
        'http://restapi.amap.com/v3/distance?origins=' + origins + '&destination=' + destination + '&output=json&key=f1be42e22d5e08b764f67f46e5703cb4',
        'GET')
    res = json.loads(content.decode('utf-8'))
    if res['status'] == '1':
        distance = int(res['results'][0]['distance'])
        return 1, distance
    else:
        return 0, res['info']

def get_around(lat, lon, r):
    try:
        lat = float(lat)
        lon = float(lon)
        r = float(r)
        degree = float((14901 * 1609) / 360.0)
        dpmlat = 1 / degree
        radiuslat = dpmlat * r
        minlat = lat - radiuslat
        maxlat = lat + radiuslat

        mpdlon = degree * math.cos(lat * (3.14159265 / 180))
        dpmlon = 1 / mpdlon
        radiuslon = dpmlon * r
        minlon = lon - radiuslon
        maxlon = lon + radiuslon

        return minlat, maxlat, minlon, maxlon
    except Exception as e:
        print(e)
        return None

def get_hint(keyword):
    conn = httplib2.Http()
    resp, content = conn.request(
        'http://restapi.amap.com/v3/assistant/inputtips?keywords=' + keyword + '&output=JSON&key=f1be42e22d5e08b764f67f46e5703cb4',
        'GET')
    res = json.loads(content.decode('utf-8'))
    return res

