# SPC Outlook Graphic Generator
A tool to create SPC-like convective outlook graphics using Graphical Forecast Creator JSON files.

# Installation
You need at least Python 3.10. Once you have installed Python, install the "cartopy" library; all other dependencies should come with it. On windows, use "pip install cartopy" (no quotes) in command prompt or powershell. A batch script has been provided ("install_dependencies.bat") to do this for you if computers are too scary.  If you're on Linux, you probably don't need my help (hell, you probably already have all the requirements); if you're on Mac, good luck. You're on your own.

# Usage
In order to use the script, you need to do (as of now) three things:
1. Set up the outlook
2. Edit config.json
3. Set the valid cycle in draw_outlook.py (temporary)

Setting up the outlook is relatively easy. Go to https://gfc.weatherboysuper.com/forecast, create a forecast outlook, and then save it with the name "outlook.json". Place the file into the directory where you have the repository installed; replace if necessary.
A template outlook.json has been provided because why not.

Editing config.json isn't too big an issue. Most of the options should be self-explanatory. It is worth mentioning that currently, the program has no way to automatically regenerate the JSON should something go awry; if the file gets messed up, you're going to have to redownload it from this repository. Also note that currently the custom logo options and the valid date options don't do anything. I have yet to go through the nightmare hell torture of learning the datetime library.

Setting the valid cycle is the most annoying part. Open draw_outlook.py in a text editor, and head to line 81. There should be a string that says 'Valid: 1630Z Wed 04/27 - 1200Z Thu 04/28'. Change that to whatever time period your outlook is valid for. Note that if anything outside the quotes is changed, the program is very likely to crash. I am not responsible for any issues that arise from modifying the script. This will not be necessary in a future release, but I'm too lazy to do it at the moment.

Once you have all of that done, you should be able to run outlook_graphic_generator.py. It will output up to four PNG files, depending on what is specified in the config.
If double-clicking the file doesn't work, use outlook_graphic_generator.bat instead.

# Warning(s)
The script is rather cumbersome to use right now. I'm figuring that out; my apologies. User-friendly design has never been my strong suit.
Additionally, I think it might be a federal crime to release the generated images on social media? I don't know. Be careful. There will be functionality in the future for a custom, non-NOAA logo, but I don't know when I'll get around to doing that.

# TODO
- Add great salt lake (i couldn't find a good shapefile for it lmao)
- Filter risk contours to US borders
- "Probability too low"
- Fix issues with multiple nested CIG contours
- Days 2/3 plotting
- GUI?
- Old format?