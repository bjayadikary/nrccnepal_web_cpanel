from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .models import HomeFeaturedImage, CountsSection, CoreTeam, UpcomingPrograms
from .models import Contact, Programs, TestProgram, TestProgramTopic
from .models import ResearchTrainingTrainers2023, ResearchTrainingMentors2023, ResearchTrainingOrganizers2023, ResearchTrainingTestimonials2023
from .models import ResearchTrainingTrainers2024, ResearchTrainingMentors2024, ResearchTrainingOrganizers2024, ResearchTrainingTestimonials2024
from .models import NewsletterSubscription
from .forms import ContactForm, NewsletterSubscriptionForm #, NewsletterMailMessageForm
# from datetime import datetime
from django.utils import timezone
# Create your views here.

def home(request):
    # Retrieving the major programs, ordered by priority_in_major_programs_list in descending order
    # major_programs = TestProgram.objects.all().order_by('-priority_in_major_programs_list')[:3]
    home_featured_images = HomeFeaturedImage.objects.all().order_by('-updated_datetime').first() # descending order, only top one

    # Retrieve Counts for counts section, in descending order like 3 is shown first, then 2, then 1
    counts_section = CountsSection.objects.all().order_by('-priority')

    now = timezone.now() # datetime.today(), datetime.now() same, but not timezone aware
    # Retrieving upcoming programs (those that have not started yet), ordered by commence_date in ascending order, for example 2024-01-03, 2024-02-15
    upcoming_programs = UpcomingPrograms.objects.filter(commence_date__gte=now).order_by('commence_date', 'published_date')

    # Retrieve ongoing programs (those that have started but not yet ended)
    ongoing_programs = UpcomingPrograms.objects.filter(commence_date__lte=now, end_date__gte=now).order_by('commence_date', 'published_date')

    # Combine both querysets
    ongoing_and_upcoming_programs = (ongoing_programs|upcoming_programs).order_by('commence_date', 'published_date')[:4] # Get only top 4
    
    # Retreiving core team members
    core_team_members = CoreTeam.objects.all().order_by('-priority') # ordered by priority in ascending 
    
    # For newsletter subscription
    subscriber_form = NewsletterSubscriptionForm()
    form_type = None # To track which form was submitted

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'newsletter_form':
            subscriber_form = NewsletterSubscriptionForm(request.POST)
            if subscriber_form.is_valid():
                # Check if the email already exists in db
                email = subscriber_form.cleaned_data.get('email')
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.info(request, "You're already subscribed.")
                else:
                    subscriber_form.save()
                    messages.success(request, 'Thank you for Subscribing!')
                    subscriber_form = NewsletterSubscriptionForm()  # Reset form
            elif not subscriber_form.is_valid():
                if 'email' in subscriber_form.errors and 'already exists' in str(subscriber_form.errors['email']):
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(request, 'Error with your subscription. Please try again with correct details!')


    return render(request, 'core/index.html',{
        # "major_programs": major_programs, # it is not used in homepage currently
        "home_featured_images": home_featured_images,
        "ongoing_and_upcoming_programs": ongoing_and_upcoming_programs,
        "core_team_members": core_team_members,
        "counts_section": counts_section,
        "show_footer": True,
        "now": now,
        "subscriber_form": subscriber_form,
        "form_type": form_type,

    })


def about(request):
    return render(request, 'core/about.html', {
        "show_footer": True,
    })


def research24(request):
    # Initialize the NewsletterSubscriptionForm
    subscriber_form = NewsletterSubscriptionForm()
    form_type = None # To track which form was submitted

    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == 'newsletter_form':
            subscriber_form = NewsletterSubscriptionForm(request.POST)
            if subscriber_form.is_valid():
                # Check if the email already exists in db
                email = subscriber_form.cleaned_data.get('email')
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.info(request, "You're already subscribed.")
                else:
                    subscriber_form.save()
                    messages.success(request, 'Thank you for Subscribing!')
                    subscriber_form = NewsletterSubscriptionForm()  # Reset form

            elif not subscriber_form.is_valid():
                if 'email' in subscriber_form.errors and 'already exists' in str(subscriber_form.errors['email']):
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(request, 'Error with your subscription. Please try again with correct details!')

    # Retrieving trainers, mentors, and organizers list
    trainers_list = ResearchTrainingTrainers2024.objects.all().order_by('priority') # ordered by priority in ascending order
    mentors_list = ResearchTrainingMentors2024.objects.all().order_by('priority')
    organizers_list = ResearchTrainingOrganizers2024.objects.all().order_by('priority')
    
    # Retrieving testimonials from RT2023 
    testimonials_list = ResearchTrainingTestimonials2024.objects.all().order_by('priority')
    return render(request, 'core/research24.html', {
        'trainers': trainers_list,
        'mentors': mentors_list,
        'organizers': organizers_list,
        'testimonials': testimonials_list,
        "show_footer": False,
        "subscriber_form": subscriber_form,
        "form_type": form_type,
    })


