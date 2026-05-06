import matplotlib as mpl
import json
import os
from matplotlib.patches import Polygon
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import getpass
import matplotlib.image as mpimg

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
styletable_path = os.path.join(SCRIPT_DIR,"styles.json")

json_path = os.path.join(SCRIPT_DIR,"outlook.json")
with open(json_path) as json_file:
    outlook_data = json.loads(json_file.read())

tor_data = outlook_data["forecastCycle"]["days"]["1"]["data"]["tornado"]
wind_data = outlook_data["forecastCycle"]["days"]["1"]["data"]["wind"]
hail_data = outlook_data["forecastCycle"]["days"]["1"]["data"]["hail"]

cig1_hatch_path = os.path.join(SCRIPT_DIR,'img/cig1.png')
cig2_hatch_path = os.path.join(SCRIPT_DIR,'img/cig2.png')
cig3_hatch_path = os.path.join(SCRIPT_DIR,'img/cig3.png')

with open(styletable_path) as json_file:
    styletables = json.loads(json_file.read())

def plot_outlook(main_ax, contour_ax, data, type, risk, mask=None):
    global tor_data, wind_data, hail_data
    styletable = styletables[type][risk]
    
    edgecolor = styletable['linecolor']; fillcolor = styletable['fillcolor']; linewidth = styletable['linewidth']; filled = styletable['filled']; zorder = styletable['zorder']
    if filled == True:
        edge_polygon = Polygon(data, fill=False, edgecolor=edgecolor, facecolor = fillcolor, linewidth=linewidth, linestyle='-', zorder = zorder); edge_polygon.set_transform(ccrs.PlateCarree()._as_mpl_transform(main_ax))
        fill_polygon = Polygon(data, fill=True,  edgecolor=edgecolor, facecolor = fillcolor, linewidth=linewidth, linestyle='-', zorder = zorder); fill_polygon.set_transform(ccrs.PlateCarree()._as_mpl_transform(main_ax))
        contour_ax.add_patch(edge_polygon)
        main_ax.add_patch(fill_polygon)
    if filled == False:
        edge_polygon = Polygon(data, fill=False, edgecolor=edgecolor, facecolor = fillcolor, linewidth=linewidth, linestyle='-', zorder = zorder); edge_polygon.set_transform(ccrs.PlateCarree()._as_mpl_transform(main_ax))
        if not mask == None:
            mask_polygon = Polygon(mask, fill=False, edgecolor='#00000000'); mask_polygon.set_transform(ccrs.PlateCarree()._as_mpl_transform(main_ax))
        contour_ax.add_patch(edge_polygon)
        if risk=='CIG3':
            #print('Bleh')
            cig3_image = mpimg.imread(cig3_hatch_path)
            cig3_image_plot = contour_ax.imshow(cig3_image, zorder = zorder, interpolation='none',
                                                extent = [
                                                    contour_ax.get_xlim()[0],
                                                    contour_ax.get_xlim()[1],
                                                    contour_ax.get_ylim()[0],
                                                    contour_ax.get_ylim()[1],
                                                ])
            cig3_image_plot.set_clip_path(mask_polygon)
        if risk=='CIG2':
            cig2_image = mpimg.imread(cig2_hatch_path)
            cig2_image_plot = contour_ax.imshow(cig2_image, zorder = zorder, interpolation='none',
                                                extent = [
                                                    contour_ax.get_xlim()[0],
                                                    contour_ax.get_xlim()[1],
                                                    contour_ax.get_ylim()[0],
                                                    contour_ax.get_ylim()[1],
                                                ])
            cig2_image_plot.set_clip_path(mask_polygon)
        if risk=='CIG1':
            cig1_image = mpimg.imread(cig1_hatch_path)
            cig1_image_plot = contour_ax.imshow(cig1_image, zorder = zorder, interpolation='none',
                                                extent = [
                                                    contour_ax.get_xlim()[0],
                                                    contour_ax.get_xlim()[1],
                                                    contour_ax.get_ylim()[0],
                                                    contour_ax.get_ylim()[1],
                                                ])
            cig1_image_plot.set_clip_path(mask_polygon)
        del(mask_polygon)

def plot_text(ax,metadata,type):
    day = metadata['day']
    issue_date = metadata['issueDate']
    valid_date = metadata['validDate']
    forecaster = metadata['forecaster']
    
    ax.text(114/1630,153/1110,
            f'SPC Day {str(day)} {type[0].upper()}{type[1:len(type)]} Outlook', 
            fontsize = 27.75, transform=ax.transAxes, fontname = 'Nunito', fontweight = 'regular')
    ax.text(114/1630,115/1110,
            f'Issued: {issue_date[11:13]}{issue_date[14:16]}Z {issue_date[5:7]}/{issue_date[8:10]}/{issue_date[0:4]}', 
            fontsize = 27.75, transform=ax.transAxes, fontname = 'Nunito', fontweight = 'regular')
    ax.text(114/1630,77/1110,
            f'Valid: 1630Z Sun 04/24 - 1200Z Mon 04/25', #UPDATE LATER TO REFLECT ACTUAL VALID CYCLE
            fontsize = 27.75, transform=ax.transAxes, fontname = 'Nunito', fontweight = 'regular')
    ax.text(114/1630,39/1110,
            f'Forecaster: {forecaster}', 
            fontsize = 27.75, transform=ax.transAxes, fontname = 'Nunito', fontweight = 'regular')