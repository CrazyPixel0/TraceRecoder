
import os
import folium
import pandas as pd
import gpxpy
import gpxpy.gpx
from pytz import timezone
from flask import Flask, render_template, request

app = Flask(__name__)

# 处理一个gpx文件，获取经纬度数据
def processGpxFile(gpx_file):
    gpx = gpxpy.parse(gpx_file)
    Lat      = []
    Lng      = []
    Alt      = []
    for track in gpx.tracks:
        for segment in track.segments:
            points = segment.points
            N = len(points)
            for i in range(N):
                point = points[i]
                lat      = point.latitude
                lng      = point.longitude
                alt      = point.elevation
                Lat.append(lat)
                Lng.append(lng)
                Alt.append(alt)
    return Lat, Lng, Alt

# 根据经纬高度数字，处理数据，获取中心点、经纬轨迹
def getData(Lat, Lng, Alt):
    data=pd.DataFrame()
    data[0]=Lat
    data[1]=Lng
    data[2]=Alt
    data.columns=['Latitude','Longitude','Altitude'] # 经度 纬度 高度
    lat0=data['Latitude'].mean()
    lon0=data['Longitude'].mean()
    df=data[['Latitude','Longitude']]
    return data, lat0, lon0, df

# 根据第一个点的经纬度进行中心点定位
def setMap(path, zoom = 13):
    # 获取中心点坐标
    Lat, Lng, Alt = processGpxFile(open(path, mode = 'r', encoding = 'utf-8'))
    data, lat0, lon0, df = getData(Lat, Lng, Alt)
    # 生成图像
    f = folium.Figure(width=2000, height=1000)
    eq_map = folium.Map(location = [lat0,lon0], tiles="Cartodb dark_matter", zoom_start=zoom).add_to(f)
    return eq_map

def visualizeTracks(pathList, eq_map, zoom = 8):
    for path in pathList:
        gpx_file = open(path, mode = 'r', encoding = 'utf-8')
        Lat, Lng, Alt = processGpxFile(gpx_file)
        data, lat0, lon0, df = getData(Lat, Lng, Alt)
        points=tuple(zip(df['Latitude'],df['Longitude'])) 
        folium.PolyLine(points, color="yellow", weight=2.5, opacity=0.1).add_to(eq_map)
    return eq_map

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        path0 = request.form['gpxfile']
    else:
        gpx_files = os.listdir('D:/TraceRecoder/TraceRecoder/traces')
        gpx_files = [
            filename for filename in gpx_files if filename.endswith('.gpx')]
        return render_template('index.html', gpx_files=gpx_files)
    pathList = []
    gpx_files = os.listdir('D:/TraceRecoder/TraceRecoder/traces/')
    for path in gpx_files:
        if path.endswith('.gpx'):
            pathList.append(os.path.join('D:/TraceRecoder/TraceRecoder/traces/',path))
    eq_map = setMap(pathList[0])
    eq_map = visualizeTracks(pathList, eq_map, 13)
    eq_map.save("./result.html")
    graph_html = "<iframe width = '2400' height = '1600' src = 'static/2023.html' frameborder = '0' > </iframe >"
    return render_template('index.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)



