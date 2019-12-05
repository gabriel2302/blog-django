# blog-django

#instalando ambiente virtual
python -m venv venv

#ativando ambiente virtual
source Scripts/activate

#instalando bibliotecas necessárias para funcionar o projeto
pip install -r requirements.txt

#executa antes esse arquivo para verificar se o mysql está instalado
pip freeze

#se não estiver, execute o comando abaixo
#instalando o mysql
pip install mysqlclient-1.4.6-cp38-cp38-win32.whl

#migrando base de dados
python manage.py makemigrations
python manage.py migrate

#criando usuário para acessar área administrativa
python manage.py createsuperuser
#coloque nome de usuário e senha, não esqueça!

#rodando servidor, clique no link (ctrl + clique)
python manage.py runserver