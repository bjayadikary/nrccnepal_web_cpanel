from django.contrib import admin
from .models import Contact, Programs, TestProgram, TestProgramTopic, NewsletterSubscription #, NewsletterMailMessage
from .models import HomeFeaturedImage, CountsSection, CoreTeam, UpcomingPrograms
from .models import ResearchTrainingTrainers2023, ResearchTrainingMentors2023, ResearchTrainingOrganizers2023, ResearchTrainingTestimonials2023
from .models import ResearchTrainingTrainers2024, ResearchTrainingMentors2024, ResearchTrainingOrganizers2024, ResearchTrainingTestimonials2024


# Testprograms is used currently so no need of this
# class ProgramsAdmin(admin.ModelAdmin):
# 	list_filter = ('title', 'priority_in_programs', 'priority_in_home')
# 	list_display = ('title', 'priority_in_programs', 'priority_in_home')
# 	exclude = ['slug']

################
## HomePage
################
class HomeFeaturedImageAdmin(admin.ModelAdmin):
	fields = ('landing_cover_pic', 'intro_side_pic')
	list_display = ('updated_datetime', 'landing_cover_pic', 'intro_side_pic')
	list_display_links = ('updated_datetime', )
	list_editable = ('landing_cover_pic', 'intro_side_pic') # can't edit item if used to display link

class CountsSectionAdmin(admin.ModelAdmin):
	fields = ('descriptive_text', 'counts', 'priority')
	list_display = ('descriptive_text', 'counts', 'priority')
	list_editable = ('priority', )

class CoreTeamAdmin(admin.ModelAdmin):
	fields = ('name', 'position', 'social_medium_1', 'social_medium_1_link', 'social_medium_2', 'social_medium_2_link', 'priority', 'image') # Fields that is display in superadmin when trying to populate the database
	list_display = ('name', 'position', 'priority') # Display name, position, and priority queries 
	list_editable = ('priority', ) # Makes priority editable in the displayed list

class UpcomingProgramsAdmin(admin.ModelAdmin):
	fields = ('name', 'commence_date', 'end_date', 'learn_more_link', 'featured_image')
	list_display = ('name', 'commence_date', 'end_date', 'learn_more_link')

################
### RT2023
################
class ResearchTrainingTrainers2023Admin(admin.ModelAdmin):
	fields = ('name', 'affiliation', 'social', 'social_link', 'priority', 'image')
	list_display = ('name', 'social', 'priority', 'image')
	list_editable = ('priority', ) 

class ResearchTrainingMentors2023Admin(admin.ModelAdmin):
	fields = ('name', 'affiliation', 'social', 'social_link', 'priority', 'image')
	list_display = ('name', 'social', 'priority', 'image')
	list_editable = ('priority', ) 

class ResearchTrainingOrganizers2023Admin(admin.ModelAdmin):
	fields = ('name', 'image', 'priority')
	list_display = ('name', 'image', 'priority')
	list_editable = ('priority', )

class ResearchTrainingTestimonials2023Admin(admin.ModelAdmin):
	fields = ('name', 'image', 'priority', 'content')
	list_display = ('name', 'image', 'priority')
	list_editable = ('priority', )


################
### RT2024
################
class ResearchTrainingTrainers2024Admin(admin.ModelAdmin):
	fields = ('name', 'affiliation', 'social', 'social_link', 'priority', 'image')
	list_editable = ('priority', ) 
	list_display = ('name', 'social', 'priority', 'image')

class ResearchTrainingMentors2024Admin(admin.ModelAdmin):
	fields = ('name', 'affiliation', 'social_link', 'social', 'priority', 'image')
	list_editable = ('priority',)
	list_display = ('name', 'social', 'priority', 'image')

class ResearchTrainingOrganizers2024Admin(admin.ModelAdmin):
	fields = ('name', 'image', 'priority')
	list_display = ('name', 'image', 'priority')
	list_editable = ('priority', )

class ResearchTrainingTestimonials2024Admin(admin.ModelAdmin):
	fields = ('name', 'image', 'priority', 'content')
	list_display = ('name', 'image', 'priority')
	list_editable = ('priority', )



####################
## Our Programs
####################
# Test
class TestProgramAdmin(admin.ModelAdmin):
	list_display = ('title', 'updated_datetime', 'priority_in_major_programs_list', 'priority_in_programs_list')
	list_filter = ('program_tags', 'published_date')
	exclude = ['slug']
	
class TestProgramTopicAdmin(admin.ModelAdmin):
	list_display = ('topic', 'program_title', 'topic_order')
	list_filter = ('program_title', 'topic_order')


#########################
#### Footer and Contact
########################

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
	list_display = ('email', 'created_at')

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'content', 'created_at','query_solved')
	list_editable = ('query_solved', )


# Register your models here.
# Homepage
admin.site.register(HomeFeaturedImage, HomeFeaturedImageAdmin)
admin.site.register(CountsSection, CountsSectionAdmin)
admin.site.register(UpcomingPrograms, UpcomingProgramsAdmin)
admin.site.register(CoreTeam, CoreTeamAdmin)

# Our Programs
# admin.site.register(Programs, ProgramsAdmin) # Since TestPrograms and TestProgramTopics are used currentl
admin.site.register(TestProgram, TestProgramAdmin)
admin.site.register(TestProgramTopic, TestProgramTopicAdmin)

# RT2023
admin.site.register(ResearchTrainingTrainers2023, ResearchTrainingTrainers2023Admin)
admin.site.register(ResearchTrainingMentors2023, ResearchTrainingMentors2023Admin)
admin.site.register(ResearchTrainingOrganizers2023, ResearchTrainingOrganizers2023Admin)
admin.site.register(ResearchTrainingTestimonials2023, ResearchTrainingTestimonials2023Admin)

# RT2024
admin.site.register(ResearchTrainingTrainers2024, ResearchTrainingTrainers2024Admin)
admin.site.register(ResearchTrainingMentors2024, ResearchTrainingMentors2024Admin)
admin.site.register(ResearchTrainingOrganizers2024, ResearchTrainingOrganizers2024Admin)
admin.site.register(ResearchTrainingTestimonials2024, ResearchTrainingTestimonials2024Admin)

# Contact and Footer
admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
# admin.site.register(NewsletterMailMessage)



# admin.site.unregister(HomeFeaturedImage)
# admin.site.unregister(CountsSection)
# admin.site.unregister(UpcomingPrograms)
# admin.site.unregister(CoreTeam)
# admin.site.unregister(TestProgram)
# admin.site.unregister(TestProgramTopic)
# admin.site.unregister(ResearchTrainingTrainers2023)
# admin.site.unregister(ResearchTrainingMentors2023)
# admin.site.unregister(ResearchTrainingOrganizers2023)
# admin.site.unregister(ResearchTrainingTestimonials2023)
# admin.site.unregister(Contact)
# admin.site.unregister(NewsletterSubscription)
