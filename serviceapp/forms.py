from django import forms 
from .models import * 

class CompanyForm(forms.ModelForm): 
    class Meta: 
        model=Company 
        fields=("company_name","company_username","company_email","company_create_password","company_image","company_description","company_contact","company_address","company_bankname","company_accountNo","company_ifsc") 
        widgets = {
                'company_description':forms.Textarea(attrs={
                'rows':3, 'cols':52,'style': 'border-radius:10px;',
                }),
                'company_name':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'company_username':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'company_email':forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'company_create_password':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'company_contact':forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'company_address':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'company_bankname':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'company_accountNo':forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'company_ifsc':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),

                }


class ProductForm(forms.ModelForm): 
    class Meta: 
        model=Product 
        fields=("company","product_name","product_image","product_originalPrice","product_sellingPrice","product_color","product_battery","product_screen","product_network","product_features","product_storage") 
        widgets = {
                'company':forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'product_features':forms.Textarea(attrs={
                'rows':3, 'cols':52,'style': 'border-radius:10px;',
                }),
                'product_name':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'product_originalPrice':forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'product_sellingPrice':forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'product_color':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'product_battery':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'product_storage':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'product_screen':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'product_network':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),

                }

BIRTH_YEAR_CHOICES = ['1970', '1971', '1972', '1973', '1974', '1975','1976', '1977', '1978','1979','1980', '1981', '1982', '1983', '1984', '1985','1986', '1987', '1988','1989','1990', '1991', '1992', '1993', '1994', '1995','1996', '1997', '1998','1999','2000','2001','2002','2003','2004','2005','2006']  
STATE_CHOICES = [('andhra pradesh','Andhra Pradesh'),('arunachal pradesh','Arunachal Pradesh'),('assam','Assam'),('bihar','Bihar'),('chhattisgarh','Chhattisgarh'),('goa','Goa'),('gujarat','Gujarat'),('haryana','Haryana'),('himachal pradesh','Himachal Pradesh'),('jharkhand','Jharkhand'),('karnataka','Karnataka'),('kerala','Kerala'),('madhya pradesh','Madhya Pradesh'),('maharastra','Maharastra'),('manipur','Manipur'),('megalaya','Megalaya'),('mizoram','Mizoram'),('nagaland','Nagaland'),('odisha','Odisha'),('punjab','Punjab'),('rajasthan','Rajasthan'),('sikkim','Sikkim'),('tamil nadu','Tamil Nadu'),('telangana','Telangana'),('tripura','Tripura'),('uttarkhand','Uttarkhand'),('uttar pradesh','Uttar Pradesh'),('west bengal','West Bengal')]
class CustomerForm(forms.ModelForm): 
    class Meta: 
        model=Customer 
        fields=("user_fname","user_lname","user_email","user_create_password","user_dob","user_city","user_state","user_pincode","user_contact") 
        
        widgets = {
                
                'user_fname':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'user_lname':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'user_email':forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'user_create_password':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'user_dob':forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES,attrs={
                'class': "form-control",
                'style': 'max-width: 80px;',
                }),
                'user_city':forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px; ',
                }),
                'user_state':forms.Select(choices=STATE_CHOICES,attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                
                'user_pincode':forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
                'user_contact':forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),

                }