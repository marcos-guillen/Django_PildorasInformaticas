## Proyecto Django según Juan Diaz de Pildoras Informaticas

Esto es un proyecto del curso de Juan Diaz https://www.youtube.com/watch?v=7XO1AzwkPPE&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=1


![](./screenshot.png)

## Esta actualizado hasta el video 64.

### Esta pensado este código para aquellas personas que siguiendo el curso se hayan perdido y no les funcione.


Este código no es totalmente fiel a las clases del explendido profesor Juan Diaz, he realizado algunos cambios que me han parecido adecuados.





* En Blog he puesto un articulo sin imagen y trato de forma diferente las categorias
* En autenticación dejo que alguien anonimo pueda gestionar el carro (para evitar tener que comentar y descomentar lineas de codigo)
* etc.


### Instalación

```
git clone https://github.com/marcos-guillen/Django_PildorasInformaticas.git
cd Django_PildorasInformaticas
pip install -r requirements.txt
```
se tiene que crear un archivo .env en el directorio de la BBDD con el siguiente contenido:
```
SECRET_KEY = TU_CLAVE_secreta
EMAIL_HOST_USER = tu_email_de_gmail
EMAIL_HOST_PASSWORD = la contraseña de tu email
EMAIL1 = el email de to:
EMAIL2 = otro email de to:
```
Ya se puede arrancar el servidor
```
python manage.py runserver
```

Ahora puedes visitar <a href="http://localhost:8000" target="_blank">http://localhost:8000</a> para ver como funciona