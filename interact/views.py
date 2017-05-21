from interact import app
from flask import request, make_response, jsonify
from .models import User, db

app.config.from_object('config')


@app.errorhandler(404)
def not_found(self):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/addnewuser', methods=['POST'])
def newuser():
    if not request.json \
            or not 'name' in request.json \
            or not 'linkedin_url' in request.json \
            or not 'title' in request.json \
            or not 'access_token' in request.json \
            or not 'image_url' in request.json:
        return jsonify({'error': 'wtf'}), 400
    else:
        user = User(request.json['name'],
                    request.json['linkedin_url'],
                    request.json['color'],
                    request.json['phone_number'],
                    request.json['title'],
                    request.json['image_url'],
                    request.json['access_token'])
        db.session.add(user)
        db.session.commit()

    return jsonify({'id': user.id}), 201


@app.route('/getuserinfo/<int:user_id>', methods=['GET'])
def listusers(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        return jsonify({'name': user.name,
                        'title': user.title,
                        'linkedin_url': user.linkedin_url,
                        'access_token': user.access_token,
                        'image_url': user.image_url,
                        'color': user.color,
                        'phone_number': user.phone_number,
                        }), 200
    else:
        return jsonify({'error': 'wtf'}), 404


@app.route('/', methods=['GET'])
def selamlar():
    return jsonify({'selam': 'canım'}), 200

#test purpose only
@app.route('/addfriend', methods=['GET'])
def addfriend():
    user = User.query.filter_by(id=2).first()
    user2 = User.query.filter_by(id=3).first()
    user.children.append(user2)
    db.session.add(user)
    db.session.commit()
    return jsonify({'error': 'none'}), 200
