from pyramid.view import view_config
from .Student import StudentDAO
import json

@view_config(route_name='add_student', renderer='string', request_method='POST')
def add_student(request):
    s_dict = json.loads(request.body.decode('utf-8'))
    sdao = StudentDAO()
    name = s_dict ['name']
    secondname = s_dict['secondname']
    city = s_dict['city']
    id = s_dict['id']
    age = int(s_dict['age'])
    sdao.add_student(name = name, secondname=secondname, age=age, city=city, id=id)
    return {'info': 'student added'}

@view_config(route_name='list_students', renderer='string', request_method='GET')
def list_students(request):
    sdao = StudentDAO()
    response_list = sdao.get_students()
    return_list = []
    for s in response_list:
        s_dict = dict()
        s_dict["name"] = s.name
        s_dict["secondname"] = s.secondname
        s_dict["city"] = s.city
        s_dict["age"] = s.age
        s_dict["id"] = s.id
        return_list.append(s_dict)
    return json.dumps(return_list)

@view_config(route_name='add_student_template', renderer='templates/add_student_template.pt')
def add_student(request):
    return {}

@view_config(route_name='student_added', renderer='templates/student_added.pt', request_method="POST")
def student_added(request):
    name = request.POST['name']
    secondname = request.POST['secondname']
    city = request.POST['city']
    age  = request.POST['age']
    id= request.POST['id']
    sdao = StudentDAO()
    sdao.add_student(id, name, secondname,city,age)
    return {}

@view_config(route_name='students_list_page', renderer='templates/students_list_page.pt')
def students_list_page(request):
    #wczytujemy z sdao, robimy odpowiednia strukture i zwracamy. przetwarzamy w  template
    sdao = StudentDAO()
    response_list = sdao.get_students()
    return_list = []
    for s in response_list:
        s_dict = dict()
        s_dict["name"] = s.name
        s_dict["secondname"] = s.secondname
        s_dict["city"] = s.city
        s_dict["age"] = s.age
        s_dict["id"] = s.id
        return_list.append(s_dict)
    to_return_dict = dict()
    to_return_dict['students'] = return_list
    return to_return_dict


