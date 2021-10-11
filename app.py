
from extension.extension import Extensions



ext = Extensions.getInstance(r"C:\Users\asamir\OneDrive - Ciena Corporation\Desktop\pet shop\pet-shop-project\config\flask.cfg")
api = ext.add_end_points()
app = ext.get_app()


if __name__ == "__main__":
    app.run(debug=True)
