__author__ = "Jakupov Dias"

def get_center_coordinates(latA, lonA, latB=None, lonB=None):
    """Returns centrelised coordinates for folium map"""
    cord = (latA, lonA)
    if latB:
        cord = [(latA+latB)/2, (lonA+lonB)/2]
    return cord

def get_zoom(distance):
    """Returns optimal zoom level for folium map"""
    if distance <= 300:
        return 50
    elif distance > 300  and distance <=1000:
        return 30
    else:
        return 14