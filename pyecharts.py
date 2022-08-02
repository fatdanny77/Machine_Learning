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


###############################################################
bar = Bar()
bar.add_xaxis(["襯衫", "羊毛衫", "雪紡", "褲子", "鞋子", "襪子"])
bar.add_yaxis("商店A", [5, 50, 100, 90, 110, 30])
bar.add_yaxis("商店B", [10, 30, 150, 100, 70, 50])
bar.set_global_opts(title_opts=opts.TitleOpts(title="單獨調用 Bar2結果", subtitle="商店A中六樣商品數"))
bar.load_javascript()
# bar.render("bar2.html")
# bar.render('bar.html')
###############################################################
bar.render_notebook()


###############################################################
class Color():
    def __init__(self, score):
        self.score = score
    
    # 可以利用self取得自己這個類別裡面的變數
    def score_color(self):
        if self.score <= 60:
            return '#FFA1A1'
        elif 60 < self.score <= 100:
            return '#FFD59E'
        elif 100 < self.score :
            return '#B3E283'   
    

print(AC_Death)
###############################################################


AC_Death = Color(94).score_color()
AC_Health = Color(48).score_color()
AC_One = Color(90).score_color()

AC = (
    Gauge(
#         init_opts = opts.InitOpts(width = '800px',height = '400px')
    )
    .add(
        'AC通路保障型',
        data_pair = [('死亡險', 94)],
        radius="80%", # 设置比例大小
        start_angle=-180, end_angle=-360,
        min_=0,max_= 200, # 设置起始、终止刻度
        title_label_opts=opts.GaugeTitleOpts(
                offset_center=['-50%','25%'],
                font_size=20, color='black', font_family='微軟正黑體'
        ),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#FFA1A1"), (0.5, "#FFD59E"), (1, '#B3E283')], width=30  # 设置区间颜色、仪表宽度
            )
        ),
        detail_label_opts=(
            opts.GaugeDetailOpts(
                offset_center=['-50%','38%'], 
                formatter = '  {value}%  ', 
                font_family='Arial',
                font_size=18,
                color = 'black',
                border_radius = 10,
                background_color= AC_Death,
                # 文字块的背景阴影颜色。
                shadow_color = "black",
                # 文字块的背景阴影长度。
                shadow_blur = 2,
                # 文字块的背景阴影 X 偏移。
                shadow_offset_x = 2,
                # 文字块的背景阴影 Y 偏移。
                shadow_offset_y = 2   
            ) #內部Label
        ),
        pointer = opts.GaugePointerOpts(
            length='70%',
            width = 5
        )
    )
    .add(
        'AC通路保障型',
        data_pair = [('健康險', 48)],
        radius="80%", # 设置比例大小
        start_angle=-180, end_angle=-360,
        min_=0,max_= 200, # 设置起始、终止刻度

        title_label_opts=opts.GaugeTitleOpts(
                font_size=20, color="black", font_family='微軟正黑體', is_show=True,  # 设置字体、颜色、大小
                offset_center=['0%','25%']
            ),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#FFA1A1"), (0.5, "#FFD59E"), (1, '#B3E283')], width=30  # 设置区间颜色、仪表宽度
            )
        ),
        detail_label_opts=(
            opts.GaugeDetailOpts(
                offset_center=['0%','38%'], 
                formatter = '  {value}%  ', 
                font_family='Arial',
                font_size=18,
                color = 'black',
                border_radius = 10,
                background_color= AC_Health,
                # 文字块的背景阴影颜色。
                shadow_color = "black",
                # 文字块的背景阴影长度。
                shadow_blur = 2,
                # 文字块的背景阴影 X 偏移。
                shadow_offset_x = 2,
                # 文字块的背景阴影 Y 偏移。
                shadow_offset_y = 2
            )
            
        ), #內部Label
        pointer = opts.GaugePointerOpts(
            length='70%',
            width = 5
        )  
    ) 
    .add(
        'AC通路保障型',
        data_pair = [('一年期險', 90)],
        radius="80%", # 设置比例大小
        start_angle=-180, end_angle=-360,
        min_=0,max_= 200, # 设置起始、终止刻度

        title_label_opts=opts.GaugeTitleOpts(
                font_size=20, color="black", font_family='微軟正黑體', is_show=True,  # 设置字体、颜色、大小
                offset_center=['50%','25%']
            ),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#FFA1A1"), (0.5, "#FFD59E"), (1, '#B3E283')], width=30  # 设置区间颜色、仪表宽度
            )
        ),
        detail_label_opts=(
            opts.GaugeDetailOpts(
                offset_center=['50%','38%'], 
                formatter = '  {value}%  ', 
                font_family='Arial',
                font_size=18,
                color = 'black',
                border_radius = 10,
                background_color= AC_One,
                # 文字块的背景阴影颜色。
                shadow_color = "black",
                # 文字块的背景阴影长度。
                shadow_blur = 2,
                # 文字块的背景阴影 X 偏移。
                shadow_offset_x = 2,
                # 文字块的背景阴影 Y 偏移。
                shadow_offset_y = 2
            )
        ), #內部Label
        pointer = opts.GaugePointerOpts(
            length='70%',
            width = 5
        )
    )   
    .set_global_opts(
        title_opts=opts.TitleOpts(         
            title='AC通路保障型業績達成率',
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=25, font_family='SimHei',
                color='black', font_weight='bold',
            ),
        pos_left="300", pos_top="8",
        ),
        legend_opts=opts.LegendOpts(        
            is_show=False
        ),
        tooltip_opts=opts.TooltipOpts(    
            is_show=True,
            formatter='{a} <br/>{b} 達成率 : {c}%'
        )
    )
)
AC.render_notebook()


