import plotly.express as px
from django.db.models import Sum

from tracker.models import Category


def plot_income_expenses_bar_chart(qs):
    x_vals = ['Receita', 'Despesa']

    # somar os totais
    total_income = qs.filter(type='receita').aggregate(
        total=Sum('amount')
    )['total']

    # somar os totais
    total_expense = qs.filter(type='despesa').aggregate(
        total=Sum('amount')
    )['total']


    fig = px.bar(x=x_vals, y=[total_income, total_expense])

    fig.update_layout(title='Gráfico de Barras')

    return fig


# def plot_category_pie_chart(qs):
#     count_per_category = (
#         qs.order_by('category').values('category')
#         .annotate(total=Sum('amount'))
#     )

#     category_pks = count_per_category.values_list('category', flat=True).order_by('category')
#     categories = Category.objects.filter(pk__in=category_pks).order_by('pk').values_list('name', flat=True)

#     total_amount = count_per_category.values_list('amount', flat=True)

#     fig = px.pie(values=total_amount, names=categories)
#     fig.update_layout(title_text='Total de valor por Categoria')
#     return fig


def plot_category_pie_chart(qs, title="Gráficos por Categoria"):
    # Consulta corrigida - pegar categoria e valor na mesma consulta
    category_data = (
        qs.values('category__name')  # Pegar o nome da categoria diretamente
        .annotate(total=Sum('amount'))
        .filter(total__isnull=False)  # Filtrar valores nulos
        .order_by('-total')
    )
    
    # Extrair nomes e valores da mesma consulta
    categories = [item['category__name'] for item in category_data]
    total_amount = [float(item['total']) for item in category_data]  # Converter para float
    
    # Verificar se temos dados
    if not categories or not total_amount:
        # Retornar um gráfico vazio se não houver dados
        fig = px.pie(values=[1], names=['Sem dados'])
        fig.update_layout(title_text='Nenhum dado disponível')
        return fig
    
    fig = px.pie(values=total_amount, names=categories)


    
    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            xanchor='center',
            font=dict(size=16)
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,  # Aumente este valor para dar mais espaço
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=20, r=20, t=40, b=150),  # Aumente a margem inferior
        height=500  # Defina uma altura fixa maior
    )


    return fig
