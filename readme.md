***Usage:***
* Make a new tournament through the `/new/<tournament type>` endpoint. Save the session ID, this is the only way you can access the tournament data.
* Populate the tournament with players through the `/<session_id>/add_player` endpoint. Important information must be specified.

    ** Required information:
    ** gym
    ** skill_type
    ** skill_rating
    ** stamina
    ** speed
    ** power

* Generate a new bracket through the `/<session_id>/generate_bracket` endpoint. This will return a list of matches.
* Get the next match through `/<session_id>/match/next`. It will return any important information regarding the match.
* Set a winner through `/<session_id>/match/<match_no>/set_winner/<player_id>`. This will tag the match as complete and set a winner.
* Once all of the matches from this bracket is finished, you need to call `/<session_id>/generate_bracket` again to generate the next set of matches.
* Continue until the final match.



**Endpoint /new/<tournament type>**
```http://localhost:1122/new/<tournament type>```
Creates a new tournament. A session_id is supplied to access the tournament

Example
```http://localhost:1122/new/flyweight```
Reuturns
```json
{
  "bracket": [], 
  "id": "1vYySSg6twYsTTytHI-dKA", 
  "match_type": "flyweight", 
  "players": []
}```


**Endpoint /<session_id>**
```http://localhost:1122/<session_id>```
Returns tournament data and bracket information

Example
```http://localhost:1122/G42GHgc728kLxYuyfGlbfA```

Returns
```json
{
  "bracket": [], 
  "id": "G42GHgc728kLxYuyfGlbfA", 
  "match_type": "bantam", 
  "players": [
    "89109a9f14", 
    "371b0d0ac4", 
    "03ae209a26"...
  ]
}```


**Endpoint /<session_id>/add_player**
```http://localhost:1122/<session_id>/add_player?arguments```
Adds a player to the tournament.

Example
```http://localhost:1122/WgULnabTJrF7Kayo6ZQDmA/add_player?first_name=Alfred&last_name=John```

Returns
```json
{
  "achievement": null, 
  "age": null, 
  "belt": null, 
  "category": null, 
  "coach": null, 
  "dob": null, 
  "first_name": "Alfred", 
  "first_time": true, 
  "gym": null, 
  "height": null, 
  "id": "6e3a7d8b14", 
  "last_name": "John", 
  "middle_name": null, 
  "power": 0, 
  "school_level": null, 
  "seasoned": false, 
  "sex": "m", 
  "skill_rating": 0, 
  "skill_type": "novice", 
  "speed": 0, 
  "stamina": 0, 
  "weight": null
}```

**Endpoint /<session_id>/add_player**
```http://localhost:1122/<session_id>/add_player?arguments```
Adds a player to the tournament.

Example
```http://localhost:1122/WgULnabTJrF7Kayo6ZQDmA/add_player?first_name=Alfred&last_name=John```

Returns
```json
{
  "achievement": null, 
  "age": null, 
  "belt": null, 
  "category": null, 
  "coach": null, 
  "dob": null, 
  "first_name": "Alfred", 
  "first_time": true, 
  "gym": null, 
  "height": null, 
  "id": "6e3a7d8b14", 
  "last_name": "John", 
  "middle_name": null, 
  "power": 0, 
  "school_level": null, 
  "seasoned": false, 
  "sex": "m", 
  "skill_rating": 0, 
  "skill_type": "novice", 
  "speed": 0, 
  "stamina": 0, 
  "weight": null
}```


**Endpoint /<session_id>/players**
```http://localhost:1122/<session_id>/players```
Returns a list of players in a tournament

Example
```http://localhost:1122/XXlI0NqN6usHsPeNtHyzuQ/players```

Returns
```json
[
  {
    "achievement": "National", 
    "age": "20", 
    "belt": "1st Dan Black Belt", 
    "category": "Feather Weight", 
    "coach": "Ahmad Riyahd Fahran", 
    "dob": "1996-09-07", 
    "first_name": "Caisey", 
    "first_time": "No", 
    "gym": "CPU International", 
    "height": "240", 
    "id": "51b68c588a"...
  }, 
  {
    "achievement": "National", 
    "age": "20", 
    "belt": "2nd Dan Black Belt", 
    "category": "Feather Weight", 
    "coach": "Ahmad Riyahd Fahran", 
    "dob": "1996-08-28", 
    "first_name": "James", 
    "first_time": "No", 
    "gym": "CPU International", 
    "height": "240", 
    "id": "eaa624993a", 
    "last_name": "Pelletier"...
  }, 
  {
    "achievement": "National", 
    "age": "20", 
    "belt": "1st Dan Black Belt", 
    "category": "Feather Weight", 
    "coach": "User U User", 
    "dob": "1995-09-02", 
    "first_name": "Cash", 
    "first_time": "No", 
    "gym": "User Gym", 
    "height": "178", 
    "id": "d7ba87156b", 
    "last_name": "Simard"...
  }...
]```

**Endpoint /<session_id>/player/<player_id>**
```http://localhost:1122/<session_id>/player/<player_id>```
Returns player information.

Example
```http://localhost:1122/XXlI0NqN6usHsPeNtHyzuQ/player/51b68c588a```

Returns
```json
{
  "achievement": "National", 
  "age": "20", 
  "belt": "1st Dan Black Belt", 
  "category": "Feather Weight", 
  "coach": "Ahmad Riyahd Fahran", 
  "dob": "1996-09-07", 
  "first_name": "Caisey", 
  "first_time": "No", 
  "gym": "CPU International", 
  "height": "240", 
  "id": "51b68c588a", 
  "last_name": "Brown"...
}```


**Endpoint /<session_id>/player/<player_id>/edit?args**
```http://localhost:1122/<session_id>/player/<player_id>/edit?args```
Edits player data.

Example
```http://localhost:1122/XXlI0NqN6usHsPeNtHyzuQ/player/51b68c588a/edit?first_name=Casey```

Returns
```json
{
  "achievement": "National", 
  "age": "20", 
  "belt": "1st Dan Black Belt", 
  "category": "Feather Weight", 
  "coach": "Ahmad Riyahd Fahran", 
  "dob": "1996-09-07", 
  "first_name": "Casey", 
  "first_time": "No", 
  "gym": "CPU International", 
  "height": "240", 
  "id": "51b68c588a", 
  "last_name": "Brown"...
}```


**Endpoint /<session_id>/generate_bracket**
```http://localhost:1122/<session_id>/generate_bracket```
Generates a bracket and it's corresponding matches.

Example
```http://localhost:1122/XXlI0NqN6usHsPeNtHyzuQ/generate_bracket```

Returns
```json
[
  {
    "match_number": 1, 
    "player1": "bf9af20c5e", 
    "player2": "c7ae61adb3", 
    "winner": null
  }, 
  {
    "match_number": 2, 
    "player1": "433aa54348", 
    "player2": "c59b322e3d", 
    "winner": null
  }, 
  {
    "match_number": 3, 
    "player1": "80856597b9", 
    "player2": "e53f4403ec", 
    "winner": null
  }, 
  {
    "match_number": 4, 
    "player1": "5b35d2e33f", 
    "player2": "e46a3ca970", 
    "winner": null
  }, 
  {
    "match_number": 5, 
    "player1": "38d9daf3bb", 
    "player2": "b9f9fec8db", 
    "winner": null
  }, 
  {
    "match_number": 6, 
    "player1": "4538187758", 
    "player2": "f1abb08ed0", 
    "winner": null
  }...
]```

**Endpoint /<session_id>/bracket/<bracket_no>**
```http://localhost:1122/<session_id>/bracket/<bracket_no>```
Returns a specific bracket

Example
```http://localhost:1122/XXlI0NqN6usHsPeNtHyzuQ/bracket/1```

Returns
```json
[
  {
    "match_number": 1, 
    "player1": "bf9af20c5e", 
    "player2": "c7ae61adb3", 
    "winner": null
  }, 
  {
    "match_number": 2, 
    "player1": "433aa54348", 
    "player2": "c59b322e3d", 
    "winner": null
  }, 
  {
    "match_number": 3, 
    "player1": "80856597b9", 
    "player2": "e53f4403ec", 
    "winner": null
  }, 
  {
    "match_number": 4, 
    "player1": "5b35d2e33f", 
    "player2": "e46a3ca970", 
    "winner": null
  }, 
  {
    "match_number": 5, 
    "player1": "38d9daf3bb", 
    "player2": "b9f9fec8db", 
    "winner": null
  }, 
  {
    "match_number": 6, 
    "player1": "4538187758", 
    "player2": "f1abb08ed0", 
    "winner": null
  }...
]```


**Endpoint /<session_id>/match/next**
```http://localhost:1122/match/next```
Returns the next upcomming match.

Example
```http://localhost:1122/XXlI0NqN6usHsPeNtHyzuQ/match/next```

Returns
```json
{
    "match_number": 1, 
    "player1": "bf9af20c5e", 
    "player2": "c7ae61adb3", 
    "winner": null
}```

**Endpoint /<session_id>/match/<match_no>**
```http://localhost:1122/match/<match_no>```
Returns a specific match info.

Example
```http://localhost:1122/XXlI0NqN6usHsPeNtHyzuQ/match/6```

Returns
```json
{
    "match_number": 6, 
    "player1": "4538187758", 
    "player2": "f1abb08ed0", 
    "winner": null
}```


**Endpoint /<session_id>/match/<m_id>/set_winner/<player_id>**
```http://localhost:1122/match/<m_id>/set_winner/<player_id>```
Sets a winner

Example
```http://localhost:1122/XXlI0NqN6usHsPeNtHyzuQ/match/1/set_winner/bf9af20c5e```

Returns
```json
[
  {
    "match_number": 1, 
    "player1": "bf9af20c5e", 
    "player2": "c7ae61adb3", 
    "winner": "bf9af20c5e"
  }, 
  {
    "match_number": 2, 
    "player1": "433aa54348", 
    "player2": "c59b322e3d", 
    "winner": null
  }, 
  {
    "match_number": 3, 
    "player1": "80856597b9", 
    "player2": "e53f4403ec", 
    "winner": null
  }, 
  {
    "match_number": 4, 
    "player1": "5b35d2e33f", 
    "player2": "e46a3ca970", 
    "winner": null
  }...
]```