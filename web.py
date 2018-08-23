# -*- coding: utf-8 -*-
from flask import Flask
import random

app = Flask(__name__)
@app.route('/main')
def main():
    return '''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="/static/main.css">
            <title>Резюме.</title>
          </head>
          <body>
            <header>
              <div class="container">
                <div id="logo">
                  <h1>My Own Landing Page</h1>
                </div>
                <div class="navigation">
                  <nav>
                    <ul>
                      <li><a href="/main">Главная</a></li>
                      <li><a href="/me">Обо мне</a></li>
                      <li><a href="/weather">Погода</a></li>
                    </ul>
                  </nav>
                </div>
              </div>
            </header>
          </body>
        </html>
    '''

@app.route('/me')
def me():
    return '''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="/static/main.css">
            <title>Резюме.</title>
          </head>
          <body>
            <header>
              <div class="container">
                <div id="logo">
                  <h1>My Own Landing Page</h1>
                </div>
                <div class="navigation">
                  <nav>
                    <ul>
                      <li><a href="/main">Главная</a></li>
                      <li><a href="/me">Обо мне</a></li>
                      <li><a href="/weather">Погода</a></li>
                    </ul>
                  </nav>
                </div>
              </div>
            </header>
            <div class="container" id="all">
              <section>
                <div class="container" id="intro">
                  <h1>Sergey Skripnik</h1>
                  <img src="/static/38626149_190290595024243_271509802180411392_n.jpg" alt="My photo">
                  <p></p>
                </div>
              </section>
              <section>
                <div class="container" id="interests">
                  <h1>Мои интересы</h1>
                  <table border="1">
                    <tr>
                      <th>Мои любимые фильмы.</th>
                      <th>Мои любимые книги.</th>
                      <th>Мои любимые игры.</th>
                      <th>Мои любимые спортивные игры.</th>
                    </tr>
                    <tr>
                      <th>Волк с Уолл Стрит, Дедпул, Бэтмен.</th>
                      <th>Мертвые души, Финансист.</th>
                      <th>Дота 2.</th>
                      <th>Настольный Теннис, Футбол.</th>
                    </tr>
                </table>
                </div>
              </section>
            </div>
          </body>
        </html>
     '''

@app.route('/weather')
def weather():
    rand1 = random.randint(-10, 30)
    rand2 = random.randint(-10, 30)
    rand3 = random.randint(-10, 30)
    rand4 = random.randint(-10, 30)
    rand5 = random.randint(-10, 30)
    rand6 = random.randint(-10, 30)
    rand7 = random.randint(-10, 30)
    return '''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="/static/main.css">
            <title>Резюме.</title>
          </head>
          <body>
            <header>
              <div class="container">
                <div id="logo">
                  <h1>My Own Landing Page</h1>
                </div>
                <div class="navigation">
                  <nav>
                    <ul>
                      <li><a href="/main">Главная</a></li>
                      <li><a href="/me">Обо мне</a></li>
                      <li><a href="/weather">Погода</a></li>
                    </ul>
                  </nav>
                </div>
              </div>
            </header>
            <section>
              <div class="container" id="weather_name">
                <h1>Погода</h1>
              </div>
              <div class="container">
                <table border="1" id="weather">
                  <tr>
                    <th>Понедельник.</th>
                    <th>Вторник.</th>
                    <th>Среда.</th>
                    <th>Четверг.</th>
                    <th>Пятница.</th>
                    <th>Суббота.</th>
                    <th>Воскресенье.</th>
                  </tr>
                  <tr>
                    <th>{}</th>
                    <th>{}</th>
                    <th>{}</th>
                    <th>{}</th>
                    <th>{}</th>
                    <th>{}</th>
                    <th>{}</th>
                  </tr>
              </table>
              </div>
            </section>
          </body>
        </html>
    '''.format(rand1, rand2, rand3, rand4, rand5, rand6, rand7)

app.run(debug=True, port=8080)
