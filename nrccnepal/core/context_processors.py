from .models import TestProgram

def nav_slugs(request):
    # Retrieve slugs from the database
    programs = TestProgram.objects.all()
    slugs = {program.title:program.slug for program in programs}
    return {'slugs': slugs}