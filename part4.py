# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets

py.sign_in('anuzk13', 'YXTcJoHfZLBlDhVHrDc6')
nouns = []
freq = []
with open('part1.csv') as n_file:
    first_row = next(n_file)
    for row in n_file:
        nouns.append(row.split(',')[0])
        freq.append(row.split(',')[1])
bar_data = go.Bar(x=nouns, y=freq)
fig_data = [bar_data]
layout = go.Layout(title='Tweets Nouns frequency distribution', width=800, height=640)
fig = go.Figure(data=fig_data, layout=layout)

py.image.save_as(fig, filename='part4_viz_image.png')
