from django import forms
from .models import Task, Tag


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['hints', 'status', ]


# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['name',]


class CreateTaskForm(forms.ModelForm):
    # new_tag = TagForm()
    name = forms.CharField(max_length=255)
    class Meta:
        model = Task
        fields = ['title', 'description', 'date_deadline', 'time_deadline', 'category', 'tags', 'name']

        # fields = ['title', 'description', 'date_deadline', 'time_deadline', 'category', 'user_Constructive', 'user_doing', 'tags', 'name']



    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'title',
    #         'name': 'title',
    #         'placeholder': 'Title...',
    #         'required': '',
    #     })
    #     self.fields['description'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'description',
    #         'name': 'description',
    #         'placeholder': 'Description...',
    #         'required': '',
    #     })
    #
    #     self.fields['date_deadline'].widget = forms.widgets.DateInput(
    #         attrs={
    #             'type': 'date', 'placeholder': 'yyyy-mm-dd',
    #             'class': 'form-control w-50'
    #         }
    #     )
    #     self.fields['date_deadline'].widget = forms.widgets.TimeInput(
    #         attrs={
    #             'type': 'time',
    #             'class': 'form-control w-50'
    #         }
    #     )
    #     self.fields['category'].widget.attrs.update({
    #         'class': 'd-block me-auto'
    #     })
    #     self.fields['tags'].widget.attrs.update({
    #         'class': 'd-block me-auto'
    #     })
    #     self.fields['name'].widget.attrs.update({
    #         'class': 'd-block me-auto'
    #     })



    # def save(self, commit=True):
    #     task_obj = super().save(commit=False)
    #     name = self.cleaned_data['name']
    #
    #     if commit:
    #         # instance = Setupuser.objects.create(organization=org)
    #         task_obj.save()
    #         task_obj.tags.set(name)
    #         # task_obj.tags
    #         #  Tag.objects.create(
    #         #     name=name
    #         # )
    #         print('=' * 50)
    #     # return task_obj
