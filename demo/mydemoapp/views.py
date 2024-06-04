from django.shortcuts import render, HttpResponse
from .models import TodoItem


import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import pandas as pd
from jinja2 import Template


# Create your views here.
def home(request):
    return HttpResponse("hello wor rcr crc r crc rc ld")

def newhome(request):
    items = TodoItem.objects.all()
    return render(request, "home.html", {"todos": items })


def dash_view(request):
    return render(request, 'dash_graph.html')



def plotly_view(request):
    # Generate a Plotly figure
    fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 1, 2]))


    # Generate a Plotly figure
    fig3 = go.Figure(data=go.Bar(x=[1, 2, 3], y=[4, 1, 2]))

    df = pd.DataFrame({
  "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
  "Contestant": ["Alex", "Alex", "Alex", "ANGELA", "ANGELA", "ANGELA"],
  "Number Eaten": [2, 1, 3, 1, 3, 2],
  })


    # Plotly Express
    fig2 = px.bar(df, x="Fruit", y="Number Eaten", color="Contestant", barmode="group")



    # Convert the figure to JSON
    graph_json = pio.to_json(fig)
    graph_json2 = pio.to_json(fig2)

    return render(request, 'plotly_template.html', {'graph_json': graph_json, 'graph_json2': graph_json2})



def jinja_view(request):
    # Sample data
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Number Eaten": [5, 3, 2, 4, 2, 5],
        "Contestant": ["A", "A", "A", "B", "B", "B"]
    })

    # Generate the Plotly figure
    fig = px.bar(df, x="Fruit", y="Number Eaten", color="Contestant", barmode="group")

    # Convert the Plotly figure to HTML
    fig_html = fig.to_html(full_html=False)

    # Pass the HTML to the template
    return render(request, 'plotly_jinja.html', {'fig_html': fig_html})
