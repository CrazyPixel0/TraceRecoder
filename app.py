
import os
import folium
import pandas as pd
import gpxpy
import gpxpy.gpx
from pytz import timezone
from flask import Flask, render_template, request

app = Flask(__name__)

def VISUALIZE_MAP(path,zoom=13):

    gpx_file = open(path, 'r')
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
    data=pd.DataFrame()
    data[0]=Lat
    data[1]=Lng
    data[2]=Alt
    data.columns=['Latitude','Longitude','Altitude']
    lat0=data['Latitude'].mean()
    lon0=data['Longitude'].mean()
    df=data[['Latitude','Longitude']]
    points=tuple(zip(df['Latitude'],df['Longitude'])) 
    f = folium.Figure(width=800, height=400)
    eq_map = folium.Map([lat0,lon0],zoom_start=zoom).add_to(f)
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(eq_map)
    
    return eq_map


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        path0 = request.form['gpxfile']
        eq_map = VISUALIZE_MAP(os.path.join('static',path0),13)
        eq_map.save("static/2023.html")
        graph_html = "<iframe width = '600' height = '400' src = 'static/2023.html' frameborder = '0' > </iframe >"
        return render_template('index.html', graph_html=graph_html)

    else:
        gpx_files = os.listdir('static/')
        gpx_files = [
            filename for filename in gpx_files if filename.endswith('.gpx')]
        return render_template('index.html', gpx_files=gpx_files)

if __name__ == '__main__':
    app.run(debug=True)



