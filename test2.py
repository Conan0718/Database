from flask import render_template
from flask import Flask, request
import json

app = Flask(__name__,static_folder='./', static_url_path='/',template_folder='./')

# @app.route("/index")
@app.route("/submit", methods=['POST'])
def submit():
    #return request.values['username'] + request.values['email'] + request.values['password']
    isSubmit = True
    dic = {}
    dic['isSubmit'] = isSubmit
    dataJson = json.dumps(dic, ensure_ascii = False)
    print(dataJson)
    return dataJson
    #return render_template('index.html', data = dataJson)

@app.route("/login", methods=['POST'])
def login():
    isLogin = True
    dic = {}
    dic['isLogin'] = isLogin
    dataJson = json.dumps(dic, ensure_ascii = False)
    print(dataJson)
    return dataJson

@app.route("/addfavorite", methods=['POST'])
def addFavorite():
    isAddFavorite = True
    dic = {}
    dic['isAddFavorite'] = isAddFavorite
    dataJson = json.dumps(dic, ensure_ascii = False)
    print(dataJson)
    return render_template('index.html', data = dataJson)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


