from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField, forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    banned_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар"
    ]

    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at",
        )

    def clean_name(self):
        cleaned_name = self.cleaned_data["name"]
        if cleaned_name.lower() in self.banned_words:
            raise forms.ValidationError("Недопустимое наименование поля")

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data["description"]
        if cleaned_description.lower() in self.banned_words:
            raise forms.ValidationError("Недопустимое описание поля")

        return cleaned_description


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
