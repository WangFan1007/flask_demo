from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "funny"

@app.route('/login',methods=['get','post'])
def login():
    # return "Login"
    if request.method == 'GET':
        return render_template('login.html')
    # request.args
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'alex' and pwd == '666':
        session['user'] = user
        return redirect('index')
    print(user,pwd)
    return render_template('login.html',error="用户名密码错误")

@app.route('/index')
def index():
    user = session.get('user')
    if not user:
        # pass
        return redirect('login')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()