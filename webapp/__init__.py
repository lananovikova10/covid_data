from flask import Flask, render_template


from webapp.covid_data import cases_by_country

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    @app.route('/')
    def display():
        cases = cases_by_country(app.config["CASES_DEFAULT_COUNTRY"])
        return render_template('index.html', cases=cases)
    return app

#if __name__=="__main__":
#    app.run()    

#app.run(debug=True)
