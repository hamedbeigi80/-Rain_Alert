#!/usr/bin/env python3
"""
Weather Alert System

A Python script that checks weather forecast and sends email alerts
when rain is expected in the next few hours.

Requirements:
- requests library for API calls
- smtplib for email notifications
- OpenWeatherMap API key
- Gmail app password for email authentication

Author: Hamed Ahmadbeigi
"""

import os
import sys
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WeatherAlert:
    def __init__(self):
        """Initialize the WeatherAlert with configuration from environment variables."""
        self.lat = float(os.getenv('WEATHER_LAT', '43.817070'))
        self.lon = float(os.getenv('WEATHER_LON', '125.323547'))
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.email_password = os.getenv('EMAIL_PASSWORD')
        self.from_email = os.getenv('FROM_EMAIL', 'your-email@gmail.com')
        self.to_email = os.getenv('TO_EMAIL', 'recipient@example.com')
        
        # Validate required environment variables
        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY environment variable is required")
        if not self.email_password:
            raise ValueError("EMAIL_PASSWORD environment variable is required")
    
    def get_weather_forecast(self, hours=4):
        """
        Fetch weather forecast from OpenWeatherMap API.
        
        Args:
            hours (int): Number of forecast periods to check
            
        Returns:
            dict: Weather data from API
            
        Raises:
            requests.RequestException: If API request fails
        """
        parameters = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": self.api_key,
            "cnt": hours,
        }
        
        try:
            logger.info(f"Fetching weather forecast for coordinates ({self.lat}, {self.lon})")
            response = requests.get(
                "https://api.openweathermap.org/data/2.5/forecast",
                params=parameters,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch weather data: {e}")
            raise
    
    def will_rain(self, weather_data):
        """
        Check if rain is expected based on weather condition codes.
        
        Weather condition codes < 700 typically indicate precipitation:
        - 2xx: Thunderstorm
        - 3xx: Drizzle  
        - 5xx: Rain
        - 6xx: Snow
        
        Args:
            weather_data (dict): Weather data from API
            
        Returns:
            bool: True if rain is expected, False otherwise
        """
        try:
            for hour_data in weather_data["list"]:
                condition_code = hour_data["weather"][0]["id"]
                if int(condition_code) < 700:
                    weather_desc = hour_data["weather"][0]["description"]
                    logger.info(f"Rain expected: {weather_desc} (code: {condition_code})")
                    return True
            
            logger.info("No rain expected in the forecast period")
            return False
        except (KeyError, IndexError, ValueError) as e:
            logger.error(f"Error parsing weather data: {e}")
            return False
    
    def send_rain_alert(self):
        """
        Send rain alert email notification.
        
        Raises:
            smtplib.SMTPException: If email sending fails
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = self.to_email
            msg['Subject'] = "☔ Rain Alert - Don't Forget Your Umbrella!"
            
            body = """
            Hello!
            
            The weather forecast indicates rain is expected in your area within the next few hours.
            
            Remember to bring an umbrella when you go out!
            
            Stay dry,
            Your Weather Alert System
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            logger.info("Sending rain alert email...")
            with smtplib.SMTP("smtp.gmail.com", port=587) as server:
                server.starttls()  # Enable encryption
                server.login(self.from_email, self.email_password)
                server.send_message(msg)
            
            logger.info(f"Rain alert sent successfully to {self.to_email}")
            
        except smtplib.SMTPException as e:
            logger.error(f"Failed to send email: {e}")
            raise
    
    def run(self):
        """
        Main method to check weather and send alert if necessary.
        
        Returns:
            bool: True if alert was sent, False otherwise
        """
        try:
            # Get weather forecast
            weather_data = self.get_weather_forecast()
            
            # Check if rain is expected
            if self.will_rain(weather_data):
                self.send_rain_alert()
                return True
            else:
                logger.info("No rain alert needed")
                return False
                
        except Exception as e:
            logger.error(f"Weather alert system error: {e}")
            return False

def main():
    """Main entry point for the script."""
    try:
        alert_system = WeatherAlert()
        alert_system.run()
    except Exception as e:
        logger.error(f"Failed to initialize weather alert system: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
