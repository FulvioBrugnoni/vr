from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import *
from quest.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import login_active_required, login_recruiter_required
from django.core.mail import send_mail
from .utils import Step
import logging
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .ricerca import RicercaCandidato

logger = logging.getLogger('www-logger')

def TestoCandidato(candidato, slide):
            azienda = AziendaLingua.objects.filter(candidatoparametro__candidato = candidato).first().id
            lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
            testo = Testo.objects.filter(lingua = lingua, slide =slide)
            return testo


@login_required
def Dashboard(request):
    current_step = Step.get_instance(request.user.stato)
    return redirect(reverse(current_step.get_redirect_url()))

@login_recruiter_required
def Utente2(request):
        return render(request,'quest/utente2.html')

def Proxy(request):
        if  request.user.ruolo == 1:
            step = '30'
        elif request.user.candidatoazienda_set.exists():
            step = '17'
        elif request.user.risposta_set.exists():
            step = '15'
        elif request.user.anagrafica_set.exists():
            step = '15'
        else:
            step = '5'
        return HttpResponsePermanentRedirect(step)

def Homepage(request):
        logger.debug('Errore!!!!')
        return render(request,'quest/home.html')

def Inter(request):
        return render(request,'quest/inter.html')


def GestioneInserimentoView(request, passo_corrente,tracciamento= None):
        gestione_ins = GestioneInserimento.objects.get(passo_corrente =passo_corrente)
#        slide = gestione_ins.slide
#        azienda = AziendaLingua.objects.filter(candidatoparametro__parametro__azienda = tracciamento).first().id
#        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
#        testo = Testo.objects.filter(lingua = lingua, slide = slide)
        testo = 'testo'
        passo_destra = gestione_ins.passo_destra
        if tracciamento:
            passo_destra+= f"/{tracciamento}"
        tab = {'tab': testo, 'passo_destra':passo_destra, 'passo_sinistra':gestione_ins.passo_sinistra,}
        return render(request,'quest/richiesta_inserimento.html',tab)

def GestioneInserimentoView2(request, passo_corrente,tracciamento= None):
        gestione_ins = GestioneInserimento.objects.get(passo_corrente =passo_corrente)
        passo_destra = gestione_ins.passo_destra
        testo = 'testo'
        if tracciamento:
            passo_destra+= f"/{tracciamento}"
            azienda = AziendaLingua.objects.filter(azienda = tracciamento).first().id
            lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
            slide = GestioneInserimento.objects.get(passo_corrente =passo_corrente).slide
            testo = Testo.objects.filter(lingua = lingua, slide =slide)
        else:
            candidato = request.user
            azienda = AziendaLingua.objects.filter(candidatoparametro__candidato = candidato).first().id
            lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
            slide = GestioneInserimento.objects.get(passo_corrente =passo_corrente).slide
            testo = Testo.objects.filter(lingua = lingua, slide =slide)
        tab = {'tab': testo, 'passo_destra':passo_destra, 'passo_sinistra':gestione_ins.passo_sinistra,}
        return render(request,'quest/richiesta_inserimento.html',tab)


#---------------------------------------------------------------------------------------------------------


def RegistrationView(request,tracciamento):
        azienda = AziendaLingua.objects.filter(azienda = tracciamento).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        testo = Testo.objects.filter(lingua = lingua, slide =5)
        print(len(testo))
        if request.method == "POST":
                form = CandidatoForm(request.POST)
                if form.is_valid():
                    user = form.save()
#                    send_mail('oggetto','body','fulvio.brugnoni1984@gmail.com',['fulvio.brugnoni1984@gmail.com'],fail_silently = False)
                    return HttpResponseRedirect(reverse('registrazioni_anagrafica'))
        else:
            form = CandidatoForm(initial={'tracciamento': tracciamento})

        return render(request,'quest/registrazione_utente_.html', {'form': form, 'title':'registrazione utente' })

@login_required
def RegistrationAnagView(request):
        candidato = request.user
        testo = TestoCandidato(candidato, 5)
        if request.method == "POST":
                form = AnagraficaForm(request.POST)
                if form.is_valid():
                    nome = form.cleaned_data["nome"]
                    cognome = form.cleaned_data["cognome"]
                    codicefiscale = form.cleaned_data["codicefiscale"]
                    eta = form.cleaned_data["eta"]
                    gender = form.cleaned_data["gender"]
                    u = Anagrafica(candidato =candidato, nome=nome, cognome=cognome, codicefiscale=codicefiscale,
                                eta =eta, gender=gender)
                    u.save()
                    candidato.stato = MyUser.STATO_REGSTUDI
                    candidato.save()
