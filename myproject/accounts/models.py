from django.db import models
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
# username필드의 검증에 username이 이미 사용중인지 여부 검사
def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError('아이디가 이미 사용중입니다')
    return username