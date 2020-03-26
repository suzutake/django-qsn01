from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        # fieldsに追記すると項目として追加される
        fields = ('name','staff_1','price_1','staff_2','price_2','staff_3','price_3','staff_4','price_4','staff_5','price_5','memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'Ví dụ về mục：Nguyen thi Thuy','add_class':'form-control'}),
                    #'price_total': forms.TextInput(attrs={'disabled':'disabled'}), #read-only
                    'staff_1': forms.TextInput(attrs={'placeholder':'Ví dụ về mục：Trang'}),
                    'price_1': forms.TextInput(attrs={'placeholder':'Ví dụ về mục：60'}),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
