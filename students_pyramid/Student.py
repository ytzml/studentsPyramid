from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func



Base = declarative_base()

class Student(Base):
    """
    Obiekt ten odpowada tabeli students w bazie danych
    Poszczególne pola odpowiadają kolumnom z tej tabeli
    """
    __tablename__ = 'students'

    id = Column(String, primary_key=True)
    name = Column(String)
    secondname = Column(String)
    city = Column(String)
    age = Column(Integer)

    def __str__(self):
        """
        Wywoływana w celu tworzenia tekstowej reprezentacji instancji klasy
        :return:
        """
        return "<User(name='%s', secondname='%s', city='%s', id = '%s', age = '%s')>" % (self.name, self.secondname, self.city, self.id, self.age)


class StudentDAO:
    """
    Tą klasę wykorzystujemy do zadawania zapytań (nazwa DAO pochodzi od Data Access Object)
    Przechowuje ona odpowiednie obiekty SALAlchemy oraz funkcje wywołujące określone operacje na baze.
    """
    def __init__(self):
        #działamy z bazą sqlite
        engine = create_engine('sqlite:///students_pyramid.sqlite')
        #najważniejszym obiektem poniżej jest session - będziemy na nim wywoływać operacje mające już bezpośredni skutek
        #np zapisanie danych w bazie czy pobranie danych z bazy
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        self.engine = engine
        self.session = session

    def add_student(self, id, name, secondname, city, age):
        """
        Dodaj studenta o określonych atrybutach
        :param id: identyfikator (np. numer indeksu)
        :param name: imię
        :param secondname: nazwisko
        :param city: miasto pochodzenia
        :param age: wiek
        :return: None
        """
        #tworzymy instancję klasy Student (zdefiniowanej powyżej w tym pliku)
        s = Student(id = id, name = name, secondname = secondname, city = city, age = age)
        #wywołujemy operację zapisującą do bazy dane odpowiadające obiektowi
        self.session.add(s)
        #commim musi być wywołane, aby dane faktycznie ostatecznie znalazły się w bazie
        self.session.commit()

    def get_student_by_id(self, id):
        """
        Pobiera z bazy wiersz studenta o danym ID
        :param id:
        :return:
        """
        return self.session.query(Student).filter_by(id = id).first()

    def get_students(self):
        """
        Pobiera z bazy wszystkie rekordy w klasie students
        :return:
        """
        return self.session.query(Student)

    def get_average_age(self):
        """
        Zwraca średni wiek studentów w bazie
        :return:
        """
        return self.session.query(func.avg(Student.age)).scalar()


    def get_average_age_for_city(self, city):
        """
        Zwraca średni wiek mieszkańców zadanego miasta
        :param city:
        :return:
        """
        return self.session.query(func.avg(Student.age)).filter_by(city=city).scalar()
