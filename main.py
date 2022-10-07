from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='views')

paths = [
  ['https://sigoe.na.ifms.edu.br', 'Sistema de Ocorrências', '443'],
]

@app.route('/')
def main():
    return render_template(
      'layout.html', 
      paths=paths,
      date_now=date_now()
    )

def date_now():
    return datetime.utcnow().year

if __name__ == "__main__":
    app.run(reaload=True, debug=True)