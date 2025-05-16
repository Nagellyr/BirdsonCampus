from flask import Flask, render_template, request, redirect, url_for
from data import birds
from data import get_all_birds, get_bird_by_id, get_popular_birds, get_quiz_questions
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html", birds=get_all_birds(), popular=get_popular_birds())

@app.route("/view/<id>")
def view(id):
    bird = get_bird_by_id(id)
    popular_birds = get_popular_birds()
    return render_template("view.html", bird=bird, popular_birds=popular_birds)

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = get_quiz_questions()
    feedback = {}
    score = 0

    if request.method == "POST":
        for q in questions:
            if q.get("type") == "drag-match":
                correct_map = q.get("correct_map", {})
                all_correct = True

                for key, correct_value in correct_map.items():
                    submitted = request.form.get(f"{q['name']}_{key}")
                    if submitted != correct_value:
                        all_correct = False

                if all_correct:
                    feedback[q["name"]] = " All matches correct!"
                    score += 1
                else:
                    feedback[q["name"]] = "Some matches were incorrect."

            else:
                user_answer = request.form.get(q["name"])
                correct = q.get("answer") or q.get("correct")

                if user_answer == correct:
                    feedback[q["name"]] = "Correct!"
                    score += 1
                elif not user_answer:
                    feedback[q["name"]] = "No answer selected"
                else:
                    feedback[q["name"]] = f"Incorrect. Please Try again!"

        if score == len(questions):
            return render_template("perfectscore.html", birds=get_all_birds().values())

    return render_template("quiz.html", questions=questions, feedback=feedback, score=score)

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return render_template('data_search.html', query="", results=[], empty_search=True)

    pattern = re.compile(re.escape(query), re.IGNORECASE)

    def highlight(text):
        return pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", text)

    results = []
    for bird in birds.values():
        match_title = pattern.search(bird['title'])
        match_summary = pattern.search(bird['summary'])
        match_traits = any(pattern.search(trait) for trait in bird['identifying_traits'])
        match_location = any(pattern.search(loc) for loc in bird.get('locations', []))

        if match_title or match_traits or match_location:
            bird_copy = bird.copy()
            bird_copy['highlight_title'] = highlight(bird['title'])
            bird_copy['highlight_summary'] = highlight(bird['summary'])
            bird_copy['highlight_locations'] = [highlight(loc) for loc in bird['locations']]
            results.append(bird_copy)

    return render_template('data_search.html', query=query, results=results, empty_search=False)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/edit/<id>')
def edit(id):
    bird = birds.get(id)
    if not bird:
        return "Bird not found", 404
    return render_template('edit.html', bird=bird)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    required_fields = ['title', 'summary', 'identifying_traits', 'locations', 'image', 'wingspan_cm']
    for field in required_fields:
        if not data.get(field) or (isinstance(data[field], str) and not data[field].strip()):
            return {"error": f"{field} is required"}, 400

    try:
        wingspan = int(data['wingspan_cm'])
    except ValueError:
        return {"error": "Wingspan must be a number"}, 400

    if 'id' not in data or not data['id'].strip():
        existing_ids = sorted(int(i) for i in birds.keys() if i.isdigit())
        next_id = str(existing_ids[-1] + 1 if existing_ids else 1)
        data['id'] = next_id

    bird_id = data['id']
    birds[bird_id] = {
        "id": bird_id,
        "title": data['title'],
        "summary": data['summary'],
        "identifying_traits": [s.strip() for s in data['identifying_traits'].split(',')],
        "locations": [s.strip() for s in data['locations'].split(',')],
        "image": data['image'],
        "wingspan_cm": wingspan
    }

    return {"success": True, "id": bird_id}

if __name__ == '__main__':
    app.run(debug=True, port=5001)
