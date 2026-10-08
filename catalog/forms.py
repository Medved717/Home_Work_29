from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product, Category

BAN_WORDS = ['казино', 'криптовалюта', 'крипта',
             'биржа', 'дешево', 'бесплатно', 'обман',
             'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'buying_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }
        )

        self.fields['category'].widget.attrs.update(
            {
                'class': 'form-control'
            }
        )

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control'
            }
        )

        self.fields['buying_price'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите сумму'
            }
        )

    def clean_name(self):
        name = self.cleaned_data.get('name', None)
        if name is not None:
            name_lower = name.lower()
            for ban_name in BAN_WORDS:
                if ban_name.lower() in name_lower:
                    raise ValidationError(f'Введено недопустимое слово {ban_name}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', None)
        if description is not None:
            description_lower = description.lower()
            for ban_name in BAN_WORDS:
                if ban_name.lower() in description_lower:
                    raise ValidationError(f'Введено недопустимое слово {ban_name}')
        return description

    def clean_buying_price(self):
        buying_price = self.cleaned_data.get('buying_price', None)
        if buying_price is not None and buying_price < 0:
            raise ValidationError('Цена не может быть отрицательной.')
        return buying_price


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите наименование'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }
        )
