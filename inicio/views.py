from django.shortcuts import render


# Create your views here.
def inicio(request):
	template = "inicio/inicio.html"
	return render(request, template)


def empresa(request):
	template = "inicio/empresa.html"
	return render(request, template)


def productos(request):
	template = "inicio/productos.html"
	return render(request, template)


def contacto(request):
	template = "inicio/contacto.html"
	return render(request, template)


def clientes_proyectos(request):
	template = "inicio/clientes_proyectos.html"
	return render(request, template)
