import traceback

from flask import render_template, request, redirect, url_for, flash

from config import app
from models import db, Artist

@app.route('/agents', methods=['GET'])
def artists_find():
    name_to_find = request.args.get("name")
    spotify_id_to_find = request.args.get("spotify")
    genius_id_to_find = request.args.get("genius")

    if name_to_find is None:
        name_to_find = ""
    if spotify_id_to_find is None:
        spotify_id_to_find = ""
    if genius_id_to_find is None:
        genius_id_to_find = ""

    name_search = "%{}%".format(name_to_find)
    spotify_search = "%{}%".format(spotify_id_to_find)
    genius_search = "%{}%".format(genius_id_to_find)

    all_rows = Artist.query \
        .filter(Artist.artist_name.ilike(name_search)) \
        .filter(Artist.artist_spotify_id.ilike(spotify_search)) \
        .filter(Artist.artist_genius_id.ilike(genius_search))
    return render_template("artists.html", artists=all_rows.all())

@app.route('/artists', methods=['GET'])
def artists():
    all_artists = Artist.query.all()
    return render_template("artists.html", artists=all_artists)

@app.route('/artists', methods=['POST'])
def add_artist():
    try:
       artist_name = request.form.get('newArtistName')
       artist_spotify = request.form.get('newArtistSpotify')
       artist_genius = request.form.get('newArtistGenius')
       artist_photo_url = request.form.get('newArtistPhoto')
       new_artist = Artist(
           artist_name = artist_name,
           artist_spotify_id =  artist_spotify,
           artist_genius_id =  artist_genius,
           artist_photo = artist_photo_url
       )
       db.session.add(new_artist)
       db.session.commit()
    except Exception:
        return redirect(url_for('artists'))
    return redirect(url_for('artists'))

@app.route('/artists/delete', methods=['POST'])
def delete_artist():
    artist_id = request.form.get('artist_ID')
    try:
        artist = Artist.query.filter(Artist.artist_id == artist_id).first()
        db.session.delete(artist)
        db.session.commit()
    except Exception:
        return redirect(url_for('artists'))
    return redirect(url_for('artists'))

@app.route('/artists/edit', methods=['POST'])
def edit_artist():
    try:
        curr_id = request.form.get('artist_ID')
        Artist.query.filter(Artist.artist_id == curr_id).update(
            {
                'artist_name': request.form.get('artist_name'),
                'artist_spotify_id': request.form.get('artist_spotify_id'),
                'artist_genius_id': request.form.get('artist_genius_id'),
                'artist_photo': request.form.get('artist_photo'),
            })
        db.session.commit()
    except Exception:
        traceback.print_exc()
    return redirect(url_for('artists'))