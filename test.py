from models.player import Player
import requests
import shlex
import random

sample_data = """(1, 'Simpas', 'Jim', 'Robles', 20, 'Male', '1996-09-07', 'Ahmad Riyahd Fahran', 'CPU International', 68, 240, 'No', 'Yes', 'No', 'Advance', 8, 6, 5, 5, 'National', '1st Dan Black Belt', 'College', 'Feather Weight'),
    (2, 'Robles', 'Marshall', 'S.', 20, 'Male', '1996-08-28', 'Ahmad Riyahd Fahran', 'CPU International', 72, 240, 'No', 'Yes', 'No', 'Advance', 5, 8, 6, 6, 'National', '2nd Dan Black Belt', 'College', 'Feather Weight'),
    (3, 'player', 'player', 'player', 20, 'Male', '1995-09-02', 'User U User', 'User Gym', 68, 178, 'No', 'Yes', 'No', 'Advance', 5, 2, 6, 7, 'National', '1st Dan Black Belt', 'College', 'Feather Weight'),
    (4, 'player2', 'player2', 'player2', 20, 'Male', '1996-01-28', 'User U User', 'User Gym', 56, 172, 'No', 'Yes', 'No', 'Advance', 5, 3, 9, 5, 'National', '3rd Dan Black Belt', 'College', 'Fin Weight'),
    (5, 'player3', 'player3', 'player3', 20, 'Male', '1995-09-21', 'User U User', 'User Gym', 58, 178, 'No', 'Yes', 'No', 'Advance', 8, 7, 2, 5, 'National', '2nd Dan Black Belt', 'College', 'Fly Weight'),
    (6, 'player4', 'player4', 'player4', 18, 'Male', '1997-02-08', 'User U User', 'User Gym', 59, 178, 'No', 'Yes', 'No', 'Advance', 5, 7, 8, 6, 'National', '3rd Dan Black Belt', 'College', 'Bantam Weight'),
    (7, 'player5', 'player5', 'player5', 20, 'Male', '1995-02-06', 'User U User', 'User Gym', 72, 180, 'No', 'Yes', 'No', 'Advance', 8, 7, 6, 8, 'National', '2nd Dan Black Belt', 'College', 'Welter Weight'),
    (8, 'player6', 'player6', 'player6', 18, 'Female', '1998-08-08', 'User U User', 'User Gym', 46, 172, 'No', 'Yes', 'No', 'Advance', 8, 7, 9, 5, 'National', '3rd Dan Black Belt', 'College', 'Fin Weight'),
    (9, 'player7', 'player7', 'player7', 20, 'Female', '1996-07-02', 'User U User', 'User Gym', 49, 18, 'No', 'Yes', 'No', 'Advance', 8, 7, 6, 5, 'National', '2nd Dan Black Belt', 'College', 'Fly Weight'),
    (10, 'player8', 'player8', 'player8', 20, 'Female', '1996-08-03', 'User U User', 'User Gym', 53, 170, 'No', 'Yes', 'No', 'Advance', 5, 6, 7, 8, 'National', '2nd Dan Black Belt', 'College', 'Bantam Weight'),
    (11, 'player9', 'player9', 'player', 20, 'Female', '1996-08-02', 'User U User', 'User Gym', 57, 171, 'No', 'Yes', 'No', 'Advance', 6, 7, 5, 9, 'National', '2nd Dan Black Belt', 'College', 'Feather Weight'),
    (12, 'player10', 'player10', 'player10', 21, 'Female', '1995-08-08', 'User U User', 'User Gym', 62, 172, 'No', 'Yes', 'No', 'Advance', 6, 7, 8, 9, 'National', '2nd Dan Black Belt', 'College', 'Light Weight'),
    (13, 'player11', 'player11', 'player11', 20, 'Male', '1996-08-02', 'test test test', 'Test Gym', 54, 169, 'No', 'Yes', 'No', 'Advance', 5, 6, 7, 8, 'National', '2nd Dan Black Belt', 'College', 'Fin Weight'),
    (14, 'player12', 'player12', 'player12', 20, 'Male', '1996-08-02', 'test test test', 'Test Gym', 59, 172, 'No', 'Yes', 'No', 'Advance', 5, 6, 7, 6, 'National', '2nd Dan Black Belt', 'College', 'Fly Weight'),
    (15, 'player13', 'player13', 'player13', 20, 'Male', '1997-08-07', 'test test test', 'Test Gym', 63, 175, 'No', 'Yes', 'No', 'Advance', 7, 8, 9, 9, 'National', '2nd Dan Black Belt', 'College', 'Bantam Weight'),
    (16, 'player14', 'player14', 'player', 20, 'Female', '1995-09-01', 'test test test', 'Test Gym', 57, 182, 'No', 'Yes', 'No', 'Advance', 6, 7, 8, 9, 'National', '2nd Dan Black Belt', 'College', 'Fin Weight'),
    (17, 'player15', 'player15', 'player15', 20, 'Female', '1997-08-02', 'test test test', 'Test Gym', 59, 176, 'No', 'Yes', 'No', 'Advance', 6, 7, 8, 9, 'National', '2nd Dan Black Belt', 'College', 'Fly Weight'),
    (18, 'player16', 'player16', 'player16', 20, 'Female', '1995-08-08', 'test test test', 'Test Gym', 60, 175, 'No', 'Yes', 'No', 'Advance', 7, 8, 9, 7, 'National', '2nd Dan Black Belt', 'College', 'Bantam Weight'),
    (19, 'player19', 'player19', 'player19', 20, 'Male', '1996-01-08', 'demo test test', 'Testing Gym', 54, 176, 'No', 'Yes', 'No', 'Advance', 6, 7, 8, 6, 'National', '2nd Dan Black Belt', 'College', 'Fin Weight'),
    (20, 'player20', 'player20', 'player20', 20, 'Male', '1996-09-08', 'demo test test', 'Testing Gym', 59, 179, 'No', 'Yes', 'No', 'Advance', 7, 8, 7, 8, 'National', '3rd Dan Black Belt', 'College', 'Fly Weight'),
    (21, 'player21', 'player21', 'player21', 20, 'Male', '1996-08-09', 'demo test test', 'Testing Gym', 63, 180, 'No', 'Yes', 'No', 'Advance', 7, 8, 9, 7, 'National', '2nd Dan Black Belt', 'College', 'Bantam Weight'),
    (22, 'player22', 'player22', 'player22', 19, 'Female', '1997-08-08', 'demo test test', 'Testing Gym', 52, 169, 'No', 'Yes', 'No', 'Advance', 7, 8, 9, 7, 'National', '2nd Dan Black Belt', 'College', 'Fin Weight'),
    (23, 'player23', 'player23', 'player23', 18, 'Female', '1998-08-04', 'demo test test', 'Testing Gym', 59, 170, 'No', 'Yes', 'No', 'Advance', 7, 8, 9, 7, 'National', '2nd Dan Black Belt', 'College', 'Fly Weight'),
    (24, 'player24', 'player24', 'player24', 20, 'Female', '1996-09-09', 'demo test test', 'Testing Gym', 60, 172, 'No', 'Yes', 'No', 'Advance', 7, 8, 9, 9, 'National', '3rd Dan Black Belt', 'College', 'Bantam Weight'),
    (25, 'player27', 'player27', 'player27', 20, 'Male', '1996-08-08', 'coach coach coach', 'Coach Gym', 56, 170, 'No', 'Yes', 'No', 'Advance', 3, 4, 5, 3, 'National', '1st Dan Black Belt', 'College', 'Fin Weight'),
    (26, 'player28', 'player28', 'player28', 18, 'Male', '1998-08-08', 'coach coach coach', 'Coach Gym', 59, 175, 'No', 'Yes', 'No', 'Advance', 4, 4, 3, 4, 'National', '1st Dan Black Belt', 'College', 'Fly Weight'),
    (27, 'player29', 'player29', 'player29', 20, 'Male', '1996-09-02', 'coach coach coach', 'Coach Gym', 63, 175, 'No', 'Yes', 'No', 'Advance', 4, 4, 5, 3, 'National', '1st Dan Black Belt', 'College', 'Bantam Weight'),
    (28, 'player30', 'player30', 'player30', 19, 'Female', '1997-08-02', 'coach coach coach', 'Coach Gym', 52, 169, 'No', 'Yes', 'No', 'Advance', 4, 4, 4, 5, 'National', '1st Dan Black Belt', 'College', 'Fin Weight'),
    (29, 'player31', 'player31', 'player31', 19, 'Female', '1997-05-03', 'coach coach coach', 'Coach Gym', 56, 171, 'No', 'Yes', 'No', 'Advance', 4, 4, 5, 5, 'National', '1st Dan Black Belt', 'College', 'Fly Weight'),
    (30, 'player32', 'player32', 'player32', 18, 'Female', '1998-07-07', 'coach coach coach', 'Coach Gym', 50, 172, 'No', 'Yes', 'No', 'Advance', 4, 3, 4, 5, 'National', '1st Dan Black Belt', 'College', 'Bantam Weight'),
    (31, 'Sim', 'Rim', 'J.', 20, 'Male', '1996-08-02', 'Ahmad Riyahd Fahran', 'MVP Gym', 68, 178, 'No', 'Yes', 'No', 'Advance', 10, 9, 9, 9, 'National', '2nd Dan Black Belt', 'College', 'Feather Weight'),
    (32, 'mike', 'mike', 'M.', 20, 'Male', '1996-09-09', 'Ahmad Riyahd Fahran', 'MVP Gym', 68, 180, 'No', 'Yes', 'No', 'Advance', 8, 8, 6, 7, 'National', '2nd Dan Black Belt', 'Highschool', 'Feather Weight');"""

