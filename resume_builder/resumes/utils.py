from django.template.loader import render_to_string
from weasyprint import HTML


def generate_pdf(template, context):
    html_string = render_to_string(template, context)
    return HTML(string=html_string).write_pdf()