from flask import Flask, request, jsonify
from ai_model import micro_invest, growth_score, saving_trigger, milestones

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    invest = micro_invest(data)
    score = growth_score(data)
    trigger = saving_trigger(data)
    badge = milestones(score)

    return jsonify({
        "micro_invest": invest,
        "growth_score": score,
        "saving_trigger": trigger,
        "milestone": badge
    })

if __name__ == '__main__':
    app.run(debug=True)