from modeltranslation.translator import translator, TranslationOptions
from .models import project_list, project_page, project_images

class ProjectPageTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title', 'projects', 'another_projects', 'name', 'text', 'last_projects')

class ProjectListTranslationOptions(TranslationOptions):
    fields = ('is_active', 'name',)

class ProjectImagesTranslationOptions(TranslationOptions):
    fields = ()


translator.register(project_page, ProjectPageTranslationOptions)
translator.register(project_list, ProjectListTranslationOptions)
translator.register(project_images, ProjectImagesTranslationOptions)