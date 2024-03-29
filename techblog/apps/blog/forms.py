from django import forms


class ImportForm(forms.Form):

    blog_slug = forms.CharField(label="Blog slug")
    input_file = forms.FileField()
    include_tags = forms.CharField(label="Included tags", required=False)
    exclude_tags = forms.CharField(label="Excluded tags", required=False)
    format = forms.CharField(label="Import format", widget=forms.HiddenInput, initial="WXR")


class WriterForm(forms.Form):

    title = forms.CharField(label="Post Title", required=True)
    slug = forms.CharField(label="Post Slug", required=True)
    tags = forms.CharField(label="Tags (comma separated)", required=True)
    post = forms.CharField(label="Post Content", required=False)
