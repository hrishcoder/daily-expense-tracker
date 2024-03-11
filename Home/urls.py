from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("",views.index,name='home'),#url for index page
    path("Daily report form",views.daily_report_form,name='daily_report_form'),#url for about page
    path("Daily Report results",views.daily_report_result,name='daily_report_result'),#url for contact page
    # path("Weekly report form",views.weekly_report_form,name='weekly_report_form'),
    # path("Weekly report results",views.weekly_report_result,name='weekly_report_result')
]