# Weather Alert System ☔

A Python-based weather monitoring system that automatically checks weather forecasts and sends email alerts when rain is expected in your area.

## Features

- 🌦️ **Real-time Weather Monitoring**: Uses OpenWeatherMap API to check upcoming weather conditions
- 📧 **Email Notifications**: Sends alerts via Gmail when rain is expected
- 🔒 **Secure Configuration**: Uses environment variables for sensitive data
- 📝 **Comprehensive Logging**: Detailed logs for monitoring and debugging
- ⚡ **Error Handling**: Robust error handling for network issues and API failures
- 🎛️ **Configurable**: Easy to customize location, email settings, and forecast period

## Prerequisites

Before running this application, make sure you have:

- Python 3.6 or higher
- A Gmail account with 2-factor authentication enabled
- An OpenWeatherMap API key (free tier available)
- Gmail App Password (not your regular Gmail password)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/weather-alert-system.git
   cd weather-alert-system
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your actual values:
   ```env
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   EMAIL_PASSWORD=your_gmail_app_password_here
   FROM_EMAIL=your-email@gmail.com
   TO_EMAIL=recipient@example.com
   WEATHER_LAT=43.817070
   WEATHER_LON=125.323547
   ```

## Setup Instructions

### 1. Get OpenWeatherMap API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to "My API Keys"
4. Copy your API key

### 2. Set up Gmail App Password

1. Enable 2-factor authentication on your Gmail account
2. Go to [Google Account Settings](https://myaccount.google.com/)
3. Navigate to "Security" → "2-Step Verification" → "App passwords"
4. Generate a new app password for "Mail"
5. Use this 16-character password (not your regular Gmail password)

### 3. Find Your Coordinates

You can find your latitude and longitude using:
- [LatLong.net](https://www.latlong.net/)
- Google Maps (right-click on your location)
- GPS coordinates from your phone

## Usage

### Basic Usage

Run the script once to check current weather:
```bash
python weather_alert.py
```

### Automated Monitoring

Set up a cron job to run the script automatically:

```bash
# Edit your crontab
crontab -e

# Add this line to check weather every hour
0 * * * * cd /path/to/weather-alert-system && python weather_alert.py

# Or check every 30 minutes during daytime (6 AM to 8 PM)
*/30 6-20 * * * cd /path/to/weather-alert-system && python weather_alert.py
```

### Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., every hour)
4. Set action to start your Python script

## Configuration Options

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENWEATHER_API_KEY` | Your OpenWeatherMap API key | - | ✅ |
| `EMAIL_PASSWORD` | Gmail app password | - | ✅ |
| `FROM_EMAIL` | Sender email address | your-email@gmail.com | ❌ |
| `TO_EMAIL` | Recipient email address | recipient@example.com | ❌ |
| `WEATHER_LAT` | Latitude of your location | 43.817070 | ❌ |
| `WEATHER_LON` | Longitude of your location | 125.323547 | ❌ |

### Customizing Rain Detection

The script considers these weather condition codes as "rain":
- **2xx**: Thunderstorm
- **3xx**: Drizzle
- **5xx**: Rain
- **6xx**: Snow

You can modify the rain detection logic in the `will_rain()` method.

## Logging

The application generates detailed logs including:
- Weather API requests and responses
- Email sending status
- Error messages and debugging information

Logs are printed to console with timestamps and severity levels:
```
2024-06-14 10:30:15,123 - INFO - Fetching weather forecast for coordinates (43.8, 125.3)
2024-06-14 10:30:16,456 - INFO - Rain expected: light rain (code: 500)
2024-06-14 10:30:18,789 - INFO - Rain alert sent successfully to user@example.com
```

## Troubleshooting

### Common Issues

**"Authentication failed" email error:**
- Make sure you're using an App Password, not your regular Gmail password
- Verify 2-factor authentication is enabled on your Gmail account

**"Invalid API key" error:**
- Check that your OpenWeatherMap API key is correct
- New API keys may take a few minutes to become active

**"Failed to fetch weather data":**
- Check your internet connection
- Verify your latitude and longitude are correct
- Ensure OpenWeatherMap service is operational

**No email received:**
- Check spam/junk folder
- Verify the recipient email address is correct
- Check Gmail's "Sent" folder to confirm the email was sent

### Enable Debug Logging

For more detailed debugging information, modify the logging level:

```python
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## File Structure

```
weather-alert-system/
├── weather_alert.py      # Main application script
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .env                 # Your actual environment variables (not in git)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing weather data API
- Python community for excellent libraries and documentation


---

**Stay dry!** 🌂
