from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import transaction
from .models import Producto, Factura, DetalleFactura

from django.contrib.humanize.templatetags.humanize import intcomma

from .models import Producto, Categoria



def index(request):
    categorias = Categoria.objects.all()
    productos_oferta = Producto.objects.filter(en_oferta=True)
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {
        'categorias': categorias,
        'productos_oferta': productos_oferta,
        'productos': productos,
    })

# detallesd el producto
def detalle_producto(request, id_producto):
    try:
        producto = Producto.objects.get(id=id_producto)
    except Producto.DoesNotExist:
        # Si no se encuentra el producto, renderiza una página de error
        return render(request, 'productos/error.html', {'message': 'Producto no encontrado'})
    
    return render(request, 'productos/detalle.html', {'producto': producto})


 #Funcion para buscar productos 
def buscar_productos(request):
    query = request.GET.get('search-input', '')
    
    if not query:
        # Si no hay query, muestra un mensaje o una lista vacía
        return render(request, 'productos/buscar.html', {'productos': [], 'query': query, 'mensaje': 'Por favor, ingresa un término de búsqueda'})
    
    productos = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'productos/buscar.html', {'productos': productos, 'query': query})

#  registrar usuario 
def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login si todo es válido
        else:
            return render(request, 'productos/registro.html', {'form': form, 'error': 'Formulario no válido. Por favor, revisa los campos.'})
    else:
        form = UserCreationForm()
    return render(request, 'productos/registro.html', {'form': form})


#carrito de compras 
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
    else:
        carrito[str(producto_id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1,
            'imagen': producto.imagen.url,
        }

    request.session['carrito'] = carrito
    request.session.modified = True
    return redirect('ver_carrito')

#vista del carrito de compras 
@login_required
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = 0

    for item in carrito.values():
        subtotal = float(item['precio']) * item['cantidad']
        item['subtotal'] = subtotal
        total += subtotal

    return render(request, 'productos/carrito.html', {
        'carrito': carrito,
        'total': total,
    })


#eliminar producto del carrito
def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito

    return redirect('ver_carrito')


#vaciar carrito
def vaciar_carrito(request):
    request.session['carrito'] = {}
    return redirect('ver_carrito')


#vista para ver los productos por categoria
def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    
    return render(request, 'productos/productos_por_categoria.html', {
        'categoria': categoria,
        'productos': productos
    })
    
    
@login_required
def finalizar_compra(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('ver_carrito')

    try:
        with transaction.atomic():
            factura = Factura.objects.create(usuario=request.user, total=0)
            total = 0

            for pid_str, item in carrito.items():
                producto = get_object_or_404(Producto, pk=pid_str)
                cantidad = int(item['cantidad'])
                subtotal = producto.precio * cantidad
                total += subtotal

                DetalleFactura.objects.create(
                    factura=factura,
                    producto=producto,
                    cantidad=cantidad,
                    subtotal=subtotal
                )

            factura.total = total
            factura.save()

            # Vaciar carrito
            request.session['carrito'] = {}
            request.session.modified = True

            messages.success(request, f"Compra completada. Factura #{factura.numero}")
            return redirect('ver_factura', factura_id=factura.numero)

    except Exception as e:
        messages.error(request, f"Error al finalizar la compra: {e}")
        return redirect('ver_carrito')


@login_required
def ver_factura(request, factura_id):
    factura = get_object_or_404(Factura, numero=factura_id)
    detalles = factura.detalles.select_related('producto')
    return render(request, 'productos/factura_detalle.html', {
        'factura': factura,
        'detalles': detalles
    })
    
    

