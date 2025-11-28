from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.conf import settings
from tracker.charting import plot_income_expenses_bar_chart, plot_category_pie_chart
from tracker.models import Transaction, Category
from tracker.filters import TransactionFilter
from tracker.forms import TransactionForm, CategoryForm
from django_htmx.http import retarget
from tracker.resources import TransactionResource
from django.http import HttpResponse




# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')

@login_required
def transactions_list(request):
    #Precisa ser transações apenas do usuário logado
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
    ) 

    paginator = Paginator(transaction_filter.qs, settings.PAGE_SIZE)
    transaction_page = paginator.page(1) # default to 1 when this view is triggered


    total_income = transaction_filter.qs.get_total_income()
    total_expenses = transaction_filter.qs.get_total_expenses()

    context = {
                'transactions': transaction_page,
                'filter': transaction_filter,
                'total_income': total_income,
                'total_expenses': total_expenses,
                'net_income': total_income - total_expenses
               }
    if request.htmx:
        return render(request, 'tracker/partials/transactions-container.html', context)
       
    return render(request, 'tracker/transactions-list.html', context)

@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save() 
            context = {'message': "Lançamento foi adicionado com sucesso!"}
            return render(request, 'tracker/partials/transaction-success.html', context)
        else:
            context = {'form': form}
            response = render(request, 'tracker/partials/create-transaction.html', context)
            return retarget(response, '#transaction-block')
        
    context = {'form': TransactionForm()}
    return render(request, 'tracker/partials/create-transaction.html', context)


@login_required
def update_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save()

            context = {'message': "Lançamento foi alterado com sucesso!"}
            return render(request, 'tracker/partials/transaction-success.html', context)
    
        else:
            context = {
            'form': form,
            'transaction': transaction,
            }
            response = render(request, 'tracker/partials/update-transaction.html', context)
            return retarget(response, '#transaction-block')
        
    context = {
        'form': TransactionForm(instance=transaction),
        'transaction': transaction,
    }
    return render(request, 'tracker/partials/update-transaction.html', context)


# @login_required
# def create_category (request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             context = {'message': "Categoria foi criada com sucesso!"}
#             return render(request, 'tracker/partials/transaction-success.html', context)
#     context = {'form': CategoryForm()}
#     return render(request, 'tracker/partials/category-form.html', context)


@login_required
def categories_list(request):
    # Pega TODAS as categorias
    categories = Category.objects.all()
    
    context = {
        'categories': categories
    }
    
    # Se for requisição HTMX, retorna apenas o container
    if request.htmx:
        return render(request, 'tracker/partials/categories-container.html', context)
    
    # Se for requisição normal, retorna a página completa
    return render(request, 'tracker/categories-list.html', context)

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Retorna a lista atualizada de categorias
            categories = Category.objects.all()
            
            if request.htmx:
                return render(request, 'tracker/partials/categories-container.html', {
                    'categories': categories,
                    'message': 'Categoria criada com sucesso!'
                })
            
            # Se não for HTMX, redireciona para a lista de categorias
            return redirect('categories-list')
        else:
            # Se o formulário for inválido, retorna o formulário com erros
            if request.htmx:
                return render(request, 'tracker/partials/category-form.html', {'form': form})
    
    # GET request - mostrar o formulário vazio
    context = {'form': CategoryForm()}
    
    if request.htmx:
        return render(request, 'tracker/partials/category-form.html', context)
    
    return render(request, 'tracker/partials/category-form.html', context)

@login_required
@require_http_methods(["DELETE"])
def delete_category(request, pk):
    # Remove a verificação de usuário, pois categorias são globais
    category = get_object_or_404(Category, pk=pk)
    category_name = category.name
    category.delete()

    # Retornar a lista atualizada de categorias
    categories = Category.objects.all()
    
    if request.htmx:
        return render(request, "tracker/partials/categories-container.html", {
            "categories": categories,
            "message": f"Categoria '{category_name}' deletada com sucesso!"
        })
    
    return render(request, "tracker/categories-list.html", {
        "categories": categories,
        "message": f"Categoria '{category_name}' deletada com sucesso!"
    })


@login_required
@require_http_methods(["DELETE"])
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    transaction.delete()
    context = {
        'message': f"Lançamento de {transaction.amount} na data {transaction.date} foi deletado com sucesso!"
    }
    return render(request, 'tracker/partials/transaction-success.html', context)


@login_required
def get_transactions(request):
    page = request.GET.get('page', 1)
    import time
    time.sleep(0.8)
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
    ) 

    paginator = Paginator(transaction_filter.qs, settings.PAGE_SIZE)
    context = {
        'transactions': paginator.page(page)
    }

    return render(request,
                  'tracker/partials/transactions-container.html#transaction_list',
                  context
                  )

@login_required
def transaction_charts(request):
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
    )

    income_expense_bar = plot_income_expenses_bar_chart(transaction_filter.qs)
    category_income_pie = plot_category_pie_chart(transaction_filter.qs.filter(type='receita'), 'Receitas por Categoria')
    category_expense_pie = plot_category_pie_chart(transaction_filter.qs.filter(type='despesa'), 'Despesas por Categoria')
    context = {
        'filter': transaction_filter,
        'income_expense_barchart': income_expense_bar.to_html(),
        'category_income_pie': category_income_pie.to_html(),
        'category_expense_pie': category_expense_pie.to_html(),

        }
    
    if request.htmx:
        return render(request, 'tracker/partials/charts-container.html', context)

    return render(request, 'tracker/charts.html', context)


@login_required
def export(request):

    if request.htmx:
        return HttpResponse(headers={'HX-Redirect': request.get_full_path()})
    transaction_filter = TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user).select_related('category')
    )

    data = TransactionResource().export(transaction_filter.qs)
    response = HttpResponse(data.csv)
    response['Content-Disposition'] = 'attachment; filename="lancamentos.csv"'
    return response

