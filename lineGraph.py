import pandas as pd
import plotly_express as px

a=pd.read_csv("line_chart.csv")
graph=px.line(a,x="Year",y="Per capita income",color="Country",title="Per capita income of countries in different years")
graph.show()