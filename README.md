# projeto-integrador-I
Este repositório contém o código fonte do cardápio virtual acessado através da tecnologia QR Code.


Referências:
Criar QR Code:
https://betterprogramming.pub/how-to-generate-and-decode-qr-codes-in-python-a933bce56fd0

Criar projeto CRUD em Django com frontend:
https://www.javatpoint.com/django-crud-application

Criar sistema de autenticação:
https://learndjango.com/tutorials/django-login-and-logout-tutorial

Criar sistema de integração de imagens:
https://cloudinary.com/documentation/upload_widget

Criar usuario no Heroku:
heroku run python manage.py createsuperuser

Como ligar/desligar uma base de dados MySQL e saber o status:
sudo service mysql status
sudo service mysql stop
sudo service mysql start
sudo service mysql restart

sudo mysql -u root -p
>>password

Realizar migrações da base de dados (Modelagem automatica):
python3 manage.py makemigrations
python3 manage.py migrate

Ligar aplicação django:
python3 manage.py runserver
gunicorn --chdir ./cardapio cardapio.wsgi:application

Credenciais temporarias para teste:
greencontainer
adminunivespadmin