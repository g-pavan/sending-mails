# email_templates/email_templates.py
from jinja2 import Template

class EmailTemplates:
    @staticmethod
    def subject_template(name):
        return f"Hello {name} from Python!"

    @staticmethod
    def message_template(name, employee_id):
        # Load HTML template from file
        with open('email_templates/email_template.html', 'r') as file:
            template_str = file.read()

        # Render the template using Jinja2
        template = Template(template_str)
        return template.render(name=name, employee_id=employee_id)
