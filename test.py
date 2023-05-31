from flask import render_template
from flask import Flask, request
import json
import submit_sql
import login_sql
import add_favorite_sql

app = Flask(__name__,static_folder='./', static_url_path='/',template_folder='./')

# @app.route("/index")
@app.route("/submit", methods=['POST'])
def submit():
    #return request.values['username'] + request.values['email'] + request.values['password']
    isSubmit = submit_sql.submit(request.values['username'], request.values['email'], request.values['password'])
    dic = {}
    dic['isSubmit'] = isSubmit
    dataJson = json.dumps(dic, ensure_ascii = False)
    print(dataJson)
    return render_template('index.html', data = dataJson)

@app.route("/login", methods=['POST'])
def login():
    isLogin = login_sql.login(request.values['email'], request.values['password'])
    dic = {}
    dic['isLogin'] = isLogin
    dataJson = json.dumps(dic, ensure_ascii = False)
    print(dataJson)
    return render_template('index.html', data = dataJson)

@app.route("/addfavorite", methods=['POST'])
def addFavorite():
    isAddFavorite = add_favorite_sql.addFavorite(request.values['email'], request.values['placeId'])
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


