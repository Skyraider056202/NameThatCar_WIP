from flask import Flask, redirect, url_for, request, jsonify, render_template, make_response
import json
import sys
app = Flask(__name__)

@app.route("/", methods= ['GET', 'POST']) 
def mainpage():   
    from pyt_back import game_infrastructure
    data = json.dumps(game_infrastructure.info_dict)
    targetcar = json.dumps(game_infrastructure.target_car)

    return render_template("index.html", PageTitle = 'Main Game', data=data, targetcar=targetcar)
    
    
if __name__ == '__main__':
    app.run(debug=True)
