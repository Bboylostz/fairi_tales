from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Autor, Genre, Story

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')


from django.shortcuts import render
from .models import Story

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def story_list(request):
    stories = Story.objects.all()
    paginator = Paginator(stories, 2)  # Показываем по 2 сказки на странице

    page = request.GET.get('page', 1)

    try:
        paginated_stories = paginator.page(page)
    except PageNotAnInteger:
        paginated_stories = paginator.page(1)
    except EmptyPage:
        paginated_stories = paginator.page(paginator.num_pages)

    return render(request, 'story_list.html', {'stories': paginated_stories})


def search_stories(request):
    query = request.GET.get('query', '')
    stories = Story.objects.filter(
        Q(title__icontains=query) |
        Q(author__name__icontains=query) |
        Q(genre__name__icontains=query)
    )
    return render(request, 'story_search.html', {'stories': stories})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'story_detail.html', {'story': story})