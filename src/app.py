from flask import Flask, jsonify, render_template
import os
from dbio.dbutils import DbUtils
from admin import McqExamCenterServices

def create_app():
    ''' Description: Create and return Flask app object.
        Provide sqlite db configuration to start db when app is up.
        SECRET_KEY is for data safety and used by Flask
    '''
    app = Flask(__name__, instance_relative_config=True)

    #Define config mapping- where to look for configuration file
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE= os.path.join(app.instance_path, 'MCQCenter.sqlite'),
        TEMPFILE= app.instance_path,
    )

    #load configurations from file
    app.config.from_pyfile('config.py', silent=True)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/health")
    def health():
        return jsonify(
            srarus="Up"
        )

    @app.route("/")
    def welcomePage():
        return render_template("index.html")
    
    #Register db with app and init
    DbUtils.init_app(app)

    #Register blueprint with app
    app.register_blueprint(McqExamCenterServices.bp)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

    return app