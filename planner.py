gamers = []

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")

anna = {
    'name': 'Anna Brown',
    'availability': ["Monday", "Tuesday", "Friday"]
}

add_gamer(anna, gamers)

add_gamer({'name': 'Beatrice Nelson', 'availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Carl Jones', 'availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Danny White', 'availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Evelyn Hanni', 'availability': ["thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Fred Hope', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Gretta Lynn', 'availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Helen Sellers', 'availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Ian Barnes', 'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Jillian Brown', 'availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequencey_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)

def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    return [gamer for gamer in gamers_list if day in gamer['availability']]

attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)

form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
The Sorcery Society
"""

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")

unable_to_attend_best_night = [gamer for gamer in gamers if game_night notin gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")