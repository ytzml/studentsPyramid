from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('add_student', 'add_student')
    config.add_route('list_students', 'list_students')
    config.add_route('add_student_template', 'add_student_template')
    config.add_route('student_added', 'student_added')
    config.add_route('students_list_page', 'students_list_page')
    config.scan()
    return config.make_wsgi_app()