data =  [shlex.split(data.replace("(", "").replace(")", "").replace(",", "")) for data in sample_data.split("\n")]
names = requests.post("https://uinames.com/api/?amount=35&region=canada").json()
c_data = []
for d in data:
    n_data = names.pop()
    n_player = Player()
    n_player.last_name = n_data["surname"]
    n_player.first_name = n_data["name"]
    n_player.sex = n_data["gender"]
    n_player.age = d[4]
    n_player.dob = d[6]
    n_player.coach = d[7]
    n_player.gym = d[8]
    n_player.weight = d[9]
    n_player.height = d[10]
    n_player.first_time = d[11]
    n_player.seasoned = bool(d[12])
    n_player.skill_type = d[14]
    n_player.skill_rating = d[15]
    n_player.stamina = d[16]
    n_player.speed = d[17]
    n_player.power = d[18]
    n_player.achievement = d[19]
    n_player.belt = d[20]
    n_player.school_level = d[21]
    n_player.category = d[22]
    c_data.append(n_player)

session_id = requests.get("http://localhost:1122/new/bantam").json()["id"]
print(session_id)
for player in c_data:
    x = requests.get(f"http://localhost:1122/{session_id}/add_player", params=player.__dict__)
    print(x.json()["id"])

bracket_data = requests.get(f"http://localhost:1122/{session_id}/generate_bracket")
assert "error" not in bracket_data.json()
print(f"Bracket Generated")

while True:
    match = requests.get(f"http://localhost:1122/{session_id}/match/next").json()
    if "error" in match:
        new_bracket = requests.get(f"http://localhost:1122/{session_id}/generate_bracket").json()
        if "error" in new_bracket:
            break
    else:
        print(match)
        winner = random.choice([match["player1"], match["player2"]])
        match_data = requests.get(f"http://localhost:1122/{session_id}/match/{match['match_number']}/set_winner/{winner}")
        print(f"Setting winner: {winner}")