from django.urls import path

from . import views

app_name = "Research_work"

urlpatterns = [
    path("",views.index,name="index_page"),
    path("signup/",views.signup,name="signup_page"),
    path("research-home/",views.research,name="research_home_page"),
    path("publication",views.publication,name="publication_page"),
    path("add_publication",views.add_publication,name="add_publication_page"),
    path("reseach_grant",views.research_grant,name="research_grant_page"),
    path("add_research_grant",views.add_research_grant,name="add_research_grant_page"),
    path("consultancy",views.consultancy,name="consultancy_page"),
    path("add_consultancy",views.add_consultancy,name="add_consultancy_page"),
    path("admin_page",views.admin_page,name="admin_access_page"),
    path("logout/",views.logout_view,name="logout_page")
    
]