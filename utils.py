import json


def load_candidates():
    with open('candidates.json', encoding='utf8') as fp:
        data = json.load(fp)

        return data


def home_page():
    """Возвращает всех кандидатов"""
    data = load_candidates()
    data_for_home_page = ''
    for i in data:
        data_for_home_page += f'<pre>'\
                              f'Имя кандидата - {i["name"]}\n'\
                              f'Позиция кандидата - {i["position"]}\n'\
                              f'Навыки - {i["skills"]}\n\n'\
                              f'<pre>'

    return data_for_home_page


def candidate_page(x):
    """Возвращает кандидата на позиции 'x' """
    data = load_candidates()
    data_x = data[x]
    data_for_candidate = ''
    data_for_candidate += f'<img src="({data_x["picture"]})">\n\n'\
                          f'<pre>\n'\
                          f'Имя кандидата - {data_x["name"]}\n'\
                          f'Позиция кандидата - {data_x["position"]}\n'\
                          f'Навыки - {data_x["skills"]}\n'\
                          f'<pre>\n'

    return data_for_candidate


def skill_page(x):
    """Возвращает кандидатов с навыками 'x' """
    data = load_candidates()
    data_for_skill = ''
    for i in data:
        if x.lower() in i['skills'].lower():
            data_for_skill += f'<pre>\n'\
                      f'Имя кандидата - {i["name"]}\n'\
                      f'Позиция кандидата - {i["position"]}\n'\
                      f'Навыки - {i["skills"]}\n'\
                      f'<pre>\n'

    return data_for_skill

