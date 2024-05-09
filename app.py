from flask import Flask, request, jsonify
from analizador_lexico import lexer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods= ['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text')
    lexer.input(text)
    result = []
    line_number = 1
    while True:
        tok = lexer.token()
        if not tok:
            break
        result.append(f"LINEA {line_number}\n\n<{tok.type}>    {tok.value}\n")
        line_number += 1
    return "\n".join(result)

if __name__ == '__main__':
    app.run(debug=True)