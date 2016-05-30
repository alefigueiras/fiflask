from flask import Flask, render_template, request, redirect
from first_module import quandl, plot
from bokeh.resources import INLINE
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show():
    symbol = request.args['ticker'].upper()

    history = quandl(symbol)
    
    figure = plot(history,title='Market history of ' + symbol)
    
    script,div = components(figure)
    
    return render_template('show.html',
                           js_resources=INLINE.render_js(),
                           css_resources=INLINE.render_css(),
                           script=script,
                           div=div)


if __name__ == '__main__':
    app.debug = True
    app.run(port=33507)
