# SPC Outlook Graphic Generator
A tool to create SPC-like convective outlook graphics using Graphical Forecast Creator JSON files.

# Installation
If using the executable bundle (NOT CURRENTLY RECOMMENDED), you don't need anything else (other than the three json files).
If running from source, you need at least Python 3.10. Once you have installed Python, install the "cartopy" library; all other dependencies should come with it. On windows, use "pip install cartopy" (no quotes) in command prompt or powershell. A batch script has been provided ("install_dependencies.bat") to do this for you if computers are too scary.  If you're on Linux, you probably don't need my help (hell, you probably already have all the requirements); if you're on Mac, good luck. You're on your own.

# Usage
In order to use the script, you need to do (as of now) two things:
1. Set up the outlook
2. Edit config.json

Setting up the outlook is relatively easy. Go to https://gfc.weatherboysuper.com/forecast, create a forecast outlook, and then save it with the name "outlook.json". Place the file into the directory where you have the repository installed; replace if necessary.
(NOTE: if using the binary, you need to put the outlook.json in the "_internal" directory.)
A template outlook.json has been provided because why not.

Editing config.json isn't too big an issue. Most of the options should be self-explanatory. It is worth mentioning that currently, the program has no way to automatically regenerate the JSON should something go awry; if the file gets messed up, you're going to have to redownload it from this repository. Also note that currently the custom logo option doesn't do anything.

Once you have all of that done, you should be able to run the script, either from the .exe or the "outlook_graphic_generator.py" file. If you're running the script,. It will output up to four PNG files, depending on what is specified in the config. If double-clicking the file doesn't work, use outlook_graphic_generator.bat instead.

# Warning(s)
The script is rather cumbersome to use right now. I'm figuring that out; my apologies. User-friendly design has never been my strong suit.
Additionally, I think it might be a federal crime to release the generated images on social media? I don't know. Be careful. There will be functionality in the future for a custom, non-NOAA logo, but I don't know when I'll get around to doing that.

# TODO
- Add great salt lake (i couldn't find a good shapefile for it lmao)
- "Probability too low"
- Fix issues with multiple nested CIG contours
- Days 2/3 plotting
- GUI?
- Old format?
- geojson importing
- PWOs?