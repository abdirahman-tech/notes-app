Notes & Todo App
Beskrivelse av løsningen
En enkel notatapplikasjon med en klient og en server. Serveren lagrer tekstnotater og todo-lister i en SQLite-database og gjør dem tilgjengelige gjennom et REST-API. Klienten bruker dette API-et til å opprette og hente notater og lister.

Server: Python med FastAPI og SQLite-database
Klient: HTML/CSS/JavaScript i nettleser, samt en Python CLI-klient
API: REST med JSON


Hvordan installere og starte serveren
bashcd server
pip3 install -r requirements.txt
python3 -m uvicorn server:app --reload --host 127.0.0.1 --port 8000

Hvordan starte klienten
Start en ny terminal og kjør:
bashcd client
python3 -m http.server 3000
Åpne deretter nettleseren og gå til http://localhost:3000

Eksempler på bruk av API
Opprett et tekstnotat
bashcurl -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "Handleliste", "content": "Melk, egg, brød"}'
Hent alle notater
bashcurl http://127.0.0.1:8000/notes
Opprett en todo-liste
bashcurl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Lekser", "tasks": [{"text": "Matte", "completed": false}, {"text": "Norsk", "completed": false}]}'
Hent alle todo-lister
bashcurl http://127.0.0.1:8000/todos

CLI-klient
bashcd client_cli
python3 klient.py list notes
python3 klient.py list todos
python3 klient.py add note "Tittel" "Innhold"
python3 klient.py add todo "Min liste" "Oppgave 1" "Oppgave 2"