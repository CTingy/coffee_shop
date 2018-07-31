from django import forms
from account.models import User


class UserForm(forms.ModelForm):
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['fullname', 'username', 'password', 'password2', 'email']
        labels = {
            'fullname': '姓名(可不填)',
            'username': '帳號',
            'password': '密碼',
            'email': '電子信箱',
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        '''
        Override the cleaning method for this one individual field.
        '''
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('密碼不相符')
        return password2

    def save(self, commit=True):
        '''
        Override the method of ModelForm, which can save a form instance into database.
        Called by UserForm.save()
        '''
        user = super().save(commit=False)  # 從一個self輸入，回傳一個model instance: self.instance，並在往後使用其save方法
        user.set_password(user.password)  # 加密
        if commit:
            user.save()
        return user
