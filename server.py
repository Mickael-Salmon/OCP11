import json
from flask import Flask,render_template,request,redirect,flash,url_for,jsonify
from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)


# @app.route('/book/<competition>/<club>')
# def book(competition,club):
#     foundClub = [c for c in clubs if c['name'] == club][0]
#     foundCompetition = [c for c in competitions if c['name'] == competition][0]
#     if foundClub and foundCompetition:
#         return render_template('booking.html',club=foundClub,competition=foundCompetition)
#     else:
#         flash("Something went wrong-please try again")
#         return render_template('welcome.html', club=club, competitions=competitions)

# @app.route('/book/<competition>/<club>')
# def book(competition, club):
#     foundClub = [c for c in clubs if c['name'] == club]
#     foundCompetition = [c for c in competitions if c['name'] == competition]

#     # Vérifie si le club et la compétition existent
#     if not foundClub or not foundCompetition:
#         return jsonify({"message": "Something went wrong-please try again"}), 404

#     foundClub = foundClub[0]
#     foundCompetition = foundCompetition[0]

#     # Vérifie si la compétition est terminée
#     if foundCompetition.get('closed'):
#         return jsonify({"message": "La compétition est terminée."}), 400

#     # Si tout est bon, continuer normalement
#     return render_template('booking.html', club=foundClub, competition=foundCompetition)

@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club]
    foundCompetition = [c for c in competitions if c['name'] == competition]

    # Vérifie si le club et la compétition existent
    if not foundClub or not foundCompetition:
        return jsonify({"message": "Something went wrong-please try again"}), 404

    foundClub = foundClub[0]
    foundCompetition = foundCompetition[0]

    # Vérifie si la compétition est terminée
    if foundCompetition.get('closed'):
        return jsonify({"message": "La compétition est terminée."}), 400

    # Vérifie si la date de la compétition est passée
    competition_date = datetime.strptime(foundCompetition['date'], '%Y-%m-%d')
    if competition_date < datetime.now():
        return jsonify({"message": "La compétition est terminée."}), 400

    # Si tout est bon, continuer normalement
    return render_template('booking.html', club=foundClub, competition=foundCompetition)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', form={'csrf_token': 'dummy'})


@app.route('/logout')
def logout():
    return redirect(url_for('index'))