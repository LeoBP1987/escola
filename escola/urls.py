from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('estudantes/<int:id>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:id>/matriculas/', ListaMatriculaCurso.as_view()),
]