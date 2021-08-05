# DeVolada
Equipo (Ingeniería de software)  - **Octa-Ball**  

## Objetivo del proyecto:
Poder comprar y vender artículos desde la comodidad de casa minimizando riesgos ante la contingencia sanitaria global. 
Los compradores y vendedores podrán mostrar sus productos y ofertas sin la necesidad de estar en contacto físicamente. Todo desde casa.

## Equipo de trabajo:
- Karla Denia Salas Jiménez, *responsable de equipo*
- Marco Antonio Orduña Ávila, *responsable técnico*
- Kethrim Guadalupe Trad Mateos, *responsable de la calidad*
- Omar Fernando Gramer Muñoz, *responsable de la colaboración*
- Antonio Reyes Martínez, *responsable de la colaboración*


## Backend

### Instalación Linux
```
cd backend
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
### Instalación Windows
```
cd backend
python3 -m venv venv
venv/bin/activate
pip3 install -r requirements.txt

```


### Ejecución Linux
```
cd backend
source venv/bin/activate
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```
### Ejecución Windows
```
cd backend
venv/bin/activate
set FLASK_APP=main.py
set FLASK_ENV=development
flask run
```



## Frontend

### Instalación Linux y Winodws
```
cd frontend
npm install
```

### Ejecución Linux y Windows
```
cd frontend/
```
y 
```
npm start 
```
ó 
```
ng serve 
```
ó 
```
ng s
```

## Base de datos
### Instalación
```
cd /backend/database/data
mysql -u root -p < ../DDL.sql
mysql -u root -p mydb < ../DML.sql
```