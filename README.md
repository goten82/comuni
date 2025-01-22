# Progetto per recuperare il codice Belfiore da un dato comune

## Funzionalità

- Ricerca del codice Belfiore dato il nome del comune
- Ricerca del comune dato il codice Belfiore
- API REST per interrogare il database
- Interfaccia web semplice e intuitiva

## Tecnologie utilizzate

- Python 3
- Flask (framework web)
- SQLAlchemy (ORM)
- SQLite (database)
- HTML/CSS per il frontend

## Installazione

1. Clonare il repository
2. Installare le dipendenze con `pip install -r requirements.txt`
3. Avviare l'applicazione con `python app.py`
4. Aprire il browser all'indirizzo `http://localhost:5000`

## API Endpoints

- GET `/api/comune/<nome>` - Restituisce il codice Belfiore dato il nome del comune
- GET `/api/codice/<codice>` - Restituisce il nome del comune dato il codice Belfiore

## Struttura del progetto

comuni/     
├── app.py          # Applicazione Flask    
├── models.py       # Modelli SQLAlchemy    
├── database.db     # Database SQLite   
├── templates/      # Template HTML     
└── static/         # File statici (CSS, JS)    

## Licenza

MIT License
