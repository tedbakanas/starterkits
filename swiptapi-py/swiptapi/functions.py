# imports
import logging
from random import sample
import numpy as np
import folium
from swiptapi import swiptapi_client

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] {%(filename)s} %(levelname)s - %(message)s')

def create_random_swiss_plot(file_path: str):
    """
    Uses the other functions in the swiptapi package to create a plot of busses in Switzerland
    """

    point = get_random_swiss_point()

    logging.info("Point selected:" + str(point['x']) + str(point['y']))

    sc = swiptapi_client()
    response = sc.search_around_point(lati=point['x'],longi=point['y'])

    logging.info("Making plot")

    my_map = folium.Map(location=[46.801111,8.226667],zoom_start = 8)
    for poi in response['stations']:
        if poi['coordinate']['x'] is not None:
            folium.Marker([poi['coordinate']['x'],poi['coordinate']['y']], popup = poi['name']).add_to(my_map)

    my_map.save(outfile=file_path)

def get_random_swiss_point():
    """
    Uses basic math to pick a point in a circle that roughly approximates Switzerland
    """

    logging.info("Switzerland doesn't really look like a circle but thats ok!")
    
    swi_center_x = 46.801111
    swi_center_y = 8.226667
    
    radius = sample(set(np.arange(0,2.3,0.01)),1)[0]
    theta = sample(set(np.arange(0,2*np.pi,0.01)),1)[0]
    x = swi_center_x + radius*np.cos(theta)
    y = swi_center_y + radius*np.sin(theta)
    
    return {"x": x, "y": y}