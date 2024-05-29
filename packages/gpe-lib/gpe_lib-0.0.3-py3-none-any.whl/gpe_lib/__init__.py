# gpe_lib/__init__.py
# --- IMPORTS ---------------------------------------------------------------
from . import notebook
import os, requests, matplotlib, matplotlib.font_manager, matplotlib.colors

# --- DECLARATIONS ----------------------------------------------------------
NIDEC = True

colors_dict = {"ngreen":"#009B49", "ngrey":'#666666', "nblack":"#000000", "egreen":"#008691","yellow":"#BEBE00","blue":"#59B2D8","red":"#FF0000"}
colors = list(colors_dict.values())
nidec_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("nidec", [np.array([0.243,0.243,0.243])+np.array([-0.243,0.757,0.234])*i/255 for i in range(256)])

# --- FUNCTIONS -------------------------------------------------------------
def set_nidec_color_cycle():
    import matplotlib.pyplot as plt
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=colors_list)

def __use_font(family,fonts):
    fonts_dir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.path.pardir,os.path.pardir,"files"))
    if not os.path.exists(fonts_dir): os.makedirs(fonts_dir)
        
    for fn,url in fonts:
        filename = os.path.join(fonts_dir,fn)
        if not os.path.exists(filename):
            print(f"Downloading {fn}...")
            with open(filename, "wb") as f: [f.write(chunk) if chunk else None for chunk in requests.get(url, stream=True).iter_content(chunk_size=8192)]
        matplotlib.font_manager.fontManager.addfont(filename)
    matplotlib.rc("font", family=family)
    
def use_times(): 
    __use_font("Times New Roman",[("Times New Roman.ttf","https://github.com/justrajdeep/fonts/raw/master/Times%20New%20Roman.ttf"),("Times New Roman - Bold.ttf","https://github.com/justrajdeep/fonts/raw/master/Times%20New%20Roman%20Bold.ttf"),("Times New Roman Italic.ttf","https://github.com/justrajdeep/fonts/raw/master/Times%20New%20Roman%20Italic.ttf"),("Times New Roman Bold Italic.ttf","https://github.com/justrajdeep/fonts/raw/master/Times%20New%20Roman%20Bold%20Italic.ttf")])
    matplotlib.rcParams.update({"font.family":"Times New Roman","mathtext.rm":"Times New Roman","mathtext.it":"Times New Roman:italic","mathtext.bf":"Times New Roman:bold","mathtext.fontset":"custom"})

def use_comfortaa():
    __use_font("Comfortaa",[("Comfortaa-Regular.ttf","https://github.com/googlefonts/comfortaa/raw/main/fonts/TTF/Comfortaa-Regular.ttf"),("Comfortaa-Bold.ttf","https://github.com/googlefonts/comfortaa/raw/main/fonts/TTF/Comfortaa-Bold.ttf")])
    matplotlib.rcParams.update({"font.family":"Comfortaa","mathtext.rm":"Comfortaa","mathtext.it":"Comfortaa:italic","mathtext.bf":"Comfortaa:bold","mathtext.fontset":"custom"})


# --- COMMANDS --------------------------------------------------------------
if NIDEC:
    set_nidec_color_cycle()
use_times()