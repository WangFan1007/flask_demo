from flask import Flask,views

app = Flask(__name__)


class UserView(views.MethodView):
    def get(self,*args,**kwargs):
        return 'get'

    def post(self,*args,**kwargs):
        return 'post'


app.add_url_rule('/userview',None,UserView.as_view('test'))


if __name__ == '__main__':
    app.run()