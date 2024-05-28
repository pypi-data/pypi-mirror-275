"""
whatnow package

This package contains modules and functions related to the whatnow project.
"""
from .what import get_weather_details, get_location, extract_city, get_current_datetime
__all__ = ["get_weather_details", "get_location", "extract_city", "get_current_datetime"]
