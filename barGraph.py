import pandas as pd
import plotly_express as px

a=pd.read_csv("data.csv")
graph=px.bar(a,x="Country",y="InternetUsers")
graph.show()