#                    return HttpResponseRedirect('gestione-inserimento/2')
                    return redirect(reverse('cruscotto'))
        else:
            form = AnagraficaForm()

        return render(request,'quest/registrazione_utente_anagrafica.html', {'form': form, 'tab':testo})


def RegistrationStudView(request):
        candidato = request.user
        if request.method == "POST":
                form = StudioCreationForm(request.user,request.POST)
                if form.is_valid():
                    materia = form.cleaned_data["materia"]
                    titolo = form.cleaned_data["titolo"]
                    u = Studio(candidato =candidato, materia=materia, titolo=titolo)
                    u.save()
                    return HttpResponseRedirect('gestione-inserimento/3')
        else:
            form = StudioCreationForm(request.user,request.POST)

        return render(request,'quest/registrazione_utente_studio.html', {'form': form})

def esperienza_create_view(request):
    form = EsperienzaCreationForm(request.user)
    if request.method == 'POST':
        form = EsperienzaCreationForm(request.user,request.POST)
        if form.is_valid():
            settore = form.cleaned_data["settore"]
            professione = form.cleaned_data["professione"]
            u = CandidatoEsperienza(candidato =request.user, settore=settore, professione=professione)
            u.save()
            messages.add_message(request,messages.INFO, 'ciao')
            messages.info(request, 'ciao ciao')
            return redirect('esperienza_add')
    return render(request, 'quest/esperienza.html', {'form': form})


def load_professioni(request):
    settore_id = request.GET.get('settore_id')
    professioni = Professione.objects.filter(settore_id=settore_id).all()
    return render(request, 'quest/professione_dropdown_list_options.html', {'professioni': professioni})

def residenza_create_view(request):
#    form = ResidenzaCreationForm(request.user)
    form = ResidenzaCreationForm()
    if request.method == 'POST':
        form = ResidenzaCreationForm(request.POST)
        if form.is_valid():
            amm1 = form.cleaned_data["amm1"]
            amm2 = form.cleaned_data["amm2"]
            amm3 = form.cleaned_data["amm3"]
            amm4 = form.cleaned_data["amm4"]
            u = CandidatoResidenza(candidato = request.user, amm1=amm1, amm2=amm2, amm3=amm3, amm4=amm4)
            u.save()

        return redirect('residenza_add')
    return render(request, 'quest/residenza.html', {'form': form})


def load_amm2(request):
    amm1_id = request.GET.get('amm1_id')
    amm2s = Amm2.objects.filter(amm1_id=amm1_id).all()
    return render(request, 'quest/amm_dropdown_list_options.html', {'items': amm2s})

def load_amm3(request):
    amm2_id = request.GET.get('amm2_id')
    amm3s = Amm3.objects.filter(amm2_id=amm2_id).all()
    return render(request, 'quest/amm_dropdown_list_options.html', {'items': amm3s})

def load_amm4(request):
    amm3_id = request.GET.get('amm3_id')
    amm4s = Amm4.objects.filter(amm3_id=amm3_id).all()
    return render(request, 'quest/amm_dropdown_list_options.html', {'items': amm4s})


def RegistrationExpView(request):
        candidato = request.user
        if request.method == "POST":
                form = EsperienzaForm(request.POST)
                if form.is_valid():
                    professione = form.cleaned_data["professione"]
                    durata = form.cleaned_data["durata"]
                    u = Esperienza(candidato =candidato, professione=professione, durata=durata)
                    u.save()
                    return HttpResponseRedirect('gestione-inserimento/5')
        else:
            form = EsperienzaForm()

        return render(request,'quest/registrazione_utente_esperienza.html', {'form': form})

def RegistrationLangView(request,a=None):
        candidato = request.user
        if request.method == "POST":
                form = LinguaCreationForm(request.user,request.POST)
                if form.is_valid():
                    lingua = form.cleaned_data["lingua"]
                    livello = form.cleaned_data["livello"]
                    u = Linguaconosciuta(candidato =candidato, lingua=lingua, livello=livello)
                    u.save()
                    if a=='a':
                        return HttpResponseRedirect('/17')
                    else:
                        return HttpResponseRedirect('gestione-inserimento/7')
        else:
            form = LinguaCreationForm(request.user,request.POST)

        return render(request,'quest/registrazione_utente_lingua.html', {'form': form})


