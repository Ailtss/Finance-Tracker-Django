from django import forms
from tracker.models import Transaction, Category

class TransactionForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.RadioSelect(),
        label="Categoria"
    )

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError("Valor precisa ser um valor positivo")
        return amount
    
    class Meta:
        model = Transaction
        fields = (
            'type',
            'amount',
            'date',
            'category'
        )
        labels = {
            'type': 'Tipo',
            'amount': 'Valor',
            'date': 'Data',
            'category': 'Categoria',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nome da Categoria',
        }