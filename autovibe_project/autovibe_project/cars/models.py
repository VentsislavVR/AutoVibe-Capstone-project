from django.core.validators import MinLengthValidator
# Create your views here.
from django.db import models

from autovibe_project.cars.validators import get_current_year_plus_one


class CarBrand(models.Model):
    MAX_BRAND_NAME_LENGTH = 100
    MIN_BRAND_NAME_LENGTH = 2

    MAX_COUNTRY_OF_ORIGIN_LENGTH = 100
    MIN_COUNTRY_OF_ORIGIN_LENGTH = 2

    brand_name = models.CharField(
        max_length=MAX_BRAND_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_BRAND_NAME_LENGTH),
        ],
    )

    country_of_origin = models.CharField(
        max_length=MAX_COUNTRY_OF_ORIGIN_LENGTH,
        validators=[
            MinLengthValidator(MIN_COUNTRY_OF_ORIGIN_LENGTH),
        ])

    logo = models.ImageField(
        upload_to='brand_logos/',
    )

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    MAX_MODEL_LENGTH = 100
    MIN_MODEL_LENGTH = 2

    MAX_COLOR_LENGTH = 50

    MAX_VIN_LENGTH = 17

    BGN_TO_EUR_CONVERSION_RATIO = 0.51129


    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=[
            MinLengthValidator(MIN_MODEL_LENGTH),
        ]
    )
    year = models.PositiveIntegerField(
        validators=[
            get_current_year_plus_one,
        ]
    )
    color = models.CharField(
        max_length=MAX_COLOR_LENGTH,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    mileage = models.PositiveIntegerField(
        validators=[

        ]
    )
    vin = models.CharField(
        max_length=MAX_VIN_LENGTH,
        unique=True,
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=500,
    )
    image = models.ImageField(upload_to='car_images/')



    def price_in_eur(self):
        # Convert the price from BGN to EUR using the fixed ratio
        price_bgn = self.price
        price_eur = price_bgn * self.BGN_TO_EUR_CONVERSION_RATIO
        return price_eur

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class CarFeature(models.Model):
    MAX_FEATURE_LENGTH = 100
    MIN_FEATURE_LENGTH = 2

    INTERIOR_FEATURES_CHOICES = [
        ('leather_seats', 'Leather Seats'),
        ('navigation_system', 'Navigation System'),
        ('heated_seats', 'Heated Seats'),
        ('sunroof', 'Sunroof'),
        ('power_windows', 'Power Windows'),
        ('power_seats', 'Power Seats'),
        ('memory_seats', 'Memory Seats'),
        ('climate_control', 'Climate Control'),
        ('premium_audio_system', 'Premium Audio System'),
        ('wireless_charging', 'Wireless Charging'),
        ('ambient_lighting', 'Ambient Lighting'),
        ('rear_entertainment_system', 'Rear Entertainment System'),

    ]

    EXTERIOR_FEATURES_CHOICES = [
        ('alloy_wheels', 'Alloy Wheels'),
        ('led_headlights', 'LED Headlights'),
        ('panoramic_roof', 'Panoramic Roof'),
        ('power_tailgate', 'Power Tailgate'),
        ('power_sliding_doors', 'Power Sliding Doors'),
        ('roof_rails', 'Roof Rails'),
        ('fog_lights', 'Fog Lights'),
        ('automatic_headlights', 'Automatic Headlights'),
        ('rain_sensing_wipers', 'Rain Sensing Wipers'),
        ('heated_mirrors', 'Heated Mirrors'),
        ('parking_sensors', 'Parking Sensors'),
        ('backup_camera', 'Backup Camera'),

    ]

    SAFETY_FEATURES_CHOICES = [
        ('abs', 'ABS'),
        ('airbags', 'Airbags'),
        ('lane_departure_warning', 'Lane Departure Warning'),
        ('automatic_emergency_braking', 'Automatic Emergency Braking'),
        ('blind_spot_monitoring', 'Blind Spot Monitoring'),
        ('adaptive_cruise_control', 'Adaptive Cruise Control'),
        ('forward_collision_warning', 'Forward Collision Warning'),
        ('rear_cross_traffic_alert', 'Rear Cross Traffic Alert'),
        ('parking_assist', 'Parking Assist'),
        ('tire_pressure_monitoring', 'Tire Pressure Monitoring'),
        ('driver_assist_package', 'Driver Assist Package'),
        ('night_vision_assist', 'Night Vision Assist'),

    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    interior_features = models.CharField(
        max_length=100,
        choices=INTERIOR_FEATURES_CHOICES,
        blank=True,
    )
    exterior_features = models.CharField(
        max_length=100,
        choices=EXTERIOR_FEATURES_CHOICES,
        blank=True
    )
    safety_features = models.CharField(
        max_length=100,
        choices=SAFETY_FEATURES_CHOICES,
        blank=True
    )
    other_features = models.TextField(
        max_length=500,
        blank=True
    )

    def __str__(self):
        return f"Features of {self.car}"
