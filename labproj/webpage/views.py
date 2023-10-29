from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def webpage_view(request):
    name = "abdulrahman"
    my_list = ["twitter blog","video games store", "chat rooms"]
    context = {"my_list": my_list}
    x = HttpResponse(f"""
    <html>                 
        <head></head>
        <body>
            <h1> hi my name is:<h1> 
            <h3>{name} </h3>                 
            <p>
            welcome to the lab
            <p>
            <p>below you will see a list of my project ideas<p>
            <h3>{my_list}<h3>
            <a href="http://twitter.com/"> twitter link</a>
        <body>
    <html>

""")
    return x