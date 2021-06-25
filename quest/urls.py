from django.urls import path, include, re_path
from quest    import views
from .views import LoginTracciamento


urlpatterns = [
                path('2',views.ProvaView,name ='login_utenti' ),
                path('4/<str:tracciamento>',views.RegistrationView,name ='registrazione_utenti'),
                path('5',views.RegistrationAnagView,name ='registrazioni_anagrafica'),
                path('7',views.RegistrationStudView,name ='registrazioni_studi'),
                path('10',views.RegistrationExpView,name ='registrazioni_esperienze'),
#                path('esperienza/', views.candidato_exp_view, name='esperienza_add'),
#                path('ajax/load-lavori/', views.load_lavori, name='ajax_load_lavori'),
                path('13',views.RegistrationLangView,name ='registrazioni_lingue'),
                path('13/<str:a>',views.RegistrationLangView,name ='registrazioni_lingue'),
                path('15',views.QuestView,name ='registrazioni_questionari'),
                path('17',views.RiassuntoCandidato,name ='pagina_utente'),
                path('18/<str:id>',views.CancellaLingua,name ='cancella_dato'),
                path('19/<str:id>',views.CancellaEsperienza,name ='cancella_dato'),
                path('20/<str:id>',views.CancellaStudio,name ='cancella_dato'),
                path('gestione-inserimento/<str:passo_corrente>/',views.GestioneInserimentoView2,name ='gestione_inserimento'),
                path('gestione-inserimento/<str:passo_corrente>/<str:tracciamento>/',views.GestioneInserimentoView2,name ='gestione_inserimento'),
                path('accounts/',include('django.contrib.auth.urls')),
                path('login/',LoginTracciamento.as_view(),name ='login_tracciamento'),
                path('cruscotto',views.Dashboard, name='cruscotto'),
                path('',views.Homepage),
                path('inter',views.Inter),
                path('utente2', views.Utente2),
                path('proxy', views.Proxy),
                re_path(r'^29/(?P<professione>\w+| )/(?P<lingua>\w+|)$',views.Tabella),
                path('29',views.Tabella),
#                path('30',views.RicercaCandidato),
                path('esperienza/', views.esperienza_create_view, name='esperienza_add'),
                path('ajax/load-professioni/', views.load_professioni, name='ajax_load_professioni'),
                path('residenza/', views.residenza_create_view, name='residenza_add'),
                path('ajax/load-amm2/', views.load_amm2, name='ajax_load_amm2'),
                path('ajax/load-amm3/', views.load_amm3, name='ajax_load_amm3'),
                path('ajax/load-amm4/', views.load_amm4, name='ajax_load_amm4'),
                ]
