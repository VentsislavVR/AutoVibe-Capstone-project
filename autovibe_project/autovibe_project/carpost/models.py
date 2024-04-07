from datetime import datetime

from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
UserModel = get_user_model()
from multiselectfield import MultiSelectField as MSField
class MultiSelectField(MSField):
    """
    Custom Implementation of MultiSelectField to achieve Django 5.0 compatibility

    See: https://github.com/goinnn/django-multiselectfield/issues/141#issuecomment-1911731471
    """

    def _get_flatchoices(self):
        flat_choices = super(models.CharField, self).flatchoices

        class MSFFlatchoices(list):
            # Used to trick django.contrib.admin.utils.display_for_field into not treating the list of values as a
            # dictionary key (which errors out)
            # Todo celebrate a small victory
            def __bool__(self):
                return False

            __nonzero__ = __bool__

        return MSFFlatchoices(flat_choices)

    flatchoices = property(_get_flatchoices)



# class Logo(models.Model):
#     image = models.ImageField(upload_to='logos/')


# Todo maybe use for blog articles which
class CarBrands(models.Model):
    BRAND_CHOICES = [
        ('ACURA', 'ACURA'),
        ('ALFA ROMEO', 'ALFA ROMEO'),
        ('ASTON MARTIN', 'ASTON MARTIN'),
        ('AUDI', 'AUDI'),
        ('BENTLEY', 'BENTLEY'),
        ('BMW', 'BMW'),
        ('BUICK', 'BUICK'),
        ('CADILLAC', 'CADILLAC'),
        ('CHEVROLET', 'CHEVROLET'),
        ('CHRYSLER', 'CHRYSLER'),
        ('DODGE', 'DODGE'),
        ('FERRARI', 'FERRARI'),
        ('FIAT', 'FIAT'),
        ('FORD', 'FORD'),
        ('GENESIS', 'GENESIS'),
        ('GMC', 'GMC'),
        ('HONDA', 'HONDA'),
        ('HYUNDAI', 'HYUNDAI'),
        ('INFINITI', 'INFINITI'),
        ('JAGUAR', 'JAGUAR'),
        ('JEEP', 'JEEP'),
        ('KIA', 'KIA'),
        ('LAMBORGHINI', 'LAMBORGHINI'),
        ('LAND ROVER', 'LAND ROVER'),
        ('LEXUS', 'LEXUS'),
        ('LINCOLN', 'LINCOLN'),
        ('LOTUS', 'LOTUS'),
        ('MASERATI', 'MASERATI'),
        ('MAZDA', 'MAZDA'),
        ('MCLAREN', 'MCLAREN'),
        ('MERCEDES-BENZ', 'MERCEDES-BENZ'),
        ('MINI', 'MINI'),
        ('MITSUBISHI', 'MITSUBISHI'),
        ('NISSAN', 'NISSAN'),
        ('PAGANI', 'PAGANI'),
        ('PORSCHE', 'PORSCHE'),
        ('RAM', 'RAM'),
        ('ROLLS-ROYCE', 'ROLLS-ROYCE'),
        ('SMART', 'SMART'),
        ('SUBARU', 'SUBARU'),
        ('TESLA', 'TESLA'),
        ('TOYOTA', 'TOYOTA'),
        ('VOLKSWAGEN', 'VOLKSWAGEN'),
        ('VOLVO', 'VOLVO'),
    ]

    brand_name = models.CharField(
        max_length=100,
        choices=BRAND_CHOICES,
        unique=True
    )


    def __str__(self):
        return self.brand_name


