from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from mercado.models import User

class CadastroForm(FlaskForm):
    def validate_username(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuario ja existe! Cadastre outro usuario")

    def validate_email(self, check_email):
        user = User.query.filter_by(usuario=check_email.data).first()
        if user:
            raise ValidationError("Email ja existe! Cadastre outro Email")
        
    def validate_senha(self, check_senha):
        user = User.query.filter_by(usuario=check_senha.data).first()
        if user:
            raise ValidationError("Senha ja existe! Cadastre outra senha")
        
    usuario = StringField(label='Username:', validators=[Length(min=2,max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha', validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label='Confirmação da senha', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')


class LoginForm(FlaskForm):
    usuario = StringField(label='usuario', validators=[DataRequired()])
    senha = PasswordField(label='senha',validators=[DataRequired()])
    submit = SubmitField(label='log in')


class CompraProdutoForm(FlaskForm):
    submit = SubmitField(label='Comprar Produto!')

class VendaProdutoForm(FlaskForm):
    submit = SubmitField(label='Vender Produto!')