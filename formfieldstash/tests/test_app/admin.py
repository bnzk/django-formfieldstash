from django import forms
from django.contrib import admin

from formfieldstash.admin import FormFieldStashMixin
from formfieldstash.helpers import get_advanced_stash_attrs
from .models import TestModelSingle, TestModelAdvanced, TestModelInInlineModel, TestInlineModelSingle, \
    TestInlineModel, TestModelAdvanced2


class TestModelAdmin(FormFieldStashMixin, admin.ModelAdmin):
    single_formfield_stash = ('selection', )


admin.site.register(TestModelSingle, TestModelAdmin)


class TestInlineModelInline(admin.StackedInline):
    model = TestInlineModel


ADVANCED_STASH = {
    'set': {
        'set1': ('set1_1', '#testinlinemodel_set-group', ),
        'set2': ('set2_1', 'set2_2', 'set2_3', ),
        'set3': ('set3_1', 'set2_1', ),
    },
}


class TestModelAdvancedAdmin(FormFieldStashMixin, admin.ModelAdmin):
    inlines = [TestInlineModelInline, ]
    formfield_stash = ADVANCED_STASH


admin.site.register(TestModelAdvanced, TestModelAdvancedAdmin)


SET_CHOICES = (
    ('set1', 'with inline and field',),
    ('set2', 'three fields',),
    ('set3', 'two',),
)


class TestModelAdvanced2AdminForm(forms.ModelForm):
    set = forms.ChoiceField(
        required=False,
        choices=SET_CHOICES,
        widget=forms.Select(
            attrs=get_advanced_stash_attrs('set', ADVANCED_STASH['set'])
        )
    )


class TestModelAdvanced2AdminWithForm(FormFieldStashMixin, admin.ModelAdmin):
    inlines = [TestInlineModelInline, ]
    form = TestModelAdvanced2AdminForm


admin.site.register(TestModelAdvanced2, TestModelAdvanced2AdminWithForm)


class TestInlineModelSingleInline(FormFieldStashMixin, admin.StackedInline):
    model = TestInlineModelSingle
    single_formfield_stash = ('selection', )


class TestModelInInlineModelAdmin(FormFieldStashMixin, admin.ModelAdmin):
    inlines = [TestInlineModelSingleInline, ]


admin.site.register(TestModelInInlineModel, TestModelInInlineModelAdmin)
