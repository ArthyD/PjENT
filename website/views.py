from flask import Blueprint, render_template,request, url_for
import os
import json

views = Blueprint('views',__name__)

@views.route('/',methods=['POST','GET'])
def home():
    f = open(os.path.dirname(__file__)+'/config.json')
    configJson = json.load(f)
    currentlySelected = configJson.pop("SelectedConfig",None)
    f.close()
    if request.method == 'POST':
        configName = request.form.get("button")
        f = open(os.path.dirname(__file__)+'/config.json','w')
        configSelected= {"SelectedConfig":configName}
        configJson.update(configSelected)
        print(configJson)
        json.dump(configJson,f)
        currentlySelected = configJson.pop("SelectedConfig",None)
        f.close()
    return render_template("mainPage.html", configJson = configJson, current = currentlySelected)

@views.route('/controle',methods=['POST','GET'])
def controle():
    return render_template("controle.html")

