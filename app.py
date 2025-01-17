from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configura il percorso del database SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza SQLAlchemy
db = SQLAlchemy(app)


USER_NOT_FOUND = "Comune not found"
# Definisci un modello per rappresentare una tabella
class Comuni(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comune = db.Column(db.String(50), nullable=False)
    provincia = db.Column(db.String(25), unique=True, nullable=False)
    codice_belfiore = db.Column(db.String(4), nullable=True)

    def __repr__(self):
        return f'<Comune {self.comune}>'
    
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/add_comune', methods=['POST'])
def add_comune():
    comune = request.form.get('comune')
    provincia = request.form.get('provincia')
    codice_belfiore = request.form.get('codice_belfiore')

    # Crea un nuovo oggetto Comune
    new_comune = Comuni(comune=comune, provincia=provincia, codice_belfiore=codice_belfiore) # type: ignore
    db.session.add(new_comune)  # Aggiunge l'comune alla sessione
    db.session.commit()       # Salva nel database

    return jsonify({"message": "Comune added successfully!"})

@app.route('/comuni', methods=['GET'])
def get_comuni():
    comuni = Comuni.query.all()
    comune_data = [{"id": comune.id,"comune": comune.comune, "provincia": comune.provincia, "codice_belfiore": comune.codice_belfiore} for comune in comuni]
    return jsonify(comune_data)

@app.route('/comune/id/<int:comune_id>', methods=['GET'])
def get_comune_by_id(comune_id):
   
    comune = Comuni.query.get(comune_id)  # Cerca il comune in base all'ID
    if not comune:
        return jsonify({"message": USER_NOT_FOUND}), 404

    # Restituisce i dati del comune in formato JSON
    comune_data = {
        "id": comune.id,
        "comune": comune.comune,
        "provincia": comune.provincia,
        "codice_belfiore": comune.codice_belfiore
    }
    return jsonify(comune_data)

@app.route('/comune/codice/<string:comune_codice_belfiore>', methods=['GET'])
def get_comune_by_cb(comune_codice_belfiore):

    comune = Comuni.query.filter_by(codice_belfiore=comune_codice_belfiore).first()  # Cerca l'utente in base all'ID filter_by(name=name).first()
    if not comune:
        return jsonify({"message": USER_NOT_FOUND}), 404

    # Restituisce i dati dell'utente in formato JSON
    user_data = {
        "id": comune.id,
        "comune": comune.comune,
        "provincia": comune.provincia,
        "codice_belfiore": comune.codice_belfiore
    }
    return jsonify(user_data)

@app.route('/comune/comune/<string:comune_comune>', methods=['GET'])
def get_comune_by_comune(comune_comune):
    #filter(Comuni.comune.ilike(f"%{comune_comune}%")).all()
    comuni = Comuni.query.filter(Comuni.comune.ilike(f"%{comune_comune}%")).all()  # Cerca l'utente in base all'ID filter_by(name=name).first()
    if not comuni:
        return jsonify({"message": "User not found"}), 404

    # Restituisce i dati dell'utente in formato JSON
    user_data = [
        {
        "id": comune.id,
        "comune": comune.comune,
        "provincia": comune.provincia,
        "codice_belfiore": comune.codice_belfiore
    } for comune in comuni]
    return jsonify(user_data)

@app.route('/update_comune/<int:comune_id>', methods=['PUT'])
def update_comune(comune_id):
    comune = Comuni.query.get(comune_id)  # Cerca l'utente per ID
    if not comune:
        return jsonify({"message": "Comune not found"}), 404

    # Ottiene i nuovi dati dal corpo della richiesta
    comune = request.json.get('comune', comune.comune)  # type: ignore # Usa il nome attuale come valore di default
    provincia = request.json.get('provincia', comune.provincia) # type: ignore
    codice_belfiore = request.json.get('codice_belfiore', comune.codice_belfiore) # type: ignore

    # Aggiorna i campi dell'utente
    comune.comune = comune
    comune.provincia = provincia
    comune.codice_belfiore = codice_belfiore
    db.session.commit()  # Salva le modifiche nel database

    return jsonify({"message": "User updated successfully!"})


@app.route('/delete_comune/<int:comune_id>', methods=['DELETE'])
def delete_comune(comune_id):
    comune = Comuni.query.get(comune_id)
    if not comune:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(comune)  # Elimina l'utente dal database
    db.session.commit()

    return jsonify({"message": "User deleted successfully!"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)