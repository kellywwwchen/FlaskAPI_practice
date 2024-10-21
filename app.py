from flask import Flask
from flasgger import Swagger
from views.user_view import bp as user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
swagger = Swagger(app, template_file="swagger.yml")

if __name__ == "__main__":
    app.run(debug=True)