class CarModel(models.Model):
    TEN_POPULAR_MODELS_PER_BRAND = {
        'ACURA':
            ['MDX', 'RDX', 'TLX', 'ILX', 'RLX', 'NSX', 'CL', 'RSX', 'TSX', 'ZDX'],
        'ALFA ROMEO':
            ['Giulia', 'Stelvio', '4C', 'Giulietta', 'Spider', 'Brera', '159', 'GT', '6C', '8C'],
        'ASTON MARTIN':
            ['DB11', 'Vantage', 'DBS', 'Rapide', 'Vanquish', 'DB9', 'DBX', 'Virage', 'Lagonda', 'Valkyrie'],
        'AUDI':
            ['A3', 'A4', 'A6', 'A8', 'Q3', 'Q5', 'Q7', 'Q8', 'TT', 'R8'],
        'BENTLEY':
            ['Continental GT', 'Bentayga', 'Flying Spur', 'Mulsanne', 'Arnage', 'Azure', 'Brooklands', 'Turbo R',
                    'Bentley 3 Litre', 'Mark VI'],
        'BMW':
            ['3 Series', '5 Series', '7 Series', 'X3', 'X5', 'X7', 'M3', 'M5', 'i3', 'i8'],
        'BUICK':
            ['Enclave', 'Encore', 'Envision', 'Regal', 'LaCrosse', 'Century', 'Riviera', 'Verano', 'Roadmaster',
                  'Park Avenue'],
        'CADILLAC':
            ['Escalade', 'CTS', 'XT5', 'XTS', 'ATS', 'CT6', 'SRX', 'XT4', 'XT6', 'Eldorado'],
        'CHEVROLET':
            ['Silverado', 'Equinox', 'Malibu', 'Camaro', 'Tahoe', 'Traverse', 'Cruze', 'Impala', 'Colorado',
                      'Suburban'],
        'CHRYSLER':
            ['300', 'Pacifica', 'Voyager', 'Sebring', 'Aspen', 'Crossfire', 'Concorde', 'PT Cruiser', 'LHS',
                     'New Yorker'],
        'DODGE':
            ['Charger', 'Challenger', 'Durango', 'Journey', 'Grand Caravan', 'Dart', 'Avenger', 'Caliber', 'Nitro',
                  'Magnum'],
        'FERRARI':
            ['488', 'F8 Tributo', '812 Superfast', 'SF90 Stradale', 'Portofino', 'GTC4Lusso', 'Roma',
                    'Monza SP1', 'Monza SP2', 'LaFerrari'],
        'FIAT':
            ['500', '500X', '500L', '124 Spider', 'Punto', 'Bravo', 'Tipo', 'Doblo', 'Freemont', 'Croma'],
        'FORD':
            ['F-150', 'Escape', 'Explorer', 'Focus', 'Fusion', 'Mustang', 'Edge', 'Expedition', 'Taurus', 'Ranger'],
        'GENESIS':
            ['G70', 'G80', 'G90', 'GV80', 'Essentia', 'Mint', 'GV70', 'Mira', 'NY', 'X Concept'],
        'GMC':
            ['Sierra', 'Yukon', 'Terrain', 'Acadia', 'Canyon', 'Savana', 'Envoy', 'Vandura', 'Jimmy', 'Syclone'],
        'HONDA':
            ['Civic', 'Accord', 'CR-V', 'Pilot', 'Odyssey', 'Fit', 'HR-V', 'Ridgeline', 'Insight', 'Clarity'],
        'HYUNDAI':
            ['Elantra', 'Sonata', 'Tucson', 'Santa Fe', 'Kona', 'Palisade', 'Accent', 'Veloster', 'Ioniq',
                    'Genesis'],
        'INFINITI':
            ['Q50', 'Q60', 'Q70', 'QX50', 'QX60', 'QX80', 'QX30', 'G35', 'G37', 'Q45'],
        'JAGUAR':
            ['F-PACE', 'XE', 'XF', 'XJ', 'E-PACE', 'I-PACE', 'F-TYPE', 'S-TYPE', 'XK', 'XK8'],
        'JEEP':
            ['Wrangler', 'Cherokee', 'Grand Cherokee', 'Compass', 'Renegade', 'Gladiator', 'Commander', 'Liberty',
                 'Patriot', 'CJ-7'],
        'KIA':
            ['Sorento', 'Sportage', 'Soul', 'Forte', 'Optima', 'Rio', 'Cadenza', 'Stinger', 'Telluride', 'K900'],
        'LAMBORGHINI':
            ['Aventador', 'Huracan', 'Urus', 'Gallardo', 'Murcielago', 'Diablo', 'Countach', 'Miura',
                        'Espada', 'Jarama'],
        'LAND ROVER':
            ['Range Rover', 'Range Rover Sport', 'Range Rover Evoque', 'Discovery', 'Discovery Sport',
                       'Defender', 'Freelander', 'Series I', ], }
    brand = models.CharField(
        max_length=100,
        default='Pick a brand',
    )
    model = models.CharField(
        max_length=100,
        default='Pick a model',
    )


    def __str__(self):
        return f"{self.brand} {self.model} - {self.pk}"