def research23(request):
    # Initialize the NewsletterSubscriptionForm
    subscriber_form = NewsletterSubscriptionForm()
    form_type = None # To track which form was submitted

    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == 'newsletter_form':
            subscriber_form = NewsletterSubscriptionForm(request.POST)
            if subscriber_form.is_valid():
                # Check if the email already exists in db
                email = subscriber_form.cleaned_data.get('email')
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.info(request, "You're already subscribed.")
                else:
                    subscriber_form.save()
                    messages.success(request, 'Thank you for Subscribing!')
                    subscriber_form = NewsletterSubscriptionForm()  # Reset form

            elif not subscriber_form.is_valid():
                if 'email' in subscriber_form.errors and 'already exists' in str(subscriber_form.errors['email']):
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(request, 'Error with your subscription. Please try again with correct details!')

    # Retrieving trainers, mentors, and organizers list
    trainers_list = ResearchTrainingTrainers2023.objects.all().order_by('priority') # ordered by priority in ascending order
    mentors_list = ResearchTrainingMentors2023.objects.all().order_by('priority')
    organizers_list = ResearchTrainingOrganizers2023.objects.all().order_by('priority')
    
    # Retrieving testimonials from RT2023 
    testimonials_list = ResearchTrainingTestimonials2023.objects.all().order_by('priority')
    return render(request, 'core/research23.html', {
        'trainers': trainers_list,
        'mentors': mentors_list,
        'organizers': organizers_list,
        'testimonials': testimonials_list,
        "show_footer": False,
        "subscriber_form": subscriber_form,
        "form_type": form_type,
    })

def programs(request):
    # Retrieving all the programsm, ordered by priority_in_programs_list in descending order, if conflict occurs, then order by datetime
    all_programs = TestProgram.objects.all().order_by('-priority_in_programs_list', '-updated_datetime', '-published_date')
    paginator = Paginator(all_programs, 6) # number of objects to display per page
    current_page = request.GET.get('page') # retrieves current page number
    
    try:
        paginator_objects = paginator.page(current_page)
    except PageNotAnInteger:
        paginator_objects = paginator.page(1)

    # For newsletter subscription
    subscriber_form = NewsletterSubscriptionForm()
    form_type = None # To track which form was submitted

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'newsletter_form':
            subscriber_form = NewsletterSubscriptionForm(request.POST)
            if subscriber_form.is_valid():
                # Check if the email already exists in db
                email = subscriber_form.cleaned_data.get('email')
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.info(request, "You're already subscribed.")
                else:
                    subscriber_form.save()
                    messages.success(request, 'Thank you for Subscribing!')
                    subscriber_form = NewsletterSubscriptionForm()  # Reset form

            elif not subscriber_form.is_valid():
                if 'email' in subscriber_form.errors and 'already exists' in str(subscriber_form.errors['email']):
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(request, 'Error with your subscription. Please try again with correct details!')


    return render(request, 'core/programs.html', {
        "all_programs": paginator_objects,
        "show_footer": True,
        "subscriber_form": subscriber_form,
        "form_type": form_type,

    })

def program_details(request, slug):
    # recent_programs = Programs.objects.all().order_by('-priority_in_programs')
    now = timezone.now()
    
    # Retrieve (ongoing programs) programs that have started but not yet ended (Happening Now!)
    ongoing_programs = UpcomingPrograms.objects.filter(commence_date__lte=now, end_date__gte=now).order_by('-commence_date')

    # Retreive (past programs) programs that ended before today, sorted by commence_date in descending order
    past_programs = UpcomingPrograms.objects.filter(end_date__lt=now).order_by('-commence_date')

    # Combine both querysets, with ongoing programs first
    recent_programs = (ongoing_programs | past_programs)[:4]  # top 4 recent programs

    program = TestProgram.objects.filter(slug=slug).first()
    
    if program:
        program_topics = TestProgramTopic.objects.filter(program_title=program.id).order_by('topic_order') # or, program_title__title=program_title

    else:
        # Handle the case where the program is not found
        program_topics = None

    # For newsletter subscription
    subscriber_form = NewsletterSubscriptionForm()
    form_type = None # To track which form was submitted

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'newsletter_form':
            subscriber_form = NewsletterSubscriptionForm(request.POST)
            if subscriber_form.is_valid():
                # Check if the email already exists in db
                email = subscriber_form.cleaned_data.get('email')
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.info(request, "You're already subscribed.")
                else:
                    subscriber_form.save()
                    messages.success(request, 'Thank you for Subscribing!')
                    subscriber_form = NewsletterSubscriptionForm()  # Reset form

            elif not subscriber_form.is_valid():
                if 'email' in subscriber_form.errors and 'already exists' in str(subscriber_form.errors['email']):
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(request, 'Error with your subscription. Please try again with correct details!')


    return render(request, 'core/program-details.html',{
        "program": program,
        "program_topics": program_topics,
        "recent_programs": recent_programs,
        "show_footer": True,
        "now": now,
        "subscriber_form": subscriber_form,
        "form_type": form_type,

    })

