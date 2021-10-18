from models import User

print('___ Единичный запрос ___')
user = User.query.first()
print(user)

print()
print('___ Выведи всех ___')

user_all = User.query.all()
print(*user_all, sep='\n')

print('___ Единичный запрос ___')
user = User.query.first()
print(f'''Имя:  {user.name}
Зарплата: {user.salary} 
Email: {user.email}''')
