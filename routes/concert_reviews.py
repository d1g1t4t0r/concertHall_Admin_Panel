import traceback

from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import asc
from config import app
from models import db, ConcertReview, User






# @app.route('/models/edit', methods=['POST'])
# def edit_model():
#     try:
#         curr_id = request.form.get('model_ID')
#         Models.query.filter(Models.id_model == curr_id).update(
#             {
#                 'model_name': request.form.get('model_name'),
#             })
#         db.session.commit()
#     except Exception:
#         traceback.print_exc()
#         flash('Impossible to change')
#     return redirect(url_for('models'))