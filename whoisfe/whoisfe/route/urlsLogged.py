from django.urls import path
from app import viewsCreateCV, viewsDashboard, viewsMyNC, viewsGuide, viewsProfile, viewsMain
urlpatterns = [
    #path("createNC/", viewsCreateNC.createNCViews, name="createNCViews"),
    path("createCV/", viewsCreateCV.createCVViews, name="createCVViews"),
    path("dashboard/", viewsDashboard.dashboardViews, name="dashboardViews"),
    path("myNC/", viewsMyNC.myNCViews, name="myNCViews"),
    path("guide/", viewsGuide.guideViews, name="guideViews"),
    path("profile/", viewsProfile.profileViews, name="profileViews"),
    path("home/", viewsMain.homeLogoutView, name="homeLogoutView"),
    ]   
