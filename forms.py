from wtforms import Form,SelectField,StringField,IntegerField,EmailField,validators

class UserForm(Form):
    id=IntegerField('id',[validators.number_range(min=1,max=20,message='Valor no valido')])
    nombre=StringField('nombre',[
        validators.DataRequired(message='Valor no valido')])
    apaterno=StringField('apaterno',[
        validators.DataRequired(message='Valor no valido')])
    email=EmailField('correo',[
        validators.DataRequired(message='Valor no valido'),
        validators.Email(message='Ingresa un correo valido')])
                    