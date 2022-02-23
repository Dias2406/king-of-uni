def get_center_coordinates(latA, lonA, latB=None, lonB=None):
    cord = (latA, lonA)
    if latB:
        cord = [(latA+latB)/2, (lonA+lonB)/2]
    return cord

def get_zoom(distance):
    if distance <= 1000:
        return 100
    elif distance > 1000  and distance <=2000:
        return 14
    else:
        return 10
