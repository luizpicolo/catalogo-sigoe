from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='views')

base_url = 'http://sistemas.na.ifms.edu.br'

paths = [
  ['/sigoe.na', 'Nova Andradina', '2697'],
  ['/sigoe.nv', 'Naviraí',        '2696'],
  ['/sigoe.pp', 'Ponta Porã',     '2693'],
  ['/sigoe.tl', 'Três Lagoas',    '2692'],
  ['/sigoe.aq', 'Aquidauana',     '2691'],
  ['/sigoe.cb', 'Corumbá',        '2690'],
  ['/sigoe.dr', 'Dourados',       '2689'],
  ['/sigoe.cx', 'Coxim',          '2688'],
  ['/sigoe.cg', 'Campo Grande',   '8888'],
  ['/sigoe.jd', 'Jardim',         '8888'],
]

@app.route('/')
def main():
    return render_template(
      'layout.html', 
      base_url=base_url, 
      paths=paths,
      date_now=date_now()
    )

def date_now():
    return datetime.utcnow().year

if __name__ == "__main__":
    app.run(reaload=True, debug=True)