import pandas as pd
import plotly_express as px

a=pd.read_csv("data.csv")
graph=px.scatter(a,x="Population",y="Per capita", size="Percentage",color="Country",size_max=60)
graph.show()
