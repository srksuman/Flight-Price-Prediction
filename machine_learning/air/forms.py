from django import forms
import datetime
class ArilinesForm(forms.Form):
    airlines_choice =[
        ('IndiGo','IndiGo'  ),
        ('Air India','Air India'),
        ('Jet Airways','Jet Airways'),
        ('SpiceJet','SpiceJet'),
        ('Multiple carriers','Multiple carriers'),
        ('GoAir','GoAir' ),
        ('Vistara','Vistara'),
        ('Vistara Premium economy','Vistara Premium economy'),
        ('Jet Airways Business','Jet Airways Business'),
        ('Multiple carriers Premium economy','Multiple carriers Premium economy'),
        ('Air Asia','Air Asia'),
        ('Trujet','Trujet')
    ]
    stops_c = [
        (0,'Non-Stop'),
        (1,'1 Stop'),
        (2,'2 Stops'),
        (3,'3 Stops'),
        (4,'4 Stops'),
    ]

    source_l = [
        ('Banglore','Banglore'),
        ('Kolkata','Kolkata'),
        ('Delhi','Delhi'),
        ('Chennai','Chennai'),
        ('Mumbai','Mumbai')
    ]
    destination_l = [
        ('Kolkata','Kolkata'),
        ('Banglore','Banglore'),
        ('Delhi','Delhi'),
        ('New Delhi','New Delhi'),
        ('Banglore','Banglore'),
        ('Hyderabad','Hyderabad')
    ]

    depature_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control','placeholder':'2020-07-20 18:20'}))
    arrival_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control','placeholder':'2020-07-20 20:20'}))
    airlines = forms.CharField(label="Airlines",widget=forms.Select(choices=airlines_choice,attrs={'class':'form-control'}))
    stops = forms.CharField(widget=forms.Select(choices=stops_c,attrs={'class':'form-control'}))
    source = forms.CharField(widget=forms.Select(choices=source_l,attrs={'class':'form-control'})) 
    destination = forms.CharField(widget=forms.Select(choices=destination_l,attrs={'class':'form-control'})) 


