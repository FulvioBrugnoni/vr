from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CandidatoForm(UserCreationForm):
        email = forms.EmailField(label='user', max_length=25)
        tracciamento = forms.CharField(label='tracciamento', max_length=25, widget=forms.HiddenInput())
        ruolo = forms.IntegerField( widget=forms.HiddenInput(), initial = MyUser.STUDENTE )
        class Meta:
            model = MyUser
            fields = ('email','password1','password2','tracciamento')
        def save(self,commit = True):
            user = super(CandidatoForm, self).save(commit=False)
            user.ruolo = self.cleaned_data['ruolo']
            tracciamento = self.cleaned_data['tracciamento']
            azienda_lingua = AziendaLingua.objects.get(azienda= tracciamento, lingua__id = 1)
            z = CandidatoParametro(candidato = user, parametro = azienda_lingua)
            if commit:
                user.save()
                z.save()
            return user,z

class AnagraficaForm(forms.Form):
        nome = forms.CharField(label= _('form.anagrafica.nome'), max_length=25)
        cognome = forms.CharField(label='cognome', max_length=25)
        codicefiscale = forms.CharField(label='codicefiscale', max_length=10)
        eta = forms.IntegerField()
        gender = forms.CharField(label='gender', max_length=1)



class StudioForm(forms.Form):
        titolo = forms.CharField(label='titolo', max_length=25)

class LinguaForm(forms.Form):
        lingua = forms.CharField(label='lingua', max_length=25)
        livello = forms.CharField(label='livello', max_length=25)

class QuestionForm(forms.Form):
    questionario = forms.IntegerField()
    domanda = forms.IntegerField()
#     valutazione = forms.CharField()
    CHOICES=[('1','1'),
             ('2','2'),
             ('3','3'),
             ('4','4'),
             ('5','5'),
             ('6','6'),
             ('7','7'),]
    valutazione = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label= 'Ciao')


class MyUserChangeForm(UserChangeForm):
    ruolo = forms.IntegerField()

    class Meta(UserChangeForm.Meta):
        model = MyUser



class EsperienzaCreationForm(forms.ModelForm):

    class Meta:
        model = CandidatoEsperienza
        fields = ['settore','professione',]

    def __init__(self,user,*args, **kwargs):
        super().__init__(*args, **kwargs)
        azienda = AziendaLingua.objects.filter(candidatoparametro__candidato = user).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        self.fields['settore'] = forms.ModelChoiceField(queryset = Settore.objects.filter(lingua__id = lingua))
        self.fields['professione'].queryset = Professione.objects.none()
        print(self.data)
        if 'settore' in self.data:
            try:
                settore_id = int(self.data.get('settore'))
                self.fields['professione'].queryset = Professione.objects.filter(settore_id=settore_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['professione'].queryset = self.instance.settore.professione_set.order_by('name')


class ResidenzaCreationForm(forms.ModelForm):
#    def __init__(self,user,*args,**kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['amm1'] = forms.ModelChoiceField(queryset = Amm1.objects.filter(lingua__id = 1))
    class Meta:
        model = CandidatoResidenza
        fields = ['amm1','amm2','amm3','amm4']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['amm2'].queryset = Amm2.objects.none()
        self.fields['amm3'].queryset = Amm3.objects.none()
        self.fields['amm4'].queryset = Amm4.objects.none()

        if 'amm1' in self.data:
            try:
                amm1_id = int(self.data.get('amm1'))
                self.fields['amm2'].queryset = Amm2.objects.filter(amm1_id=amm1_id)
            except (ValueError, TypeError):
                pass

        if 'amm2' in self.data:
            try:
                amm2_id = int(self.data.get('amm2'))
                self.fields['amm3'].queryset = Amm3.objects.filter(amm2_id=amm2_id)
            except (ValueError, TypeError):
                pass

        if 'amm3' in self.data:
            try:
                amm3_id = int(self.data.get('amm3'))
                self.fields['amm4'].queryset = Amm4.objects.filter(amm3_id=amm3_id)
            except (ValueError, TypeError):
                pass



class StudioCreationForm(forms.ModelForm):

    class Meta:
        model = Studio
        fields = '__all__'

    def __init__(self,user,*args, **kwargs):
        super().__init__(*args, **kwargs)
        azienda = AziendaLingua.objects.filter(candidatoparametro__candidato = user).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        self.fields['materia'] = forms.ModelChoiceField(queryset = Materia.objects.filter(lingua__id = lingua))
        self.fields['titolo'] = forms.ModelChoiceField(queryset = Titolo.objects.filter(lingua__id = lingua))
        print(self.data)


class LinguaCreationForm(forms.ModelForm):

    class Meta:
        model = Linguaconosciuta
        fields = '__all__'

    def __init__(self,user,*args, **kwargs):
        super().__init__(*args, **kwargs)
        azienda = AziendaLingua.objects.filter(candidatoparametro__candidato = user).first().id
        lingua = Lingua.objects.filter(aziendalingua__id = azienda).first().id
        self.fields['lingua'] = forms.ModelChoiceField(queryset = Lang.objects.filter(lingua__id = lingua))
        self.fields['livello'] = forms.ModelChoiceField(queryset = Livello.objects.filter(lingua__id = lingua))
        print(self.data)

class Ricerca(ResidenzaCreationForm, LinguaCreationForm):
        pass
