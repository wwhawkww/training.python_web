from flask import Flask

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/profile/<username>')
def show_profile(username):
    return "My username is %s" % username

@app.route('/div/<float:val>/')
def divide(val):
    return "%0.2f divided by 2 is %0.2f" %(val, val / 2)
    
@app.route('/blog/entry/<int:id>/', methods=['GET',])
def read_entry(id):
    return "reading entry %d" % id

@app.route('/blog/entry/<int:id>/',methods=['POST',])
def write_entry(id):
    return 'writing entry %d' % id


if __name__ == '__main__':
    app.run(debug=True)
    # to get this to work on the virtual machine:
    # app.run(host="0.0.0.0", debug=True)
    #This line allows you to bind to the VM host, then you can
    # hit it with your browser
    
    