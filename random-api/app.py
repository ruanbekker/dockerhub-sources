from random import choice, randint
from flask import Flask, request, jsonify

names = ['john', 'james', 'frank', 'adam', 'paul', 'jason', 'nick', 'ryan']
surnames = ['smith', 'adams', 'stevens', 'mcgreggor', 'adamson', 'phillips']
countries = ['south africa', 'ireland', 'new zealand', 'australia', 'america', 'england', 'mexico', 'canada', 'sweden', 'italy']
jobs = ['doctor', 'it', 'nurse', 'police officer', 'lawyer', 'teacher', 'entrepreneur', 'freelancer', 'musician', 'carpenter']
hobbies_lists = [['sport', 'music', 'nature'], ['ice hockey', 'programming', 'mountain biking'], ['running', 'food', 'social'], ['learning', 'youtube', 'sleeping'], ['food', 'nature', 'sport']]

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify({"message": "hello"}), 200

@app.route('/people')
def people():
    data = {
        "name": choice(names),
        "surname": choice(surnames),
        "country": choice(countries),
        "age": randint(21,38),
        "job": choice(jobs),
        "experience_in_years": randint(1,30),
        "hobbies": choice(hobbies_lists)
    }

    return jsonify(data)

@app.route('/people/list')
def peoplelist():
    datalist = []
    for x in range(3):
        
        data = {
            "name": choice(names),
            "surname": choice(surnames),
            "country": choice(countries),
            "age": randint(21,38),
            "job": choice(jobs),
            "experience_in_years": randint(1,30),
            "hobbies": choice(hobbies_lists)
        }
        datalist.append(data)

    return jsonify(datalist)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
