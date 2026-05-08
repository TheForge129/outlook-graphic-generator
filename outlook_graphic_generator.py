import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg
import getpass

import setup_axes
import draw_outlook
import cig_handler

mpl.rcParams['figure.dpi'] = 72
mpl.rcParams['savefig.dpi'] = 72

###################################

# TODO: ADD SALT LAKE TO BOUNDARIES

# TODO: FILTER CONTOURS TO US BORDERS + ~20 MILES

###################################

tor_cig_plotted_flag = False
wind_cig_plotted_flag = False
hail_cig_plotted_flag = False

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(SCRIPT_DIR,"config.json")
json_path = os.path.join(SCRIPT_DIR,"outlook.json")
cat_legend_path = os.path.join(SCRIPT_DIR,"img/categorical_legend.png")
tor_legend_path = os.path.join(SCRIPT_DIR,"img/tornado_legend.png")
wind_legend_path = os.path.join(SCRIPT_DIR,"img/wind_legend.png")
hail_legend_path = os.path.join(SCRIPT_DIR,"img/hail_legend.png")

with open(json_path) as json_file:
    outlook_data = json.loads(json_file.read())

with open(config_path) as json_file:
    config_data = json.loads(json_file.read())

cat_data = outlook_data["forecastCycle"]["days"]["1"]["data"]["categorical"]
tor_data = outlook_data["forecastCycle"]["days"]["1"]["data"]["tornado"]
wind_data = outlook_data["forecastCycle"]["days"]["1"]["data"]["wind"]
hail_data = outlook_data["forecastCycle"]["days"]["1"]["data"]["hail"]

metadata = outlook_data["forecastCycle"]["days"]["1"]["metadata"]
valid_date = metadata["validDate"]
valid_date_list = list(valid_date)
for fuck in [4,6,8,10]:
    valid_date_list.pop(fuck)
del(valid_date_list[12:]); valid_date_list.insert(8,'_')
valid_date_fname_friendly = "".join(valid_date_list)
metadata['day'] = 1

if config_data['autoIssueDate'] == False:
    metadata['issueDate'] = config_data['issueDate']
if config_data['autoValidDate'] == False:
    metadata['validDate'] = config_data['validDate']

if config_data['getForecasterFromUsername'] == False:
    if config_data['forecaster'] == 'random':
        metadata['forecaster']
    else:
        metadata['forecaster'] = config_data['forecaster']
else:
    metadata['forecaster'] = getpass.getuser()

def plot_categorical():
    fig, main_ax, contour_ax = setup_axes.initialize_plot()
    
    for risk in cat_data:
        type = risk[0]
        for outline in risk[1]:
            if outline['geometry']['type'] == "MultiPolygon":
                for geom in outline['geometry']['coordinates']:
                    draw_outlook.plot_outlook(main_ax, contour_ax, geom[0], 'categorical', type)
            else:
                geom = outline['geometry']['coordinates'][0]
                draw_outlook.plot_outlook(main_ax, contour_ax, geom, 'categorical', type)
    
    legend = mpimg.imread(cat_legend_path)
    fig.figimage(legend, zorder=1.5)
    
    draw_outlook.plot_text(contour_ax, metadata, type='Categorical')
    
    plt.savefig(f"{valid_date_fname_friendly}_categorical.png")

def plot_tornado():
    fig, main_ax, contour_ax = setup_axes.initialize_plot()
    
    global tor_cig_plotted_flag
    
    for risk in tor_data:
        type = risk[0]
        for outline in risk[1]:
            geom = outline['geometry']['coordinates'][0]
            if outline['properties']["probability"] in ['CIG1','CIG2','CIG3']:
                if tor_cig_plotted_flag == False:
                    plot_cig_contours(main_ax, contour_ax, tor_data, type='tornado')
                    tor_cig_plotted_flag = True
            else:
                draw_outlook.plot_outlook(main_ax, contour_ax, geom, 'tornado', type)
    
    legend = mpimg.imread(tor_legend_path)
    fig.figimage(legend, zorder=1.5)
    
    draw_outlook.plot_text(contour_ax, metadata, type='tornado')
    
    plt.savefig(f"{valid_date_fname_friendly}_tornado.png")

def plot_wind():
    fig, main_ax, contour_ax = setup_axes.initialize_plot()
    
    global wind_cig_plotted_flag
    
    for risk in wind_data:
        type = risk[0]
        for outline in risk[1]:
            geom = outline['geometry']['coordinates'][0]
            if outline['properties']["probability"] in ['CIG1','CIG2','CIG3']:
                if wind_cig_plotted_flag == False:
                    plot_cig_contours(main_ax, contour_ax, wind_data, type='wind')
                    wind_cig_plotted_flag = True
            else:
                draw_outlook.plot_outlook(main_ax, contour_ax, geom, 'wind', type)
    
    legend = mpimg.imread(wind_legend_path)
    fig.figimage(legend, zorder=1.5)
    
    draw_outlook.plot_text(contour_ax, metadata, type='wind')
    
    plt.savefig(f"{valid_date_fname_friendly}_wind.png")

def plot_hail():
    fig, main_ax, contour_ax = setup_axes.initialize_plot()
    
    global hail_cig_plotted_flag
    
    for risk in hail_data:
        type = risk[0]
        for outline in risk[1]:
            geom = outline['geometry']['coordinates'][0]
            if outline['properties']["probability"] in ['CIG1','CIG2','CIG3']:
                if hail_cig_plotted_flag == False:
                    plot_cig_contours(main_ax, contour_ax, hail_data, type='hail')
                    hail_cig_plotted_flag = True
            else:
                draw_outlook.plot_outlook(main_ax, contour_ax, geom, 'hail', type)
    
    legend = mpimg.imread(hail_legend_path)
    fig.figimage(legend, zorder=1.5)
    
    draw_outlook.plot_text(contour_ax, metadata, type='hail')
    
    plt.savefig(f"{valid_date_fname_friendly}_hail.png")

def plot_cig_contours(main_ax, contour_ax, data, type):
    cig_polys, cig_poly_masks = cig_handler.create_cig_polys(data)
    try:
        for k in range(0,len(cig_polys['cig1'])):
            poly, mask = cig_polys['cig1'][k], cig_poly_masks['cig1'][k]
            draw_outlook.plot_outlook(main_ax, contour_ax, poly, type, 'CIG1', mask=mask)
    except:
        print('No CIG1 to plot (or it errored)')
    try:
        for k in range(0,len(cig_polys['cig2'])):
            poly, mask = cig_polys['cig2'][k], cig_poly_masks['cig2'][k]
            draw_outlook.plot_outlook(main_ax, contour_ax, poly, type, 'CIG2', mask=mask)
    except:
        print('No CIG2 to plot (or it errored)')
    try:
        for k in range(0,len(cig_polys['cig3'])):
            poly, mask = cig_polys['cig3'][k], cig_poly_masks['cig3'][k]
            draw_outlook.plot_outlook(main_ax, contour_ax, poly, type, 'CIG3', mask=mask)
    except:
        print('No CIG3 to plot (or it errored)')

if config_data['generateCategorical']:
    plot_categorical()
if config_data['generateTornado']:
    plot_tornado()
if config_data['generateWind']:
    plot_wind()
if config_data['generateHail']:
    plot_hail()