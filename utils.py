import json
from pprint import pprint as pp

path = 'candidates.json'


def load_candidates_from_json():
    '''возвращает список всех кандидатов'''
    file = open(path, encoding='utf-8')
    data = json.load(file)
    file.close()
    return data


def get_candidate_by_id(pk):
    '''возвращает одного кандидата по его id'''
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate.get('id') == pk:
            return candidate


def get_candidates_by_name(candidate_name):
    '''возвращает кандидатов по имени'''
    candidates = load_candidates_from_json()
    candidates_list = [candidate for candidate in candidates if candidate_name.lower() in candidate.get('name').lower()]
    return candidates_list


def get_candidates_by_skill(skill_name):
    '''возвращает кандидатов по навыку'''
    skill_name = skill_name.lower()
    candidates = load_candidates_from_json()
    candidates_skill_list = []

    for candidate in candidates:
        skill = candidate.get('skills')
        skill_list = skill.lower().split(", ")
        if skill_name in skill_list:
            candidates_skill_list.append(candidate)
    return candidates_skill_list
