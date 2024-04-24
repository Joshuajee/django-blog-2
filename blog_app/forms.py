from django.forms import Form, CharField, Textarea

class CreatePostForm(Form):
    title = CharField(max_length=150, label="Post Title")
    content = CharField(max_length=10000, label="Post Content", widget=Textarea())
