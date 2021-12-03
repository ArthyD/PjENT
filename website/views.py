from flask import Blueprint, render_template,request, url_for
import os
import json

views = Blueprint('views',__name__)

@views.route('/')
def home():
    
    f = open(os.path.dirname(__file__)+'/config.json')
    configJson = json.load(f)
    print(configJson)
    f.close()
    return render_template("mainPage.html", configJson = configJson)