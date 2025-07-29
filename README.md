# 🌤️ Weather Logger with GitHub Actions

[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-blue?logo=github-actions)](https://github.com/features/actions)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://python.org)
[![Weatherstack](https://img.shields.io/badge/API-Weatherstack-orange)](https://weatherstack.com/)

This project periodically fetches weather data for Berlin using the [Weatherstack API](https://weatherstack.com/) and logs the information to a file. The process is automated with GitHub Actions on a schedule.

## ✨ Features

- 🌍 Fetches current weather data from Weatherstack API
- 📝 Logs weather info with rotating file logs
- ⏰ Runs automatically on GitHub using scheduled workflows
- 🔄 Commits updated log files back to the repository
- 🔒 Secure API key management with GitHub Secrets

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A Weatherstack API key ([Get one here](https://weatherstack.com/))

### 📦 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/kvn05/GithubAction.git
   cd your-repo
   ```

2. **Create a `.env` file** (optional for local runs)
   
   Add your Weatherstack API key in `.env` (this file should be gitignored):
   ```env
   WEATHERSTACK_KEY=your_actual_weatherstack_api_key
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Running Locally

Make sure you have the environment variable set (`WEATHERSTACK_KEY`) either via `.env` using `python-dotenv` or by exporting it manually.

```bash
python main.py
```

## ⚙️ GitHub Actions Workflow

The automated workflow:
- 📅 Scheduled to run **twice weekly** (Monday and Thursday) at midnight UTC
- 🔄 Automatically fetches weather and updates logs
- 📤 Commits and pushes updated logs back to the `main` branch
- 🔐 Uses GitHub Secrets to keep API keys secure (`WEATHERSTACK_KEY`)

### 🔧 Setting up GitHub Secrets

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `WEATHERSTACK_KEY`
5. Value: Your Weatherstack API key
6. Click **Add secret**

## 📁 Project Structure

```
weather-logger/
├── .github/
│   └── workflows/
│       └── weather-logger.yml    # GitHub Actions workflow
├── main.py                       # Main weather fetching script
├── requirements.txt              # Python dependencies
├── status.log                    # Weather log file (auto-generated)
├── .env                         # Environment variables (local only)
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

## 📊 Sample Log Output

```
2024-01-15 12:00:01 - Berlin Weather: 5°C, Overcast, Humidity: 78%
2024-01-18 12:00:01 - Berlin Weather: -2°C, Snow, Humidity: 85%
2024-01-22 12:00:01 - Berlin Weather: 8°C, Partly Cloudy, Humidity: 65%
```

## ⚠️ Important Notes

- 📊 The free Weatherstack API plan limits to **100 requests per month**
- 🕐 Adjust the GitHub Actions schedule as needed to stay within the limit
- 📝 Logs are stored in `status.log` with rotation to avoid bloating
- 🌍 Currently configured for Berlin weather - modify `main.py` to change location

## 🔧 Customization

### Change Location
Edit the location parameter in `main.py`:
```python
# Change 'Berlin' to your desired city
response = requests.get(f"http://api.weatherstack.com/current?access_key={api_key}&query=Berlin")
```

### Modify Schedule
Edit `.github/workflows/weather-logger.yml`:
```yaml
schedule:
  - cron: '0 0 * * 1,4'  # Runs at midnight UTC on Monday and Thursday
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

## 📄 License

This project is for learning purposes and does not have a specific license.

---

**Happy Weather Logging!** 🌈

If you found this project helpful, please consider giving it a ⭐!
