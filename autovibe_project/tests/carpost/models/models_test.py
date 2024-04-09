from django.contrib.auth import get_user_model
from django.test import TestCase
from datetime import datetime
from autovibe_project.carpost.models import CarBrands, CarModel, CarPost, CarFeatures

UserModel = get_user_model()

class CarModelsTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email='test@example.com', password='password')

    def test_car_brands_creation(self):
        brand = CarBrands.objects.create(brand_name='Toyota')
        self.assertEqual(brand.brand_name, 'Toyota')

    def test_car_model_creation(self):
        brand = CarBrands.objects.create(brand_name='Toyota')
        model = CarModel.objects.create(brand=brand, model='Camry')
        self.assertEqual(model.brand, brand)
        self.assertEqual(model.model, 'Camry')

    def test_car_post_creation(self):
        brand = CarBrands.objects.create(brand_name='Toyota')
        model = CarModel.objects.create(brand=brand, model='Camry')
        car_post = CarPost.objects.create(
            municipality='Sofia',
            year=datetime.now().year,
            color='Red',
            engine='Petrol',
            horsepower='150',
            transmission='Manual',
            drive_train='2WD',
            price=25000,
            mileage=10000,
            vin='ABC1234567890DEF',
            description='Test car',
            image='path/to/image.jpg',
            user=self.user,
            car_model=model
        )
        self.assertEqual(car_post.municipality, 'Sofia')
        self.assertEqual(car_post.year, datetime.now().year)
        self.assertEqual(car_post.color, 'Red')
        self.assertEqual(car_post.engine, 'Petrol')
        self.assertEqual(car_post.horsepower, '150')
        self.assertEqual(car_post.transmission, 'Manual')
        self.assertEqual(car_post.drive_train, '2WD')
        self.assertEqual(car_post.price, 25000)
        self.assertEqual(car_post.mileage, 10000)
        self.assertEqual(car_post.vin, 'ABC1234567890DEF')
        self.assertEqual(car_post.description, 'Test car')
        self.assertEqual(car_post.user, self.user)
        self.assertEqual(car_post.car_model, model)

    def test_car_features_creation(self):
        features = CarFeatures.objects.create(
            interior_features=['leather_seats', 'navigation_system'],
            exterior_features=['alloy_wheels', 'led_headlights'],
            safety_features=['abs', 'airbags'],
            other_features='Test features'
        )
        self.assertListEqual(features.interior_features, ['leather_seats', 'navigation_system'])
        self.assertListEqual(features.exterior_features, ['alloy_wheels', 'led_headlights'])
        self.assertListEqual(features.safety_features, ['abs', 'airbags'])
        self.assertEqual(features.other_features, 'Test features')