def ProvaView(request):
#        query = Risposta.objects.filter(utente__id = 5).order_by('-domanda__posizione').first()
#         print(query.domanda)
        return render(request,'quest/prova.html')


def QuestView(request):
        utente = request.user
        if request.method == "POST":
            form = QuestionForm(request.POST)
            if form.is_valid():
                valutazione= form.cleaned_data["valutazione"]
                questionario_id= form.cleaned_data["questionario"]
                domanda_id= form.cleaned_data["domanda"]
                questionario_domanda =QuestionarioDomanda.objects.get(questionario__id =questionario_id, domanda__id = domanda_id)
                v = Risposta(utente=utente,domanda=questionario_domanda ,valutazione=valutazione)
                v.save()
                try:
                    questionario_domanda =QuestionarioDomanda.objects \
                        .get(questionario =questionario_domanda.questionario,
                        posizione=questionario_domanda.posizione +1 )
                    form = QuestionForm(initial={'questionario':questionario_domanda.questionario.id, 'domanda': questionario_domanda.domanda.id })
                except ObjectDoesNotExist:
                    return HttpResponseRedirect(reverse('fine'))
        else:
            questionario = Questionario.objects.get(id=1)
            risposte = Risposta.objects.filter(domanda__questionario =questionario, utente=utente).order_by('-domanda__posizione')
#            print(risposte)
            if len(risposte) == 0:
                questionario_domanda =QuestionarioDomanda.objects.filter(questionario =questionario).order_by('posizione').first()

            else:
                ultima_questionario_domanda = risposte.first().domanda
                try:
                    questionario_domanda =QuestionarioDomanda.objects \
                        .get(questionario =ultima_questionario_domanda.questionario,
                            posizione=ultima_questionario_domanda.posizione +1 )
                except ObjectDoesNotExist:
                    return HttpResponseRedirect(reverse('fine'))

            form = QuestionForm(initial={'questionario':questionario.id, 'domanda': questionario_domanda.domanda.id })

        return render(request,'quest/15.html', {'form': form, 'testo_domanda':questionario_domanda.domanda.testo})

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def RiassuntoCandidato(request):
    candidato = request.user
    lingua = Linguaconosciuta.objects.filter(candidato = candidato)
    studio = Studio.objects.filter(candidato = candidato)
    esperienza = Esperienza.objects.filter(candidato = candidato)
    return render(request,'quest/riassunto_candidato.html', {'lingua': lingua,'studio': studio,'esperienza': esperienza })

def CancellaLingua(request,id):
    Linguaconosciuta.objects.filter(id=id).delete()
    return render(request,'quest/cancella_dato.html')

def CancellaEsperienza(request,id):
    Esperienza.objects.filter(id=id).delete()
    return render(request,'quest/cancella_dato.html')

def CancellaStudio(request,id):
    Studio.objects.filter(id=id).delete()
    return render(request,'quest/cancella_dato.html')

def Tabella(request):
    form = Ricerca(request.user)
    ricerca_candidato = RicercaCandidato(request.GET)

    pred = {'pred': ricerca_candidato.get_objects(),'form':form}
    return render(request,'quest/previsioni.html', pred)

'''
def RicercaCandidato(request):
        if request.method == "POST":
                form = Ricerca(request.POST)
                if form.is_valid():
                    professione = form.cleaned_data["professione"]
                    lingua = form.cleaned_data["lingua"]
                    return HttpResponseRedirect("29/" + professione + "/" + lingua)
        else:
            form = Ricerca()

        return render(request,'quest/ricerca_candidato.html', {'form': form})
'''

def stampa(sender,user,**kwargs):
    logger.debug('sono in stampa')
    logger.debug(sender)
    logger.debug(user)
    logger.debug(kwargs)
    request = kwargs['request']
    tracciamento = request.GET.get('tracciamento',None)
    if tracciamento:
        print(tracciamento)
        azienda_lingua = AziendaLingua.objects.get(azienda= tracciamento, lingua__id = 1)
#        z = CandidatoParametro(candidato = user, parametro = azienda_lingua)
        CandidatoParametro.objects.update_or_create(candidato = user, parametro =azienda_lingua)
#        print(z)
#        z.save()
    print('sono in stampa')



user_logged_in.connect(stampa)

class LoginTracciamento(LoginView):
    pass
