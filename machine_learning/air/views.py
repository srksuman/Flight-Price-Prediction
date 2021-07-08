from django import forms
from django.shortcuts import render
from .forms import ArilinesForm
import pandas as pd
import pickle
# Create your views here.
def form_data(request):
    if request.method == 'POST':
        form = ArilinesForm(request.POST)
        if form.is_valid():
            dep_date = form.cleaned_data['depature_date']
            Day_of_Journey = int(pd.to_datetime(dep_date).day)
            month_of_Journey = int(pd.to_datetime(dep_date).month)   
            Dep_Time_hours = int(pd.to_datetime(dep_date).hour)
            Dep_Time_minute = int(pd.to_datetime(dep_date).minute)
            print(Dep_Time_minute)

            date_arr = form.cleaned_data["arrival_date"]
            Arrival_hour = int(pd.to_datetime(date_arr).hour)
            Arrival_min = int(pd.to_datetime(date_arr).minute)
            
            Duration_hour = abs(Arrival_hour - Dep_Time_hours)
            Duration_minute = abs(Arrival_min - Dep_Time_minute)

            Total_stops = form.cleaned_data["stops"]
            airline=form.cleaned_data['airlines']
            if(airline=='Jet Airways'):
                Jet_Airways = 1
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 

            elif (airline=='IndiGo'):
                Jet_Airways = 0
                IndiGo = 1
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 

            elif (airline=='Air India'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 1
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
                
            elif (airline=='Multiple carriers'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 1
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
                
            elif (airline=='SpiceJet'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 1
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
                
            elif (airline=='Vistara'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 1
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline=='GoAir'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 1
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline=='Multiple carriers Premium economy'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 1
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline=='Jet Airways Business'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 1
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline=='Vistara Premium economy'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 1
                Trujet = 0
                
            elif (airline=='Trujet'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 1

            else:
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            Source = form.cleaned_data["source"]
            if (Source == 'Delhi'):
                source_Delhi = 1
                source_Kolkata = 0
                source_Mumbai = 0
                source_Chennai = 0

            elif (Source == 'Kolkata'):
                source_Delhi = 0
                source_Kolkata = 1
                source_Mumbai = 0
                source_Chennai = 0

            elif (Source == 'Mumbai'):
                source_Delhi = 0
                source_Kolkata = 0
                source_Mumbai = 1
                source_Chennai = 0

            elif (Source == 'Chennai'):
                source_Delhi = 0
                source_Kolkata = 0
                source_Mumbai = 0
                source_Chennai = 1

            else:
                source_Delhi = 0
                source_Kolkata = 0
                source_Mumbai = 0
                source_Chennai = 0

            destination = form.cleaned_data["destination"]
            if (destination == 'Cochin'):
                destination_Cochin = 1
                destination_Delhi = 0
                destination_New_Delhi = 0
                destination_Hyderabad = 0
                destination_Kolkata = 0
            
            elif (destination == 'Delhi'):
                destination_Cochin = 0
                destination_Delhi = 1
                destination_New_Delhi = 0
                destination_Hyderabad = 0
                destination_Kolkata = 0

            elif (destination == 'New_Delhi'):
                destination_Cochin = 0
                destination_Delhi = 0
                destination_New_Delhi = 1
                destination_Hyderabad = 0
                destination_Kolkata = 0

            elif (destination == 'Hyderabad'):
                destination_Cochin = 0
                destination_Delhi = 0
                destination_New_Delhi = 0
                destination_Hyderabad = 1
                destination_Kolkata = 0

            elif (destination == 'Kolkata'):
                destination_Cochin = 0
                destination_Delhi = 0
                destination_New_Delhi = 0
                destination_Hyderabad = 0
                destination_Kolkata = 1

            else:
                destination_Cochin = 0
                destination_Delhi = 0
                destination_New_Delhi = 0
                destination_Hyderabad = 0
                destination_Kolkata = 0
            file_data = open('C:\\Users\\suman\\OneDrive\\Desktop\\summer class\\Data Science\\model.pkl','rb')
            model = pickle.load(file_data)
            prediction=model.predict([[
            Total_stops,
            Day_of_Journey,
            month_of_Journey,
            Dep_Time_hours,
            Dep_Time_minute,
            Arrival_hour,
            Arrival_min,
            Duration_hour,
            Duration_minute,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            source_Chennai,
            source_Delhi,
            source_Kolkata,
            source_Mumbai,
            destination_Cochin,
            destination_Delhi,
            destination_Hyderabad,
            destination_Kolkata,
            destination_New_Delhi
        ]])
        price = prediction[0]
        print(prediction)
        return render(request,"data.html",{'form':form,"price":round(price,2),"Source":Source,"Airline":airline,"destination":destination})

    else:    
        form = ArilinesForm()
        return render(request,"data.html",{'form':form})