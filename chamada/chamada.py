import time


def find_names(table, students):
    for row in table.find_elements_by_css_selector('tr'):
        cells = row.find_elements_by_css_selector('td')
        if len(cells) >= 2:
            name = cells[1].text
            if name in students: # Garantindo que são apenas alunos realmente matriculados
                students[name] += 1
                print('.', end='')

    return students

