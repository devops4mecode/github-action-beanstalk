from django.http import HttpResponse

def home(request):
   text = """<h1>This is sample page for AWS Beanstalk written in Python for GitHub Action CI/CD</h1>"""
   return HttpResponse(text)