from db import db_session
from models import User, Salary

# Одного пользователя
user = User.query.first()
db_session.delete(user)
db_session.commit()

# Очистить БД Salary
db_session.query(Salary).delete()
db_session.commit()
