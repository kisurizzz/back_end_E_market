from app import app
from models import Category, Commodity, db



with app.app_context():
        # Drop all tables and create them again (use with caution in production)
        db.drop_all()
        db.create_all()

        # Add categories
        categories = [
            Category(name="Electronics"),
            Category(name="Books"),
            Category(name="Clothing"),
            Category(name="Home & Kitchen"),
        ]
        db.session.bulk_save_objects(categories)
        db.session.commit()

        # Add commodities
        commodities = [
            Commodity(name="Laptop", description="A high-performance laptop", price=999.99, stock=10, category_id=1, commodity_image='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.microsoft.com%2Fen-us%2Fd%2Fsurface-laptop-5-for-business%2F8wx8rsm6l09n&psig=AOvVaw0JRmfB6wlTs7MSoVfBoMOz&ust=1721233707048000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCMD2o7T9q4cDFQAAAAAdAAAAABAE'),

            Commodity(name="Smartphone", description="A latest model smartphone", price=699.99, stock=20, category_id=1, commodity_image='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.samsung.com%2Fuk%2Fsmartphones%2F&psig=AOvVaw1Tx3d4Tw_hNOzoo6Io0lfk&ust=1721233824799000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCKDp7O39q4cDFQAAAAAdAAAAABAJ'),

            Commodity(name="Novel", description="A bestselling novel", price=19.99, stock=50, category_id=2, commodity_image='https://www.google.com/url?sa=i&url=https%3A%2F%2Fkathmandupost.com%2Fbooks%2F2022%2F12%2F21%2Fnot-your-usual-romance-novel&psig=AOvVaw19CB5P0BrVOUB3PDcxljoT&ust=1721233929394000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCJjMtZr-q4cDFQAAAAAdAAAAABAE'),

            Commodity(name="T-Shirt", description="A comfortable cotton t-shirt", price=9.99, stock=100, category_id=3, commodity_image='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.sonofatailor.com%2Fproduct%2Fcotton-t-shirt%2F1-1-3-9-12&psig=AOvVaw0Jf1zxtRJSzE8-UxG8odq6&ust=1721233961566000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCMiu4Kn-q4cDFQAAAAAdAAAAABAE'),

            Commodity(name="Blender", description="A powerful kitchen blender", price=49.99, stock=15, category_id=4, commodity_image='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ariete.net%2Fen%2Fproduct%2FAriete-blender-moderna-black-585&psig=AOvVaw0BhtGm5PolvN5ooPLFw7BL&ust=1721233984902000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCLDhhLX-q4cDFQAAAAAdAAAAABAE'),
        ]
        db.session.bulk_save_objects(commodities)
        db.session.commit()

        print("Database seeded!")


