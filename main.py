from app_connector import create_myApp

#creating a flask app
app = create_myApp()

if(__name__ == "__main__"):
    app.run(port = 5000)

