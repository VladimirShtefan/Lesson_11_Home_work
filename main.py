from flask import Flask, render_template
from os.path import join, abspath
from utils.classes import Candidate

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
PATH = abspath(join('files', 'candidates.json'))


@app.route('/')
def index():
    return render_template('index.html', candidates=Candidate(PATH).load_candidates_from_json())


@app.route('/candidate/<int:uid>/')
def candidate(uid: int):
    return render_template('single.html', candidate=Candidate(PATH).get_candidate_by_id(uid))


@app.route('/search/<candidate_name>/')
def search(candidate_name: str):
    candidate_list = Candidate(PATH).search_candidates_by_name(candidate_name)
    return render_template('search.html', candidate_list=candidate_list, count=len(candidate_list))


@app.route('/skill/<skill_name>/')
def skill(skill_name: str):
    candidate_list = Candidate(PATH).search_candidates_by_skill(skill_name)
    return render_template('search.html', candidate_list=candidate_list, count=len(candidate_list), skill_name=skill_name)


if __name__ == '__main__':
    app.run()








