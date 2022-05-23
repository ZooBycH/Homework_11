from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route('/')
def page_list():  # вьюшка для отображения всех кандидатов
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:pk>/')
def page_candidate(pk):  # вьюшка для поиска кандидата по id
    candidate = utils.get_candidate_by_id(pk)
    if candidate is None:
        return "Нет такого кандидата"
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def page_search(candidate_name):  # вьюшка для поиска кандидатов по имени
    candidates = utils.get_candidates_by_name(candidate_name)
    numbers_of_candidates = len(candidates)
    return render_template('search.html', candidates=candidates, numbers_of_candidates=numbers_of_candidates)


@app.route('/skill/<skill_name>')
def page_skill(skill_name):  # вьюшка для поиска кандидатов по навыку
    candidates = utils.get_candidates_by_skill(skill_name)
    numbers_of_candidates = len(candidates)
    return render_template('skill.html', candidates=candidates,
                           skill_name=skill_name, numbers_of_candidates=numbers_of_candidates)


if __name__ == '__main__':
    app.run()
