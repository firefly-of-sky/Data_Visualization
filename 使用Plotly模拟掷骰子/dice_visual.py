import plotly.express as px

from die import Die

# 创建一个D6 和一个 D10 
die_1 = Die(8)
die_2 = Die(8)

# 掷几次骰子并将结果存储在一个列表中
results = []
results = [die_1.roll() + die_2.roll() for roll_num in range(10_000)]

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# 对结果进行可视化
title = "Results of Rolling a D6 and a D 10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# 进一步定制图形
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html("dice_visual_d6d10.html")