BR_Death = Color(166).score_color()
BR_Health = Color(107).score_color()
BR_Long = Color(10).score_color()
BR_One = Color(151).score_color()

#寫個if變數，決定儀表板長度

BR = (
    Gauge(
#         init_opts = opts.InitOpts(width = '800px',height = '400px')
    )
    .add(
        'BR通路保障型',
        data_pair = [('死亡險', 166)],
        radius="80%", # 设置比例大小
        start_angle=-180, end_angle=-360,
        min_=0,max_= 200, # 设置起始、终止刻度
        title_label_opts=opts.GaugeTitleOpts(
                offset_center=['-75%','25%'],
                font_size=20, color='black', font_family='微軟正黑體'
        ),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#FFA1A1"), (0.5, "#FFD59E"), (1, '#B3E283')], width=30  # 设置区间颜色、仪表宽度
            )
        ),
        detail_label_opts=(
            opts.GaugeDetailOpts(
                offset_center=['-75%','38%'], 
                formatter = '  {value}%  ', 
                font_family='Arial',
                font_size=18,
                color = 'black',
                border_radius = 10,
                background_color= BR_Death,
                # 文字块的背景阴影颜色。
                shadow_color = "black",
                # 文字块的背景阴影长度。
                shadow_blur = 2,
                # 文字块的背景阴影 X 偏移。
                shadow_offset_x = 2,
                # 文字块的背景阴影 Y 偏移。
                shadow_offset_y = 2   
            ) #內部Label
        ),
        pointer = opts.GaugePointerOpts(
            length='70%',
            width = 5
        )
    )
    .add(
        'BR通路保障型',
        data_pair = [('健康險', 107)],
        radius="80%", # 设置比例大小
        start_angle=-180, end_angle=-360,
        min_=0,max_= 200, # 设置起始、终止刻度

        title_label_opts=opts.GaugeTitleOpts(
                font_size=20, color="black", font_family='微軟正黑體', is_show=True,  # 设置字体、颜色、大小
                offset_center=['-25%','25%']
            ),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#FFA1A1"), (0.5, "#FFD59E"), (1, '#B3E283')], width=30  # 设置区间颜色、仪表宽度
            )
        ),
        detail_label_opts=(
            opts.GaugeDetailOpts(
                offset_center=['-25%','38%'], 
                formatter = '  {value}%  ', 
                font_family='Arial',
                font_size=18,
                color = 'black',
                border_radius = 10,
                background_color= BR_Health,
                # 文字块的背景阴影颜色。
                shadow_color = "black",
                # 文字块的背景阴影长度。
                shadow_blur = 2,
                # 文字块的背景阴影 X 偏移。
                shadow_offset_x = 2,
                # 文字块的背景阴影 Y 偏移。
                shadow_offset_y = 2
            )
            
        ), #內部Label
        pointer = opts.GaugePointerOpts(
            length='70%',
            width = 5
        )
        
    ) 
    .add(
        'BR通路保障型',
        data_pair = [('長照險', 10)],
        radius="80%", # 设置比例大小
        start_angle=-180, end_angle=-360,
        min_=0,max_= 200, # 设置起始、终止刻度

        title_label_opts=opts.GaugeTitleOpts(
                font_size=20, color="black", font_family='微軟正黑體', is_show=True,  # 设置字体、颜色、大小
                offset_center=['25%','25%']
            ),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#FFA1A1"), (0.5, "#FFD59E"), (1, '#B3E283')], width=30  # 设置区间颜色、仪表宽度
            )
        ),
        detail_label_opts=(
            opts.GaugeDetailOpts(
                offset_center=['25%','38%'], 
                formatter = '  {value}%  ', 
                font_family='Arial',
                font_size=18,
                color = 'black',
                border_radius = 10,
                background_color= BR_Long,
                # 文字块的背景阴影颜色。
                shadow_color = "black",
                # 文字块的背景阴影长度。
                shadow_blur = 2,
                # 文字块的背景阴影 X 偏移。
                shadow_offset_x = 2,
                # 文字块的背景阴影 Y 偏移。
                shadow_offset_y = 2
            )
        ), #內部Label
        pointer = opts.GaugePointerOpts(
            length='70%',
            width = 5
        )
    )        
    .add(
        'BR通路保障型',
        data_pair = [('一年期險', 151)],
        radius="80%", # 设置比例大小
        start_angle=-180, end_angle=-360,
        min_=0,max_= 200, # 设置起始、终止刻度

        title_label_opts=opts.GaugeTitleOpts(
                font_size=20, color="black", font_family='微軟正黑體', is_show=True,  # 设置字体、颜色、大小
                offset_center=['75%','25%']
            ),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#FFA1A1"), (0.5, "#FFD59E"), (1, '#B3E283')], width=30  # 设置区间颜色、仪表宽度
            )
        ),
        detail_label_opts=(
            opts.GaugeDetailOpts(
                offset_center=['75%','38%'], 
                formatter = '  {value}%  ', 
                font_family='Arial',
                font_size=18,
                color = 'black',
                border_radius = 10,
                background_color= BR_One,
                # 文字块的背景阴影颜色。
                shadow_color = "black",
                # 文字块的背景阴影长度。
                shadow_blur = 2,
                # 文字块的背景阴影 X 偏移。
                shadow_offset_x = 2,
                # 文字块的背景阴影 Y 偏移。
                shadow_offset_y = 2
            )
        ), #內部Label
        pointer = opts.GaugePointerOpts(
            length='70%',
            width = 5
        )
    )   
    .set_global_opts(
        title_opts=opts.TitleOpts(         
            title='BR通路保障型業績達成率',
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=25, font_family='SimHei',
                color='black', font_weight='bold',
            ),
        pos_left="300", pos_top="8",
        ),
        legend_opts=opts.LegendOpts(        
            is_show=False
        ),
        tooltip_opts=opts.TooltipOpts(    
            is_show=True,
            formatter='{a} <br/>{b} 達成率 : {c}%'
        )
    )
)
BR.render_notebook()


from pyecharts.charts import Page
page = Page()  
page.add(AC)
page.add(BR)
page.render_notebook()













