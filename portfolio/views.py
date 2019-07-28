from django.shortcuts import render, get_object_or_404
from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-updated_at')
    return render(request, 'portfolio/portfolio.html', {'portfolios':portfolios})

def more(request, portfolio_id):
    portfolio_more = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'portfolio/more.html', {'portfolio': portfolio_more})