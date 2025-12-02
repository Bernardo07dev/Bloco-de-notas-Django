from django.shortcuts import render, redirect
from django.shortcuts import redirect
from api.models import Nota
from django.http import HttpResponse

def home_view(request):
    notas = Nota.objects.all()
    return render(request, "home.html", {"notas": notas})

def processar_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        note = request.POST.get("note")

        Nota.objects.create(
            title=title,
            note=note
        )

        return redirect("/")
    return redirect("/")  

def CRUD(request):
    if request.method == "POST":
        acao = request.POST.get("action")
        ident = request.POST.get("nota_id")

        if acao == "apagar":
            Nota.objects.filter(id=ident).delete()
            return redirect("/")
        
        if acao == "editar":
            return redirect(f"/editar/{ident}")

def editar_view(request, id):
    return render(request, "editar.html", {"id": id})

def editar(request):
    if request.method == "POST":
        titulo = request.POST.get("new_titulo")
        novo_valor_nota = request.POST.get("new_nota")
        nota_id = request.POST.get("nota_id")   # <-- pegar id correto

        nota = Nota.objects.get(id=nota_id)     # <-- agora funciona

        nota.title = titulo
        nota.note = novo_valor_nota
        nota.save()
        return redirect("/")
    return redirect("/")