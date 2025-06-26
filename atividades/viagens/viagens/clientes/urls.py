from django.urls import path
# from .views import cadastrar_aluno, cadastrar_curso, excluir_aluno, alunos_inativos, ativar_aluno, ordenar_alunos, ordenar_alunos_inativos, index
from .views import index, cadastrar_cliente, listar_clientes

urlpatterns = [
    path('', index, name='index'),
    # path('alunos/', alunos, name='alunos'),
    # path('alunos/inativos/', alunos_inativos, name='alunos_inativos'),
    # path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    # path('editar_aluno/<int:id>/', editar_aluno, name='editar_aluno'),
    # path('excluir_aluno/<int:id>/', excluir_aluno, name='excluir_aluno'),
    # path('alunos/ativar/<int:id>/', ativar_aluno, name='ativar_aluno'),
    # path('alunos/ordenar/<parametro>/', ordenar_alunos, name='ordenar_alunos'),
    # path('alunos/ordenar/inativos/<parametro>/',
    #      ordenar_alunos_inativos, name='ordenar_alunos_inativos'),

    path('clientes/', listar_clientes, name='listar_clientes'),
    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    # path('editar_cliente/<int:id>/', editar_cliente, name='editar_cliente'),
    # path('excluir_cliente/<int:id>/', excluir_cliente, name='excluir_cliente'),
]
