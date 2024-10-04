__version__ = "0.0.1"
import biketrauma

df = biketrauma.Load_db().save_as_df()
biketrauma.plot_location(biketrauma.get_accident(df))
from .io.Load_db import Load_db
from .vis.plot_location import plot_location
from .preprocess.get_accident import get_accident
