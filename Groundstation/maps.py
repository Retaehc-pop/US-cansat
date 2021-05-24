import folium
import io


def getmap(startpoint, coordinate, alt):
    print(startpoint)
    print(coordinate)
    print(alt)
    m = folium.Map(
        location=startpoint,
        tiles='OpenStreetMap',
        zoom_start=16,
        min_zoom=10
    )
    for i, point in enumerate(coordinate):
        if i == 0:
            folium.Marker(
                location=point,
                popup="starting location : " + str(alt[i]) + 'm',
                icon=folium.Icon(color="green"),
            ).add_to(m)
        elif i == len(coordinate) - 1:
            folium.Marker(
                location=point,
                popup="FIN POINT : " + str(alt[i]) + 'm',
                icon=folium.Icon(color="red"),
            ).add_to(m)
        else:
            folium.Marker(
                location=point,
                popup=str(i + 1) + ' : ' + str(alt[i]) + 'm',
                icon=folium.Icon(),
            ).add_to(m)
    folium.PolyLine(coordinate, color="red", weight=2.5, opacity=1).add_to(m)
    data = io.BytesIO()
    m.save(data, close_file=False)
    print("map export")
    return data


if __name__ == "__main__":
    print(getmap((13.726807, 100.527764), [(13.726807, 100.527764), (13.726806, 100.527763), (13.726805, 100.527762)],
                 [1, 2, 3]))
