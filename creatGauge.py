from pyecharts import options as opts
from pyecharts.charts import Gauge
from pyecharts.commons.utils import JsCode
import random

def create_gauge(uv_index) -> Gauge:
    c = (
        Gauge()
        .add("", [("UV Index", uv_index)], title_label_opts=opts.LabelOpts(formatter="{value}"))
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}"),
        )
    )
    return c

# 模拟实时更新仪表盘数据
gauge = None
while True:
    uv_index = random.uniform(0, 10)  # 模拟获取UV指数数据
    if not gauge:
        gauge = create_gauge(uv_index)
        gauge.render('gauge.html')
    else:
        gauge = create_gauge(uv_index)
        gauge.render('gauge.html', re_render=True)
