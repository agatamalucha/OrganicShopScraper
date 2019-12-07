import os
from flask import Flask, render_template
import json


app = Flask(__name__)  # initiate Flask app
#Bootstrap(app)  # initiate Bootstrap in order to use WTF flask forms

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')  # system configurations
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
# app.config['S3_BUCKET_NAME'] = os.environ.get('S3_BUCKET_NAME')
# app.config["S3_LOCATION"] = 'http://{}.s3.amazonaws.com/'.format(os.environ.get('S3_BUCKET_NAME'))
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# app.config['DEBUG'] = True  # this allow to show any errors in the app




my_collection = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
my_list = ['1', '2']
variable = "Lukaszku i co teraz"



@app.route('/')
def index():
    with open('shop.json') as fh:
        y = json.load(fh)

    return render_template('base.html', listing=y)                # find_json = find_json, my_type = my_type
    # return (json.dumps(y , indent=4, sort_keys=True))

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('base.html')


if __name__ =='__main__':
    app.run(debug=True)



 # if y:                                           ---- to check if app sees json and to shows what type
    #     find_json = "Jest"
    #     my_type = str(type(y))
    # else:
    #     find_json = "Nie Ma"
    #     my_type = "None"