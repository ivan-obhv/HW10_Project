import json


def load_candidates():
    with open('candidates.json', encoding='utf8') as fp:
        data = json.load(fp)

        return data


def load_candidates_from_json():
    """Возвращает всех кандидатов из json """
    with open('candidates.json', encoding='utf8') as fp:
        data = json.load(fp)

    return data


def get_candidate(candidate_id):
    """Возвращает кандидата по его 'id' """
    data = load_candidates()
    data_for_candidate = data[candidate_id - 1]

    return data_for_candidate


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов с навыками 'skill_name' """
    data = load_candidates()
    data_for_skill = []
    for i in data:
        if skill_name.lower() in i['skills'].lower():
            data_for_skill.append(i)

    return data_for_skill


def get_candidates_by_name(candidate_name):
    """Возвращает кандидата по имени """
    data = load_candidates()
    data_for_candidate_name = []
    for i in data:
        if candidate_name.lower() in i['name'].lower():
            data_for_candidate_name.append(i)

    return data_for_candidate_name