# Just for testing 
def program_details_rt(request):
    # For newsletter subscription
    subscriber_form = NewsletterSubscriptionForm()
    form_type = None # To track which form was submitted

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'newsletter_form':
            subscriber_form = NewsletterSubscriptionForm(request.POST)
            if subscriber_form.is_valid():
                # Check if the email already exists in db
                email = subscriber_form.cleaned_data.get('email')
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.info(request, "You're already subscribed.")
                else:
                    subscriber_form.save()
                    messages.success(request, 'Thank you for Subscribing!')
                    subscriber_form = NewsletterSubscriptionForm()  # Reset form

            elif not subscriber_form.is_valid():
                if 'email' in subscriber_form.errors and 'already exists' in str(subscriber_form.errors['email']):
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(request, 'Error with your subscription. Please try again with correct details!')

    return render(request, 'core/program-details-research-training.html',{
        "show_footer": True,
        "subscriber_form": subscriber_form,
        "form_type": form_type,
    })

def spaceapps(request):
    # For newsletter subscription
    subscriber_form = NewsletterSubscriptionForm()
    form_type = None # To track which form was submitted

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'newsletter_form':
            subscriber_form = NewsletterSubscriptionForm(request.POST)
            if subscriber_form.is_valid():
                # Check if the email already exists in db
                email = subscriber_form.cleaned_data.get('email')
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.info(request, "You're already subscribed.")
                else:
                    subscriber_form.save()
                    messages.success(request, 'Thank you for Subscribing!')
                    subscriber_form = NewsletterSubscriptionForm()  # Reset form

            elif not subscriber_form.is_valid():
                if 'email' in subscriber_form.errors and 'already exists' in str(subscriber_form.errors['email']):
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(request, 'Error with your subscription. Please try again with correct details!')

    return render(request, 'core/spaceapps.html', {
        "show_footer": True,
        "subscriber_form": subscriber_form,
        "form_type": form_type,
    })


# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('fullname')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         content = request.POST.get('desc')

#         if name != "" and email != "" and phone != "" and content != "":
#             mycontact = Contact(name=name, email=email, phone=phone,
#                                 address=address, content=content)
#             mycontact.save()
#             # messages.success(request, 'Thank You For submitting form. We will reach you ASAP!!')

#         # else:
#             # messages.error(request, 'Please Fill Up the Form Correctly!!')

#     return render(request, 'core/contact.html')

def contact(request):
    # Initialize the forms
    contact_form = ContactForm()
    subscriber_form = NewsletterSubscriptionForm()
    form_type = None # To track which form was submitted

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'newsletter_form':
            subscriber_form = NewsletterSubscriptionForm(request.POST)
            if subscriber_form.is_valid():
                # Check if the email already exists in db
                email = subscriber_form.cleaned_data.get('email')
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.info(request, "You're already subscribed.")
                else:
                    subscriber_form.save()
                    messages.success(request, 'Thank you for Subscribing!')
                    subscriber_form = NewsletterSubscriptionForm()  # Reset form

            elif not subscriber_form.is_valid():
                if 'email' in subscriber_form.errors and 'already exists' in str(subscriber_form.errors['email']):
                    messages.info(request, "You're already subscribed.")
                else:
                    messages.error(request, 'Error with your subscription. Please try again with correct details!')

        elif form_type == 'contact_form':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Thank you for submitting the form. We will reach out to you soon!')
                contact_form = ContactForm()  # Reset form
            else:
                messages.error(request, 'Error sending your message. Please try again with correct details!')


    context = {
        'contact_form': contact_form, 
        'subscriber_form': subscriber_form, 
        'form_type': form_type,
        "show_footer": True}
    
    return render(request, 'core/contact.html', context)


# def subscribe_newsletter(request): # Can't do like this, pass form via all other views, not directly to base.html
#     if request.method == 'POST':
#         subscriber_form = NewsletterSubscriptionForm(request.POST)
#         if subscriber_form.is_valid():
#             subscriber_form.save()
#             messages.success(request, 'Thank you for Subscribing!')
#     else:
#         subscriber_form = NewsletterSubscriptionForm()

#     return render(request, 'core/base.html', {'subscriber_form': subscriber_form})