from pathlib import Path
import csv
import pandas as pd
import plotly.express as px

# 对csv文件的数据进行处理
path = Path('下载数据/eq_data/world_fires_1_day.csv')
try:
    lines = path.read_text().splitlines()
except:
    lines = path.read_text(encoding='utf8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# # 查看表头包含内容
# for index, header in enumerate(header_row):
#     print(index, header)

# 自动获取索引

# 提取时间，经纬度，亮度
times, lats, lons, brights = [], [], [], []
for row in reader:
    try:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
    except ValueError:
        # 对于无效行，显示无效信息
        print(f"Invalid data for {row[5]}")
    else:
        times.append(row[5])
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# 将数据打包
data = pd.DataFrame(
    data=zip(times, lats, lons, brights), columns=['时间', '纬度', '经度', '灾情']
)

# 进行绘图
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球火灾',
    hover_name='灾情',
    size='灾情',
    size_max=10,
    color='灾情',
)

fig.show()