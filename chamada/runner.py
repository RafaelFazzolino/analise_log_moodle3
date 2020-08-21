import time
from getpass import getpass

from chamada.verifier import read_students, print_log_count
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import click
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from chamada.chamada import find_names

delay = 10


@click.command()
@click.option('--disciplina', '-d', type=str, help='URL da disciplina no moodle3.')
@click.option('--num', '-n', type=int, help='Número de páginas de logs que serão analisadas.')
def start(disciplina, num):
    if not disciplina:
        click.echo('Por favor, insira a URL da disciplina como parâmetro ao executar. Execute chamadaunb --help para mais informações.')
        exit()
    click.echo("Chamada Automática FGA!")
    user = input('Professor, digite seu usuário do moodle:')
    password = getpass()

    options = FirefoxOptions()
    options.add_argument("--headless")

    browser = webdriver.Firefox(options=options)
    browser.get(disciplina)

    id = browser.find_element_by_xpath('//*[@id="username"]')
    id.send_keys(user)
    senha = browser.find_element_by_xpath('//*[@id="password"]')
    senha.send_keys(password)
    browser.find_element_by_xpath('//*[@id="loginbtn"]').click()

    # Waiting page loading
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div[2]/aside/div[2]/div[2]/div/ul/li/ul/li[6]/p/span')))
    browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/aside/div[2]/div[2]/div/ul/li/ul/li[6]/p/span').click()
    browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/aside/div[2]/div[2]/div/ul/li/ul/li[6]/ul/li[2]/p/a').click()
    browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/section/div/form[1]/div/input[5]').click()

    click.echo('Lendo estudantes matriculados')
    students = read_students()
    click.echo('Verificando log de acesso')

    click.echo('Realizando contagem de acessos..')
    i = 0
    while True:
        table = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/section/div/div/table')
        students = find_names(table, students)
        i += 1
        if i == num:  # Alcancei o número de páginas desejado
            break
        pages = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/section/div/nav[2]/ul')
        pages = pages.find_elements_by_css_selector('li')
        pages[-1].click()

    click.echo('\n\nContagem final:')
    print_log_count(students)