class CarPost(models.Model):
    MUNICIPALITY_CHOICES = [
        ('Blagoevgrad', 'Blagoevgrad'),
        ('Burgas', 'Burgas'),
        ('Varna', 'Varna'),
        ('Veliko Tarnovo', 'Veliko Tarnovo'),
        ('Vidin', 'Vidin'),
        ('Vratsa', 'Vratsa'),
        ('Gabrovo', 'Gabrovo'),
        ('Dobrich', 'Dobrich'),
        ('Kardzhali', 'Kardzhali'),
        ('Kyustendil', 'Kyustendil'),
        ('Lovech', 'Lovech'),
        ('Montana', 'Montana'),
        ('Pazardzhik', 'Pazardzhik'),
        ('Pernik', 'Pernik'),
        ('Pleven', 'Pleven'),
        ('Plovdiv', 'Plovdiv'),
        ('Razgrad', 'Razgrad'),
        ('Ruse', 'Ruse'),
        ('Shumen', 'Shumen'),
        ('Silistra', 'Silistra'),
        ('Sliven', 'Sliven'),
        ('Smolyan', 'Smolyan'),
        ('Sofia', 'Sofia'),
        ('Stara Zagora', 'Stara Zagora'),
        ('Targovishte', 'Targovishte'),
        ('Haskovo', 'Haskovo'),
        ('Yambol', 'Yambol'),
    ]

    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Silver', 'Silver'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Purple', 'Purple'),
        ('Pink', 'Pink'),
    ]

    ENGINE_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    TRANSMISSION_CHOICES = [
        ('Auto', 'Automatic'),
        ('Manual', 'Manual'),
    ]

    DRIVE_TRAIN_CHOICES = [
        ('2WD', '2WD'),
        ('4WD', '4WD'),
        ('AWD', 'AWD'),
    ]


    MAX_BRAND_NAME_LENGTH = 100
    MIN_BRAND_NAME_LENGTH = 2

    MAX_COUNTRY_OF_ORIGIN_LENGTH = 100
    MIN_COUNTRY_OF_ORIGIN_LENGTH = 2

    MAX_MODEL_LENGTH = 100
    MIN_MODEL_LENGTH = 2

    MAX_COLOR_LENGTH = 50

    MAX_VIN_LENGTH = 17

    MIN_YEAR_VALUE = 1900


    municipality = models.CharField(
        max_length=MAX_COUNTRY_OF_ORIGIN_LENGTH,
        choices=MUNICIPALITY_CHOICES,
        validators=[
            MinLengthValidator(MIN_COUNTRY_OF_ORIGIN_LENGTH),
        ]
    )

    year = models.PositiveIntegerField(
        validators=[MinValueValidator(MIN_YEAR_VALUE),
                    MaxValueValidator(datetime.now().year + 1)]
    )

    color = models.CharField(
        max_length=MAX_COLOR_LENGTH,
        choices=COLOR_CHOICES,
    )
    engine = models.CharField(
        max_length=20,
        choices=ENGINE_CHOICES,
    )
    # You need to define max_length
    horsepower = models.CharField(
        max_length=5,
    )
    # You need to define max_length
    transmission = models.CharField(
        max_length=100,
        choices=TRANSMISSION_CHOICES,
    )
    #Todo chage to drive train
    drive_train = models.CharField(

        max_length=100,
        choices=DRIVE_TRAIN_CHOICES,
    )  # You need to define max_length

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    mileage = models.PositiveIntegerField()

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

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,

    )
    car_feature = models.ManyToManyField(
        'CarFeatures',
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.car_model.brand} {self.car_model.model} - {self.id}"


class CarFeatures(models.Model):
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

    interior_features = MultiSelectField(
        max_length=1000,
        choices=INTERIOR_FEATURES_CHOICES,
        blank=True,
    )
    exterior_features = MultiSelectField(
        max_length=1000,
        choices=EXTERIOR_FEATURES_CHOICES,
        blank=True
    )
    safety_features = MultiSelectField(
        max_length=1000,
        choices=SAFETY_FEATURES_CHOICES,
        blank=True
    )
    other_features = models.TextField(
        max_length=500,
        blank=True
    )

    # def __str__(self):
    #     return f"{self.interior_features.flatchoices} {self.exterior_features.flatchoices} {self.safety_features}"
    #