# gpe_lib/notebook/colab/__init__.py
# --- IMPORTS ---------------------------------------------------------------
import os
from google.colab import files

# --- DECLARATIONS ----------------------------------------------------------

# --- FUNCTIONS -------------------------------------------------------------
def settings():
    import matplotlib.pyplot as plt
    plt.rcParams["figure.figsize"] = (3,3)

    from google.colab import output, files
    output.enable_custom_widget_manager()
    
# --- COMMANDS --------------------------------------------------------------
settings()

try:
    os.system("pip install ipympl")
    import ipympl
except: pass