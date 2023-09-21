from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Hello World!'

# app.run(host='0.0.0.0', port=81)
#name will be mostly main only you can directly have app.run instead of this if condition below
if __name__ == "__main__":
	app.run( )
