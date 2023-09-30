# 1 задача
inp = [
   {'city': 'Moscow', 'street': 'Trubnaya street'},
   {'city': 'Barcelona', 'street': 'Paseo de Gracia'},
   {'city': 'Moscow', 'street': 'Lenin Street'}
]
d = {} 
for i in inp:
    city = i['city']
    street = i['street']
    if city in d:
        d[city] += [street] # ковычки для того чтобы значения были списком, без них будет будет через запитую
    else:
        d[city] = [street] # ковычки для того чтобы значения были списком, без них будет будет через запитую
print(d)        
               

#res = {
#    'Moscow': ['Trubnaya street', 'Lenin Street'],
#    'Barcelona': ['Paseo de Gracia']
#}
       
# ------------------------------------------------------------------------------
# 2 задача
# Количество продаж за каждый месяц
# Необходимо подсчитать общее количество продаж за каждый месяц. 
# Для этого напиши пж функцию, которая принимает на вход массив объектов,
#  каждый из которых имеет свойства "month" и "sales", и возвращает массив сумм продаж по месяцам.

const_salesData = [
  { "month": "January", 'sales': 1000 },
  { 'month': "February", 'sales': 2000 },
  { 'month': "March", 'sales': 3000 },
  { 'month': "January", 'sales': 1500 },
  { 'month': "February", 'sales': 2500 },
  { 'month': "March", 'sales': 3500 },
  { 'month': "January", 'sales': 2000 },
  { 'month': "February", 'sales': 3000 },
  { 'month': "March", 'sales': 4000 }, ]

def func(list_dist):
    salesbymonth = {}
    for i in list_dist:
        month = i['month']
        sales = i['sales']
        if month in salesbymonth:
            salesbymonth[month] +=  sales # это для следующих значений 
        else:
            salesbymonth[month] = sales # это для первых значений 
            
    return salesbymonth


result = func(const_salesData)
print(result)
# print(func(const_salesData))


# ======================================================================

# 3 задача

# Возраст больше 18 лет
# Необходимо получить список всех пользователей, у которых возраст больше 18 лет.
# Для этого напиши пж функцию, которая принимает на вход массив объектов, каждый из которых представляет пользователя и имеет свойство "age", и возвращает массив объектов, состоящий только из пользователей, у которых возраст больше 18 лет.

const_users = [
  { "name": "Alice", "age": 22 },
  { "name": "Bob", "age": 17 },
  { "name": "Charlie", "age": 28 },
  { "name": "David", "age": 15 },
  { "name": "Eve", "age": 20 },
]

list_ = []
for i in const_users:
    name = i['name']
    age = i['age']
    if age > 18:
        list_.append(name)
print(list_)        
        


account = {
  "id": 3136,
  "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
  "account_number": "0847799459",
  "iban": "GB90XTND56373623909314",
  "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
  "routing_number": "126602476",
  "swift_bic": "BCYPGB2LHGB"
}
l = []
for key in account.keys():
    l.append(key)
print(l)         





from collections import Counter
a = [{'Петя': 6, 'Вася': 8, 'Дима': 11, 'Юля': 3}, {'Петя': 5, 'Вася': 36, 'Дима': 4, 'Юля': 8}, {'Петя': 54, 'Вася': 21, 'Дима': 22, 'Юля': 39}, {'Петя': 61, 'Вася': 48, 'Дима': 71, 'Юля': 73}]
c = Counter()
for d in a:
    print(d)
    c.update(d)
print(c) 