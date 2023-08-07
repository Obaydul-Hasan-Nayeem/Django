from django import template
from django.template.loader import get_template

register = template.Library() # template gulo load korte help korbe

def my_template(value, arg):
    if arg == 'change':
        value = 'Rahim'
        return value
    
    if arg == 'title':
        return value.title() # title nam e built in akta case ache. jar karone shob word gulor first letter capital hoye jay.
   
def show_courses():
    courses = [
            {
                "id": 1,
                "course": "A",
                "teacher": "Tanvir"
            },
            {
                "id": 2,
                "course": "B",
                "teacher": "Anis"
            },
            {
                "id": 3,
                "course": "C",
                "teacher": "Shuvo"
            },
        ]
    return {'courses': courses}

courses_template = get_template('first_app/courses.html')
register.filter('change_name', my_template)
register.inclusion_tag(courses_template)(show_courses) # template k render korte & data gulo k organized way te show korte help kore