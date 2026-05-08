import matplotlib as mpl
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import cartopy.feature as cfeature
import os
#import cartopy.io.shapereader as shpreader

mpl.rcParams['figure.dpi'] = 72
mpl.rcParams['savefig.dpi'] = 72

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
fill_img_path = os.path.join(SCRIPT_DIR,"img/basemap_fill.png")
outline_img_path = os.path.join(SCRIPT_DIR,"img/basemap_outline.png")

def initialize_plot():
    global fig
    global main_ax
    global proj
    global fuck

    fig = plt.figure(figsize=(1630/72, 1110/72))#, facecolor='#ffffff', edgecolor='#000000')
    
    proj = ccrs.LambertConformal()

    main_ax = fig.add_axes([0, 0, 1, 1], projection=proj, zorder=0)
    main_ax.patch.set_alpha(0)
    
    contour_ax = fig.add_axes([0, 0, 1, 1], projection=proj, zorder=2)
    contour_ax.patch.set_alpha(0)
    
    fig.patch.set_color('#729fcf')
    
    zoom = 1/1.0124
    
    center = (-84000,-35000)
    
    main_ax.set_ylim(center[1]-2500000*zoom/(1630/1110),
                     center[1]+2500000*zoom/(1630/1110))
    main_ax.set_xlim(center[0]-2500000*zoom,
                     center[0]+2500000*zoom)
    
    contour_ax.set_ylim(center[1]-2500000*zoom/(1630/1110),
                     center[1]+2500000*zoom/(1630/1110))
    contour_ax.set_xlim(center[0]-2500000*zoom,
                     center[0]+2500000*zoom)
    
    fuck = mpimg.imread(fill_img_path)
    fig.figimage(fuck, zorder=-1)
    
    fuck2 = mpimg.imread(outline_img_path)
    fig.figimage(fuck2, zorder=1)
    
    #main_ax.add_feature(lakes_reservoirs_feature, edgecolor='#3a3a3a', facecolor='#3a3a3a00', linewidth=1.1, zorder=0)
    #main_ax.add_feature(cfeature.LAND.with_scale('10m'), edgecolor='#88888800', facecolor='#888888', linewidth=1.1, zorder=-8)
    
    #main_ax.add_feature(forecast_zones_feature, edgecolor = '#000000', linewidth=2, zorder=9)
    
    #main_ax.add_feature(forecast_zones_feature, edgecolor='#3a3a3a', facecolor = '#3a3a3a00', linewidth=1.1, zorder=0)
    
    return [fig, main_ax, contour_ax]