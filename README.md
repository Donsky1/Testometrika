# testometrika

<i>Задание 1. Questions and answers</i>
<h2>Website Using Django</h2>
<p><b>Testometrika</b> - сервис проведения тестирования по каким-либо темам. Т.е. есть тесты с вариантами ответов, один или несколько вариантов должны быть правильными. Тесты группируются в наборы тестов, которые затем пользователь может проходить и видеть свой результат</p>
<p>Алгоритм: пользователь заходит на сайт, проходит простую регистрацию, выполняет вход под своим логином, проходит тесты и по итогу получает результ.</p>
<b><i>Используется встроенный способ создания структуры БД (makemigrations, migrate). Встроенный manage.py syncdb или миграции через South (являются устаревшими)</i></b>
<br><br><br>
Обзор:
<ul>
  <li><a href='#main'>Главная страница</a></li>
  <li><a href='#question'>Страница вопроса</a></li>
  <li><a href='#check'>Страница проверки перед тестированием</a></li>
  <li><a href='#result'>Страница результата пройденного теста</a></li>
  <li><a href='#reg'>Регистрация</a></li>
  <li><a href='#log'>Логин</a></li>
</ul>

<h2 id='main'>Главная страница</h2>
При входе на сайт, незарегистрированный пользователь увидет, следующее окно:<br>
<p><img src='https://github.com/Donsky1/Testometrika/blob/master/qa/testometrika/main.png' align="center"></p>
Полсле прохождения простого этапа регистрации (<a href='#reg'>регистрация</a>) и входа под своим <a href='#log'>логином</a> откроется основная станцица с набором тестов.<br>
<br>
<p><img src='https://github.com/Donsky1/Testometrika/blob/master/qa/testometrika/test_page.png' align="center"></p>
<br>

<h2 id='question'>Страница вопроса</h2>
Образец формы на странице вопроса<br>
<br>
<p><img src='https://github.com/Donsky1/Testometrika/blob/master/qa/testometrika/test_page2.png' align="center"></p>
<br>

<h2 id='check'>Страница проверки перед тестированием</h2>
<br>
<p><img src='https://github.com/Donsky1/Testometrika/blob/master/qa/testometrika/test_page_check.png' align="center"></p>
<br>

<h2 id='result'>Страница результата пройденного теста</h2>
Образец страницы с результатом пройденного теста<br>
<br>
<p><img src='https://github.com/Donsky1/Testometrika/blob/master/qa/testometrika/result.png' align="center"></p>
<br>

<h2 id='reg'>Регистрация</h2>
Образец страницы регистрации<br>
<br>
<p><img src='https://github.com/Donsky1/Testometrika/blob/master/qa/testometrika/registration.png' align="center"></p>
<br>

<h2 id='log'>Логин</h2>
Образец страницы входа на сайт<br>
<br>
<p><img src='https://github.com/Donsky1/Testometrika/blob/master/qa/testometrika/login.png' align="center"></p>
<br>
