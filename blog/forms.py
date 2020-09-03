from blog.models import Post
from django import forms


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["user", "title", "slug", "image"]
        exclude = ["height_field", "width_field"]

        labels = {
            "title": "Title",
            "slug": "This is slug"
        }
        help_text = {
            "title": "This is title help text",
            "slug": "This is slug"
        }
        error_messages = {
            "title": {
                "max_length": "This title is too long",
                "required": "Must enter title field"
            }
        }

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].error_messages = {
            "max_length": "This title is too long",
            "required": "Must enter title field"
        }

        for field in self.fields.values():
            print(field.label)
            field.error_messages = {
                "required": "You know, {fieldname} is required".format(fieldname=field.label)
            }

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     print(title)
    #     return title
    #
    # def save(self, commit=True, *args, **kwargs):
    #     obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
    #     obj.publish = "2016-10-01"
    #     obj.content = "Comming soon"
    #     if commit:
    #         obj.save()
    #     return obj


SOME_CHOICES = [
    ('db-value', 'Display Value'),
    ('db-value1', 'Display Value1'),
    ('db-value2', 'Display Value2'),
]

INTS_CHOICES = [tuple([x, x]) for x in range(0, 100)]

YEARS = [x for x in range(1980, 2031)]


class TestForm(forms.Form):
    date_field = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label='Text', widget=forms.Textarea(attrs={"rows": 4, "cols": 10}))
    select = forms.CharField(label='Text', widget=forms.Select(choices=SOME_CHOICES))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10, widget=forms.Select(choices=INTS_CHOICES))
    email = forms.EmailField()

    def __init__(self, user=None, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['some_text'].initial = user

    def clean_integer(self):
        integer = self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer
