from flask import Flask, render_template, send_from_directory, abort, request, session, redirect, send_file, url_for
import flask
import secrets
import json
from flask import jsonify
from map import Map
import copy
from models.player import Player

app = Flask(__name__, static_url_path='')
m_session = {}
_error = None


# Current Bugs
# * [BUG01]Player properties gets converted to string.


def get_player(s_id, p_id):
    player = [x for x in m_session[s_id].players if x.id == p_id]
    return None if not player else player[0]


@app.errorhandler(404)
def e_404(e):

    return jsonify({"error":  "Requested resource does not exist."})


@app.errorhandler(400)
def e_400(e):

    return jsonify({"error":  e.description})


@app.route("/new/<match_type>")
def new_session(match_type):
    s_id = secrets.token_urlsafe(16)
    sess = Map()
    sess.id = s_id
    sess.players = []
    sess.bracket = {}
    sess.next_bracket_participants = []
    sess.bracket_level = 0
    sess.last_match_generated = 0
    sess.match_type = match_type
    m_session[s_id] = sess

    return jsonify(sess)


@app.route("/<s_id>")
def get_data(s_id):
    if s_id in m_session:
        data = Map(m_session[s_id].copy())
        tmp = []
        for i in data.players:
            tmp.append(i.id)
        data.players = tmp

        tmp = []
        for i in data.next_bracket_participants:
            tmp.append(i.id)
        data.next_bracket_participants = tmp

        print(data)
        return jsonify(data)
    else:
        abort(404)


@app.route("/<s_id>/players")
def get_players(s_id):
    return jsonify([x.__dict__ for x in m_session[s_id].players])
    pass


@app.route("/<s_id>/player/<p_id>", methods=["GET"])
def ret_player(s_id, p_id):
    if not s_id in m_session:
        abort(404)

    player = get_player(s_id, p_id)

    if not player:
        abort(400, "Player ID does not exist!")

    return jsonify(player.__dict__)


@app.route("/<s_id>/add_player", methods=["GET"])
def add_player(s_id):
    if not s_id in m_session:
        abort(404)

    args = {}
    for i in request.args:
        args[i] = str(request.args[i])

    player = Player()
    player.__dict__.update(args)
    m_session[s_id].players.append(player)

    return jsonify(player.__dict__)


@app.route("/<s_id>/player/<p_id>/edit", methods=["GET"])
def edit_player(s_id, p_id):
    if not s_id in m_session:
        abort(404)

    args = {}
    for i in request.args:
        args[i] = str(request.args[i])

    player = get_player(s_id, p_id)

    if not player:
        abort(400, "Player ID does not exist!")

    player.__dict__.update(args)

    return jsonify(player.__dict__)


@app.route("/<s_id>/player/<p_id>/delete", methods=["GET"])
def delete_player(s_id, p_id):
    if not s_id in m_session:
        abort(404)

    args = {}
    for i in request.args:
        args[i] = str(request.args[i])

    player = get_player(s_id, p_id)

    if not player:
        abort(400, "Player ID does not exist!")

    for pos, player in enumerate(m_session[s_id].players):
        if player.id == p_id:
            m_session[s_id].players.pop(pos)

    return get_players(s_id)


@app.route("/<s_id>/generate_bracket")
def generate_bracket(s_id):

    def swap(participants, a, b):
        print(f"Swapping {a} and {b}")
        a, b = participants.index(a), participants.index(b)
        participants[b], participants[a] = participants[a], participants[b]

    if not s_id in m_session:
        abort(404)

    sess = m_session[s_id]

    if sess.bracket_level > 0:
        remaining = [x for x in sess.bracket[sess.bracket_level] if not x["winner"]]
        if remaining:
            abort(400, f"There are still {len(remaining)} matches left in bracket {sess.bracket_level}")


    if sess.next_bracket_participants:
        if len(sess.next_bracket_participants) == 1:
            abort(400, "Cannot generate more brackets. (Tournament Finished)")
        participants = sess.next_bracket_participants
        sess.next_bracket_participants = []
    else:
        participants = [x for x in sess.players if x.lost == "False" or not x.lost]
    # ^ Refer [BUG01] ^

    if sess.bracket_level == 0:
        participants = sorted(participants, key=lambda x: x.combat_level, reverse=True)
        compatible = False
        max_swap = 100
        swaps = 0
        while not compatible:
            compatible = True
            if swaps >= max_swap:
                continue

            for i in range(0, len(participants) - 1, 2):
                if participants[i].gym == participants[i + 1].gym:
                    # Swap players if the first competing bracket are gym mates
                    try:
                        a = (i + 2) if i < len(participants) - 2 else (i - 3)
                        swap(participants, participants[i + 1], participants[a])
                        compatible = False
                        swaps += 1
                    except:
                        print(f"Swap Error: {i}")
                        pass

    print(participants)
    tmp = []
    for i in range(0, len(participants) - 1, 2):
        sess.last_match_generated += 1
        m_no = sess.last_match_generated
        match = dict(   match_number=m_no,
                        player1=participants[i].id,
                        player2=participants[i + 1].id,
                        winner=None)
        tmp.append(match)

    sess.bracket_level += 1
    sess.bracket[sess.bracket_level] = tmp
    # Returns Generated Matches
    return jsonify(tmp)


@app.route("/<s_id>/bracket/<b_id>")
def get_bracket(s_id, b_id):
    if not s_id in m_session:
        abort(404)

    sess = m_session[s_id]
    b_id = int(b_id)

    if b_id in sess.bracket.keys():
        return jsonify(sess.bracket[b_id])
    else:

        abort(400, "Bracket does not exist.")


@app.route("/<s_id>/match/next")
def get_next_match(s_id):
    if not s_id in m_session:
        abort(404)

    sess = m_session[s_id]

    for match in sess.bracket[sess.bracket_level]:
        if not match["winner"]:
            return jsonify(match)

    abort(400, "No more matches left in this bracket.")


@app.route("/<s_id>/match/<m_id>")
def get_match(s_id, m_id):
    if not s_id in m_session:
        abort(404)

    sess = m_session[s_id]

    for match in sess.bracket[sess.bracket_level]:
        if match["match_number"] == int(m_id):
            return jsonify(match)

    abort(400, "Match does not exist.")
    


@app.route("/<s_id>/match/<m_id>/set_winner/<r_id>")
def result_match(s_id, m_id, r_id):
    if not s_id in m_session:
        abort(404)

    sess = m_session[s_id]
    player = get_player(s_id, r_id)
    if not player:
        abort(400, "Player does not exist.")

    for match in sess.bracket[sess.bracket_level]:
        if match["match_number"] == int(m_id):
            if player.id not in [match["player1"], match["player2"]]:
                abort(400, "Player specified is not in this match.")
            else:
                match["winner"] = player.id
                sess.next_bracket_participants.append(player)
                return get_bracket(s_id, sess.bracket_level)



    abort(400, "Match does not exist.")

app.run(host='localhost', port=1122, debug=True)