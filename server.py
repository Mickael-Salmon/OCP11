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
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        # ... (reste du code)
    except IndexError:
        if request.form['email'] == '':
            flash("Please enter your email.", 'error')
        else:
            flash("No account related to this email.", 'error')
        return render_template('index.html'), 401


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

@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    """Acheter des places pour une compétition donnée."""
    competition_name = request.form['competition']
    club_name = request.form['club']
    places_required = int(request.form['places'])

    # Trouver le club et la compétition correspondants
    competition = [c for c in competitions if c['name'] == competition_name][0]
    club = [c for c in clubs if c['name'] == club_name][0]

    # Initialisation du compteur de places réservées pour ce club et cette compétition
    if 'total_places' not in club:
        club['total_places'] = {}

    # Si la compétition n'est pas déjà dans le compteur, initialisez à 0
    if competition_name not in club['total_places']:
        club['total_places'][competition_name] = 0

    # Calculer le total des places réservées après cette réservation
    total_places_after_this_booking = club['total_places'][competition_name] + places_required

    # Calculer le coût total des places en points
    total_cost = places_required * 3

    # Vérifier si le club a suffisamment de points
    if total_cost > int(club['points']):
        flash("You don't have enough points to complete this booking.")
        return render_template('welcome.html', club=club, competitions=competitions), 400

    # Vérifier si la nouvelle réservation dépasse la limite de 12 places
    if total_places_after_this_booking > 12:
        flash('Cannot book more than 12 places in total for this competition')
        return render_template('welcome.html', club=club, competitions=competitions), 400

    # Si tout est bon, effectuer la réservation et mettre à jour le compteur
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    club['total_places'][competition_name] = total_places_after_this_booking

    # Déduire les points du club
    club['points'] = int(club['points']) - total_cost

    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/booking_route', methods=['POST'])
def booking_route():
    # Votre logique ici
    return jsonify({"message": "Réservation réussie"}), 200

@app.route('/getClubPoints/<club_name>', methods=['GET'])
def get_club_points(club_name):
    club = [c for c in clubs if c['name'] == club_name]
    if not club:
        return jsonify({"message": "Club not found"}), 404
    return jsonify({"points": club[0]['points']})

@app.route('/viewClubPoints')
def view_club_points():
    return render_template('club_points.html', clubs=clubs)


# TODO: Add route for points display

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', form={'csrf_token': 'dummy'})


@app.route('/logout')
def logout():
    return redirect(url_for('index'))