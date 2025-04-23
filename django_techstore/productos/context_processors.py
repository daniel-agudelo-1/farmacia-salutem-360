from .models import Categoria

# productos/context_processors.py

def carrito_context(request):
    return {'carrito': request.session.get('carrito', {})}


def categorias_disponibles(request):
    return {
        'categorias': Categoria.objects.all()
    }


# def categorias_context(request):
#     categorias = Categoria.objects.all()
#     return {'categorias': categorias} 