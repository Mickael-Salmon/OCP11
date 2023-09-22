import json
from datetime import datetime

def load_clubs():
    """
    Charge la liste des clubs à partir du fichier JSON.
    Returns:
        list: Liste des clubs.
    """
    with open('clubs.json') as clubs_file:
        data = json.load(clubs_file)
        return data['clubs']

def load_competitions():
    """
    Charge la liste des compétitions à partir du fichier JSON.
    Returns:
        list: Liste des compétitions.
    """
    with open('competitions.json') as competitions_file:
        data = json.load(competitions_file)
        return data['competitions']

def sort_competitions_date(competitions):
    """
    Trie les compétitions en fonction de leur date.
    Args:
        competitions (list): Liste des compétitions.
    Returns:
        tuple: Un tuple contenant deux listes, l'une pour les compétitions passées et l'autre pour les compétitions à venir.
    """
    past_competitions = []
    future_competitions = []

    current_datetime = datetime.now()

    for competition in competitions:
        comp_date = datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S')
        if comp_date < current_datetime:
            past_competitions.append(competition)
        else:
            future_competitions.append(competition)

    return past_competitions, future_competitions

def initialize_booked_places(competitions, clubs_list):
    """
    Initialise la liste des places réservées pour chaque compétition et club.
    Args:
        competitions (list): Liste des compétitions.
        clubs_list (list): Liste des clubs.
    Returns:
        list: Liste des places réservées pour chaque compétition et club.
    """
    places_booked = []

    for competition in competitions:
        for club in clubs_list:
            places_booked.append({'competition': competition['name'], 'booked': [0, club['name']]})

    return places_booked

def update_booked_places(competition, club, places_booked, places_required):
    """
    Met à jour la liste des places réservées pour une compétition et un club donnés.
    Args:
        competition (dict): Détails de la compétition.
        club (dict): Détails du club.
        places_booked (list): Liste des places réservées.
        places_required (int): Nombre de places requises.
    Returns:
        list: Liste mise à jour des places réservées.
    Raises:
        ValueError: Si le club tente de réserver plus de 12 places dans une compétition.
    """
    for item in places_booked:
        if item['competition'] == competition['name']:
            if item['booked'][1] == club['name'] and item['booked'][0] + places_required <= 12:
                item['booked'][0] += places_required
                break
            else:
                raise ValueError("You can't book more than 12 places in a competition.")

    return places_booked
