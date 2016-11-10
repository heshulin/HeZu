import httplib2
import json


def get_distance(origins, destination):
    try:
        conn = httplib2.Http()
        resp, content = conn.request(
            'http://restapi.amap.com/v3/distance?origins=' + origins + '&destination=' + destination + '&output=json&key=f1be42e22d5e08b764f67f46e5703cb4',
            'GET')
        res = json.loads(content.decode('utf-8'))
        if res['status'] == '1':
            distance = res['results'][0]['distance']
            return 1, distance
        else:
            return 0, res['info']
    except Exception as e:
        print(e)
        return 0, '服务器异常'

