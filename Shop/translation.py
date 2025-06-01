from .models import Information
from modeltranslation.translator import TranslationOptions,register

@register(Information)
class InformationTranslationOptions(TranslationOptions):
    fields = ('p_name','city','description')
