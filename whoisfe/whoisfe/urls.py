
from django.urls import path,  include

urlpatterns = [
    ##### undsen huudasnuud ##############################
    path("", include('whoisfe.route.urlsMain')),
    ######################################################

    ##### newtersen hereglegchiin huudasnuud #############
    path("", include('whoisfe.route.urlsLogged')),
    ######################################################

    ##### week1 huudasnuud ###############################
    path("", include('whoisfe.route.urlsWeek1')),
    ######################################################   
]
