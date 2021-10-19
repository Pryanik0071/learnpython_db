from models import Salary


def get_top_salary(num_rows):
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)
    for salary in top_salary:
        print(f'З/п {salary.salary}')


def salary_by_city(city_name):
    top_salary = Salary.query.filter(Salary.city == city_name)\
        .order_by(Salary.salary.desc())
    print(city_name)
    for salary in top_salary:
        print(f'З/п {salary.salary}')


def top_salary_by_email_domain(domain_name, num_rows):
    top_salary = Salary.query.filter(Salary.email.like(f"%{domain_name}"))\
        .order_by(Salary.salary.desc()).limit(num_rows)
    print(domain_name)
    for salary in top_salary:
        print(f'З/п {salary.salary}')


if __name__ == '__main__':
    get_top_salary(5)
    salary_by_city('Адыгейск')
    top_salary_by_email_domain('@gmail.com', 5)