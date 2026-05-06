import shapely

def create_cig_polys(data):
    cig3_poly_coords = []; cig3_polys = []
    cig2_poly_coords = []; cig2_polys = []; cig2_refined_polys = []
    cig1_poly_coords = []; cig1_polys = []; cig1_refined_polys = []
    for entry in data:
        type = entry[0]
        match type:
            case 'CIG1':
                for bleh in entry[1]:
                    cig1_poly_coords.append(bleh['geometry']['coordinates'][0])
            case 'CIG2':
                for bleh in entry[1]:
                    cig2_poly_coords.append(bleh['geometry']['coordinates'][0])
            case 'CIG3':
                for bleh in entry[1]:
                    cig3_poly_coords.append(bleh['geometry']['coordinates'][0])
    for fuck in cig1_poly_coords:
        cig1_polys.append(shapely.Polygon(fuck))
    for fuck in cig2_poly_coords:
        cig2_polys.append(shapely.Polygon(fuck))
    for fuck in cig3_poly_coords:
        cig3_polys.append(shapely.Polygon(fuck))

    if cig2_polys != []:
        for cig1_polygon in cig1_polys:
            for cig2_polygon in cig2_polys:
                cig1_polygon = cig1_polygon.difference(cig2_polygon)
            cig1_refined_polys.append(cig1_polygon)
    else:
        cig1_refined_polys = cig1_polys
    if cig3_polys != []:
        for cig2_polygon in cig2_polys:
            for cig3_polygon in cig3_polys:
                cig2_polygon = cig2_polygon.difference(cig3_polygon)
            cig2_refined_polys.append(cig2_polygon)
    else:
        cig2_refined_polys = cig2_polys

    cig1_return_list = []; cig2_return_list = []; cig3_return_list = []
    for poly in cig3_polys:
        cig3_return_list.append(list(poly.exterior.coords))
    for poly in cig2_refined_polys:
        FUCK = list(poly.exterior.coords)
        FUCK2 = [list(hole.coords) for hole in poly.interiors]
        for fuck in FUCK2:
            for killme in fuck:
                FUCK.append(killme)
        cig2_return_list.append(FUCK)
    for poly in cig1_refined_polys:
        FUCK = list(poly.exterior.coords)
        FUCK2 = [list(hole.coords) for hole in poly.interiors]
        for fuck in FUCK2:
            for killme in fuck:
                FUCK.append(killme)
        cig1_return_list.append(FUCK)
    
    return [{'cig1':cig1_poly_coords,'cig2':cig2_poly_coords,'cig3':cig3_poly_coords},
            {'cig1':cig1_return_list,'cig2':cig2_return_list,'cig3':cig3_return_list}]