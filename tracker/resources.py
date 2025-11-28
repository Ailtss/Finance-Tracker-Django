from import_export import resources, fields
from tracker.models import Transaction, Category
from import_export.widgets import ForeignKeyWidget

class TransactionResource(resources.ModelResource):

    Valor = fields.Field(
        column_name='Valor',
        attribute='amount'
    )
    
    Tipo = fields.Field(
        column_name='Tipo', 
        attribute='type'
    )
    
    Data = fields.Field(
        column_name='Data',
        attribute='date'
    )

    category = fields.Field(
        column_name='Categoria',
        attribute='category',
        widget=ForeignKeyWidget(Category, field='name')
    )

    class Meta:
        model = Transaction
        fields = (
            'Valor',
            'Tipo',
            'Data',
            'category',
        )
        export_order = ('Valor', 'Tipo', 'Data', 'Categoria')

