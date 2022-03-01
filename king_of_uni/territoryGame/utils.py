def get_center_coordinates(latA, lonA, latB=None, lonB=None):
    cord = (latA, lonA)
    if latB:
        cord = [(latA+latB)/2, (lonA+lonB)/2]
    return cord

def get_zoom(distance):
    if distance <= 300:
        return 50
    elif distance > 300  and distance <=1000:
        return 30
    else:
        return 14
