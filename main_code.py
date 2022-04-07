from flask import Flask
import utils

app = Flask(__name__)


@app.route('/homepage/')
def home_page():
    data = utils.home_page()
    return data


@app.route('/candidate/<int:x>/')
def candidate_page(x):
    data = utils.candidate_page(x)
    return data


@app.route('/skill/<x>')
def skill_page(x):
    data = utils.skill_page(x)
    return data


app.run(host='127.0.0.2', port=80)




