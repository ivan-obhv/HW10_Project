from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route('/')
def home_page():
    names = utils.load_candidates_from_json()
    return render_template('list.html', names=names)


@app.route('/candidate/<int:x>/')
def candidate_page(x):
    data = utils.get_candidate(x)
    return render_template('single.html', data=data)


@app.route('/skill/<skill_name>')
def skill_page(skill_name):
    data = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', data=data, skill=skill_name)


@app.route('/search/<candidate_name>')
def get_candidates_by_name(candidate_name):
    data = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', data=data)


app.run(host='127.0.0.2', port=80)

