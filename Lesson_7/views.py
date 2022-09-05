from datetime import date
from logging import getLogger

from decors import AppRoute, Logger, debug
from framework.template import render
from patterns.creational_patterns import Engine, MapperRegistry
from patterns.cbv import EmailNotifier, SmsNotifier, ListView, CreateView, Serializer
from db.unit_of_work import UnitOfWork

site = Engine()
LOGGER = getLogger('main')
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()
UnitOfWork.new_current()
UnitOfWork.get_current().set_mapper_registry(MapperRegistry)

routes = {}


@AppRoute(routes=routes, url='/')
class Index:
    @debug
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self, request):
        return '200 OK', render('about.html')


@AppRoute(routes=routes, url='/contacts/')
class Contacts:
    def __call__(self, request):
        if request.get('method') == 'POST':
            return '200 OK', render('contacts.html')
        else:
            return '200 OK', render('contacts.html')


@AppRoute(routes=routes, url='/training-programs/')
class TrainingPrograms:
    @debug
    def __call__(self, request):
        return '200 OK', render('training-programs.html', data=date.today())


class NotFound404:
    @debug
    def __call__(self, request):
        LOGGER.error(f'Ошибка 404. Страница не найдена')
        return '404 WHAT', '404 PAGE Not Found'


@AppRoute(routes=routes, url='/courses-list/')
class CoursesList:
    @debug
    def __call__(self, request):

        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            LOGGER.info(f'Добавлена категория {category}')
            return '200 OK', render('course-list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)
        except KeyError:
            LOGGER.info(f'Нет курса для добавления')
            return '200 OK', 'No courses have been added yet'


@AppRoute(routes=routes, url='/create-course/')
class CreateCourse:
    category_id = -1

    @debug
    def __call__(self, request):
        if request['method'] == 'POST':

            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                course.observers.append(email_notifier)
                course.observers.append(sms_notifier)
                site.courses.append(course)

            return '200 OK', render('course-list.html',
                                    objects_list=category.courses,
                                    name=category.name,
                                    id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                # print(f'ахх {request}')
                LOGGER.info(f'Запрос {request}')
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create-course.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                LOGGER.info(f'Нет категории для добавления')
                return '200 OK', 'No categories have been added yet'


@AppRoute(routes=routes, url='/create-category/')
class CreateCategory:
    @debug
    def __call__(self, request):

        if request['method'] == 'POST':

            # print(request)
            LOGGER.info(f'Запрос {request}')
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render('index.html',
                                    objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create-category.html',
                                    categories=categories)


@AppRoute(routes=routes, url='/category-list/')
class CategoryList:
    @debug
    def __call__(self, request):
        LOGGER.info(f'Список категорий')
        return '200 OK', render('category-list.html',
                                objects_list=site.categories)


@AppRoute(routes=routes, url='/student-list/')
class StudentListView(ListView):
    queryset = site.students
    template_name = 'student_list.html'

    def get_queryset(self):
        mapper = MapperRegistry.get_current_mapper('student')
        return mapper.all()


@AppRoute(routes=routes, url='/create-student/')
class StudentCreateView(CreateView):
    template_name = 'create_student.html'

    def create_obj(self, data: dict):
        name = data['name']
        name = site.decode_value(name)
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)
        new_obj.mark_new()
        UnitOfWork.get_current().commit()


@AppRoute(routes=routes, url='/add-student/')
class AddStudentByCourseCreateView(CreateView):
    template_name = 'add_student.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = site.students
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course_name = site.decode_value(course_name)
        course = site.get_course(course_name)
        student_name = data['student_name']
        student_name = site.decode_value(student_name)
        student = site.get_student(student_name)
        course.add_student(student)


@AppRoute(routes=routes, url='/api/')
class CourseApi:
    @debug
    def __call__(self, request):
        return '200 OK', Serializer(site.courses).save()
