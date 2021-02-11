def get_tp(toponym):
    eny_lower_corner = [float(x) for x in toponym['boundedBy']['Envelope']['lowerCorner'].split()]
    eny_upper_corner = [float(x) for x in toponym['boundedBy']['Envelope']['upperCorner'].split()]
    return tuple(eny_upper_corner[i] - eny_lower_corner[i] for i in range(2))