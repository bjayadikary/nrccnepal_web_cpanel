from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
def validate_if_between_1_3(value):
    if value <= 3 and value >=1:
        return value
    else:
        raise ValidationError("Values should be 1, 2, or 3 representing corresponding column in NRCC's program in home page, else specify 0 for default")

########################
### Models for HomePage
########################
class HomeFeaturedImage(models.Model):
    landing_cover_pic = models.ImageField(upload_to="images/landing_page_images", blank=False, null=False)
    intro_side_pic = models.ImageField(upload_to="images/landing_page_images", blank=False, null=False)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True) # auto_now_add (set once at object creation), auto_now (updates everytime the object is saved)
    
class CoreTeam(models.Model):
    SOCIAL_CHOICES = [
        ('LI', 'LinkedIn'),
        ('FB', 'Facebook'),
        ('EM', 'Email'),
    ]
    name = models.CharField("Name", max_length=50, null=False)
    position = models.CharField("Position", max_length=100, blank=False)
    social_medium_1 = models.CharField(max_length=2, choices=SOCIAL_CHOICES, blank=False)
    social_medium_1_link = models.CharField(max_length=200, blank=False)
    social_medium_2 = models.CharField(max_length=2, choices=SOCIAL_CHOICES, blank=False)
    social_medium_2_link = models.CharField(max_length=200, blank=False)
    priority = models.PositiveIntegerField("Order in Core Team List", default=0)
    image = models.ImageField(upload_to="images/coreteam", blank=False, null=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta: # Django will order the results by 'priority' field first and then by the 'name' field if there are ties in 'priority' in the queryset involving that model
        ordering = ['priority', 'name']

class UpcomingPrograms(models.Model):
    name = models.CharField("Program Name", max_length=100, null=False, blank=False)
    published_date = models.DateField(auto_now_add=True, blank=True)
    commence_date = models.DateTimeField('Program Commence DateTime', null=False, blank=False)
    end_date = models.DateTimeField("Program End DateTime", null=False, blank=False)
    learn_more_link = models.URLField("Link to Learn More", max_length=200, null=True, blank=True) # can be optional, since we might not have detailed information of the program updated in the website
    featured_image = models.ImageField(upload_to="images/upcoming_programs", blank=False, null=False, default='default/upcoming_program_image.jpg')

    # def save(self, *args, **kwargs):
    #     if not self.end_date:
    #         self.end_date = self.commence_date
    #     super(UpcomingPrograms, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['commence_date', 'published_date']


class CountsSection(models.Model):
    descriptive_text = models.CharField("Descriptive text", max_length=200, null=False, blank=False)
    counts = models.PositiveIntegerField("Total Counts", blank=False, null=False)
    priority = models.PositiveIntegerField("Order in Counts Section", default=0)
    
    def __str__(self) -> str:
        return self.descriptive_text
    
    class Meta:
        ordering = ['priority']


######################
#### Models for RT2023
######################
class ResearchTrainingTrainers2023(models.Model):
    SOCIAL_CHOICES = [
        ('LI', 'LinkedIn'),
        ('FB', 'Facebook'),
        ('EM', 'Email'),
    ]
    name = models.CharField("Trainer Name, along with academic qualification", max_length=50, null=False)
    affiliation = models.CharField("Affiliation", max_length=100, blank=False)
    social_link = models.CharField(max_length=200, blank=False)
    social = models.CharField(max_length=2, choices=SOCIAL_CHOICES, blank=False)
    priority = models.PositiveIntegerField("Order in Trainers List", default=0)
    image = models.ImageField(upload_to="images/rt_2023/rt_trainers_2023", blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['priority', 'name']


class ResearchTrainingMentors2023(models.Model):
    SOCIAL_CHOICES = [
        ('LI', 'LinkedIn'),
        ('FB', 'Facebook'),
        ('EM', 'Email'),
    ]
    name = models.CharField("Mentors Name, along with academic qualification", max_length=50, null=False)
    affiliation = models.CharField("Affiliation", max_length=100, blank=False)
    social_link = models.CharField(max_length=200, blank=False)
    social = models.CharField(max_length=2, choices=SOCIAL_CHOICES, blank=False)
    priority = models.PositiveIntegerField("Order in Mentors List", default=0)
    image = models.ImageField(upload_to="images/rt_2023/rt_mentors__2023", blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['priority', 'name']


class ResearchTrainingOrganizers2023(models.Model):
    name = models.CharField("Organizer Name", max_length=50, null=False)
    priority = models.PositiveIntegerField("Order in Organizers List", default=0)
    image = models.ImageField(upload_to="images/rt_2023/rt_organizers__2023", blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['priority', 'name']


class ResearchTrainingTestimonials2023(models.Model):
    name = models.CharField("Name", max_length=50, null=False)
    priority = models.PositiveIntegerField("Order in Testimonials List", default=0)
    image = models.ImageField(upload_to="images/rt_2023/rt_testimonials_2023", blank=False, null=False)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['priority', 'name']


######################
#### Models for RT2024
######################
class ResearchTrainingTrainers2024(models.Model):
    SOCIAL_CHOICES = [
        ('LI', 'LinkedIn'),
        ('FB', 'Facebook'),
        ('EM', 'Email'),
    ]
    name = models.CharField("Trainer Name, along with academic qualification", max_length=50, null=False)
    affiliation = models.CharField("Affiliation", max_length=100, blank=False)
    social = models.CharField(max_length=2, choices=SOCIAL_CHOICES, blank=False)
    social_link = models.CharField(max_length=200, blank=False)
    priority = models.PositiveIntegerField("Order in Trainers List", default=0)
    image = models.ImageField(upload_to="images/rt_2024/rt_trainers_2024", blank=True, null=True) # Allowing Null values temporarily so that I can apply the migration without providing a default value. After the migration, we can manually update the records in our database and then later make the field non-nullable ( blank=False, null=False) again. 
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['priority', 'name']
       
class ResearchTrainingMentors2024(models.Model):
    SOCIAL_CHOICES = [
        ('LI', 'LinkedIn'),
        ('FB', 'Facebook'),
        ('EM', 'Email'),
    ]
    name = models.CharField("Mentors Name, along with academic qualification", max_length=50, null=False)
    affiliation = models.CharField("Affiliation", max_length=100, blank=False)
    social_link = models.CharField(max_length=200, blank=False)
    social = models.CharField(max_length=2, choices=SOCIAL_CHOICES, blank=False)
    priority = models.PositiveIntegerField("Order in Mentors List", default=0)
    image = models.ImageField(upload_to="images/rt_2024/rt_mentors__2024", blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['priority', 'name']


class ResearchTrainingOrganizers2024(models.Model):
    name = models.CharField("Organizer Name", max_length=50, null=False)
    priority = models.PositiveIntegerField("Order in Organizers List", default=0)
    image = models.ImageField(upload_to="images/rt_2024/rt_organizers__2024", blank=False, null=False)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['priority', 'name']


class ResearchTrainingTestimonials2024(models.Model):
    name = models.CharField("Name", max_length=50, null=False)
    priority = models.PositiveIntegerField("Order in Testimonials List", default=0)
    image = models.ImageField(upload_to="images/rt_2024/rt_testimonials_2024", blank=False, null=False)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['priority', 'name']


################################
### Models for Our Programs Page 
################################
class Programs(models.Model):
    title = models.CharField("Program Title", max_length=500)
    body_intro = models.TextField(default="Type here...") # should change to introduction that describes the event in may be less than 50 words and that comes just below the featured_image.  
    published_date = models.DateField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)
    # program_in_home_flag = models.BooleanField(default=False)
    priority_in_home = models.IntegerField(default=0, blank=True, validators=[validate_if_between_1_3]) # validation should be between 0 and 4, 0 for default case with which the particular blog won't be displayed in the home page
    priority_in_programs = models.IntegerField(default=0) # rename to priority_in_programs_list
    featured_image = models.ImageField(upload_to="images/our_programs/featured_images", blank=True, null=True, default='default/no_image.jpg')
    slug = models.SlugField(unique=True, max_length=600)

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f"{self.title}"


# was created for testing propose, and is used currently in the programs view
class TestProgram(models.Model):
    title = models.CharField(help_text="Program Title in less than 500 characters", max_length=500)
    time_duration = models.CharField(help_text="Program Duration, For instance, 'Every Saturday, 1 hour, ...", max_length=100)
    readtime = models.CharField(help_text="Expected Read Time of this Blog, like '5 mins'", max_length=50)
    short_description = models.CharField(help_text="Short Description in about one or two line", max_length=1000)
    program_featured_img = models.ImageField(upload_to="images/our_programs/featured_images", blank=True, null=True)
    # program_featured_img_caption = models.CharField("Write caption for the image in less than 500 characters", max_length=500)
    program_tags = models.CharField(help_text="Mention some tags separated by comma (,)", max_length=500)

    slug = models.SlugField(unique=True, max_length=600)
    published_date = models.DateField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)
    PRIORITY_CHOICES = [
        (0, 'Do not display on homepage'),
        (1, 'Display in third column'),
        (2, 'Display in second column'),
        (3, 'Display in first column')
    ]
    priority_in_major_programs_list = models.IntegerField(help_text="Choose 0 if you don't want this program to display in homepage, else choose 1, 2, or 3 priority", choices=PRIORITY_CHOICES, default=0)
    priority_in_programs_list = models.IntegerField(help_text='0 means lowest priority', default=0)
    google_form_link = models.URLField(help_text="Google Form Link if somebody wants to be a part of this program", blank=True, null=True)
    
    class Meta:
        verbose_name = "Our Program"
        verbose_name_plural = "Our Programs"

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f"{self.title}"
    

class TestProgramTopic(models.Model):
    program_title = models.ForeignKey(TestProgram, on_delete=models.CASCADE)
    
    topic = models.CharField(help_text="Write a topic", max_length=500) # change it to topic name
    topic_order = models.IntegerField(help_text="1 to display this topic content on the first place, and similarly, 2 for second, 3 for third, and soon.", default=0, blank=True)
    
    topic_detail_first_paragraph = models.TextField(help_text="First paragraph", null=True, blank=True)
    topic_detail_first_bullet_points = models.TextField(help_text="Write bullet points in a single line separated by # ", null=True, blank=True)
    topic_detail_first_highlighting_text = models.TextField(null=True, blank=True)
    topic_detail_first_img = models.ImageField(upload_to=f"images/test_uploads/", blank=True, null=True)
    topic_detail_first_img_caption = models.CharField(help_text="Write caption for the image in less than 500 characters", max_length=500, blank=True, null=True)
    topic_detail_first_video_embed_source = models.CharField(help_text="Write the source of the video you want to embed. See the 'src' under iframe tag. Looks like: https://www.youtube.com/embed/sl18__huoXI?si=k0ZoEVYVihc-E9Pn ", max_length=200, blank=True, null=True)

    topic_detail_second_paragraph = models.TextField(help_text="Second Paragraph if exists", null=True, blank=True)
    topic_detail_second_bullet_points = models.TextField(help_text="Write bullet points in a single line separated by # ", null=True, blank=True)
    topic_detail_second_highlighting_text = models.TextField(null=True, blank=True)
    topic_detail_second_img = models.ImageField(upload_to=f"images/test_uploads", null=True, blank=True)
    topic_detail_second_img_caption = models.CharField(help_text="Write caption for the image in less than 500 characters", max_length=500, blank=True, null=True)
    topic_detail_second_video_embed_source = models.CharField(help_text="Write the source of the video you want to embed. See the 'src' under iframe tag. Looks like: https://www.youtube.com/embed/sl18__huoXI?si=k0ZoEVYVihc-E9Pn ", max_length=200, blank=True, null=True)

    topic_detail_third_paragraph = models.TextField(help_text="Third paragraph if exists", null=True, blank=True)
    topic_detail_third_bullet_points = models.TextField(help_text="Write bullet points in a single line separated by # ", null=True, blank=True)
    topic_detail_third_highlighting_text = models.TextField(null=True, blank=True)
    topic_detail_third_img = models.ImageField(upload_to=f"images/test_uploads", null=True, blank=True)
    topic_detail_third_img_caption = models.CharField(help_text="Write caption for the image in less than 500 characters", max_length=500, blank=True, null=True)
    topic_detail_third_video_embed_source = models.CharField(help_text="Write the source of the video you want to embed. See the 'src' under iframe tag. Looks like: https://www.youtube.com/embed/sl18__huoXI?si=k0ZoEVYVihc-E9Pn ", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "ProgramTopic"
        verbose_name_plural = "ProgramTopics"

    def __str__(self):
        return f"{self.topic}"
    

####################################################
## Models for footer, Newsletter, and Contact page
####################################################

class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=250, blank=False)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, default="")
    content = models.TextField()
    query_solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now) # allows to edit the created_at, although it is not what i wanted

    def __str__(self) -> str:
        return self.name
    
class NewsletterSubscription(models.Model):
    email = models.EmailField(max_length=250, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.email
    
class NewsletterMailMessage(models.Model): # Although table migrated, but not used currenntly
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title

# class NrccbasicInfo(models.Model):
#     address = models.CharField(max_length=100, blank=False, null=False, default="House No.164, Bhakti Thapa Sadak, New Baneshwor, KTM ")
#     phone = models.CharField(max_length=20, blank=False, null=False, default="+977 - 9802348778")
#     email = models.EmailField(max_length=100, blank=False, null=False, default="info@nrccnepal.org")

#     def __str__(self) -> str:
#         return f"{self.address} - {self.phone} - {self.email}"