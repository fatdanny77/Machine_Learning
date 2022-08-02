import pyecharts
## Gauge

import pyecharts.options as opts
from pyecharts.charts import Gauge
from pyecharts.charts import Bar, Line, Grid
import pandas as pd
import numpy as np
import eplot # 方便Pandas使用pyecharts

# Jupyter Lab 環境設置
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
