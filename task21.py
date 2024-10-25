# todo: Задан словарь, его значения необходимо
#  внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam, suscipit lobortis nisl ut aliquip ex ea commodo consequat."}
a = page.values() #возвращает все значения из словаря
lst = list(a)
#print('\n'.join(a))
template = f"""
<!DOCTYPE HTML>
<html>
 <head>
  <title> {lst[0]} </title>
  <meta charset={lst[1]}>
 </head>
 <body onload="alert({lst[2]})">

  <p>{lst[3]}</p>

 </body>
</html>
"""
print(template)

f = open("index.html", 'w+t')
f.write(template)
# f.seek(0)
# f.read()
print(__file__)
f.close()