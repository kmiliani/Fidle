

# ==================================================================
#  ____                 _   _           _  __        __         _
# |  _ \ _ __ __ _  ___| |_(_) ___ __ _| | \ \      / /__  _ __| | __
# | |_) | '__/ _` |/ __| __| |/ __/ _` | |  \ \ /\ / / _ \| '__| |/ /
# |  __/| | | (_| | (__| |_| | (_| (_| | |   \ V  V / (_) | |  |   <
# |_|   |_|  \__,_|\___|\__|_|\___\__,_|_|    \_/\_/ \___/|_|  |_|\_\
#                                                      Configuration
# ==================================================================
# Few configuration stuffs for the Fidle practical work notebooks
# Jean-Luc Parouty 2020


# ---- Version -----------------------------------------------------
#
VERSION = '0.6.1 DEV'

# ---- Default notebook name ---------------------------------------
#
DEFAULT_NOTEBOOK_NAME = "Unknown"

# ---- Styles ------------------------------------------------------
#
FIDLE_MPLSTYLE = '../fidle/mplstyles/custom.mplstyle'
FIDLE_CSSFILE  = '../fidle/css/custom.css'

# ---- Catalog file, a json description of all notebooks
#
CATALOG_FILE   = '../fidle/log/catalog.json'

# ---- CI Done files, to keep track of finished notebooks -----------
# Used for continous integration
#
FINISHED_FILE  = '../fidle/log/finished.json'

# ---- CI Report
#
CI_REPORT      = '../fidle/log/ci_report.html'

# ---- Defaul mode (full|smart)
#      Overided by env : FIDLE_RUNNING_MODE
#
DEFAULT_RUNNING_MODE = 'full'

# ---- Save figs or not (yes|no)
#      Overided by env : FIDLE_SAVE_FIGS
#      
DEFAULT_SAVE_FIGS    = 'yes'