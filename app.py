from flask import Flask
app=Flask(__name__)

@app.route('/admin')
def admin():
    return  'this is amdin '

#hello i am here

@app.route('/teacher')
def admin():
    return  'this is amdin '
@app.route('/stu')
def stu():
    return  'this is amdin '

@app.route("/")
def start():
    return 'please subscribe'











if __name__=='__main__':
    app.run()