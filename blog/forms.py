from blog.models import Comment
from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class CommentForm(forms.ModelForm):
  model=Comment
  fields=["content"]  
  def __init__(self, *args, **kwargs):
    super(CommentForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))
