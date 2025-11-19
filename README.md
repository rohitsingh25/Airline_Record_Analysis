# Airline Data Analysis Dashboard

A comprehensive data analysis project for CS699 (Software Lab) under Prof. Bhaskaran Raman, focusing on airline passenger data visualization and insights.

## 📊 Project Overview

This project analyzes airline passenger data to provide insights into travel patterns, demographics, and operational efficiency. The system includes a Python-based backend for data processing and visualization generation, coupled with a web-based frontend dashboard for interactive data exploration.

## 🎯 Features

- **Comprehensive Data Analysis**: Analysis of 98,000+ passenger records
- **Interactive Visualizations**: 20+ different graphs and charts
- **Demographic Insights**: Gender, age, nationality, and geographic distribution analysis
- **Flight Performance Metrics**: On-time, delayed, and cancelled flight statistics
- **Web Dashboard**: User-friendly interface to explore all visualizations
- **Multi-continent Analysis**: Data breakdown by continents and countries

## 🛠️ Tech Stack

### Backend
- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Static plotting
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive visualizations

### Frontend
- **HTML5** - Structure and content
- **CSS3** - Styling and responsive design
- **JavaScript** - Interactive elements

## 📁 Project Structure

```
SL_Project/
├── README.md
├── requirements.txt         # Python dependencies
├── Backend/
│   ├── main.py              # Main data analysis script
│   └── Airline_Dataset.csv  # Raw dataset (98,621 records)
└── Frontend/
    ├── index.html           # Main dashboard page
    ├── style.css           # Styling
    ├── img/                # Image assets
    ├── Pages/              # Individual graph pages
    │   ├── Graph1.html     # Gender distribution
    │   ├── Graph2.html     # Top countries analysis
    │   ├── Graph3.html     # Continent-wise breakdown
    │   ├── Graph4.html     # Age histogram
    │   ├── Graph5.html     # Age distribution plot
    │   ├── Graph7.html     # Nationality analysis
    │   ├── Graph8.html     # Flight status overview
    │   ├── Graph11.html    # Flight trends over time
    │   ├── Graph13.html    # Average age trends
    │   └── ...             # Additional visualization pages
    └── Reports/
        └── Airline_Dataset.csv  # Dataset copy for reports
```

## 📈 Data Analysis Insights

The project generates various types of visualizations including:

1. **Demographic Analysis**
   - Gender distribution of passengers
   - Age distribution and trends
   - Nationality breakdown

2. **Geographic Analysis**
   - Top 10 countries by passenger volume
   - Continent-wise passenger distribution
   - Regional travel patterns

3. **Flight Operations**
   - Flight status analysis (On-time, Delayed, Cancelled)
   - Temporal trends in flight performance
   - Departure date patterns

4. **Regional Deep-dives**
   - Asia-specific passenger analysis
   - North America travel patterns
   - European market insights

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- All required packages are listed in `requirements.txt`

### Running the Analysis

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rohitsingh25/Software-Lab-Project.git
   cd Software-Lab-Project
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Create virtual environment
   python -m venv airline_env
   
   # Activate virtual environment
   # On Linux/Mac:
   source airline_env/bin/activate
   
   # On Windows:
   # airline_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend analysis**:
   ```bash
   cd Backend
   python main.py
   ```

5. **View the dashboard**:
   - Open `Frontend/index.html` in your web browser
   - Navigate through different sections to explore visualizations

6. **Deactivate virtual environment** (when done):
   ```bash
   deactivate
   ```

### Dataset Information

The airline dataset contains:
- **98,621 passenger records**
- **Passenger demographics**: ID, Name, Gender, Age, Nationality
- **Flight details**: Departure/Arrival airports, dates, pilot information
- **Geographic data**: Country codes, continents, airport locations
- **Operational data**: Flight status (On Time, Delayed, Cancelled)

## 🔍 Key Findings

- Analysis covers passengers from multiple continents with diverse demographics
- Flight performance metrics reveal operational efficiency patterns
- Temporal analysis shows seasonal and periodic travel trends
- Geographic distribution highlights major travel corridors

## 👥 Contributors

- **Rohit Singh** - [LinkedIn](https://in.linkedin.com/in/rohit1225/)
- **Bharat Patidar** - [LinkedIn](https://in.linkedin.com/in/bharat-patidar-a74a8b1b0)

## 📧 Contact

For questions or collaboration opportunities, please reach out through our LinkedIn profiles or create an issue in this repository.

## 📄 License

This project is part of academic coursework for CS699 (Software Lab) and is intended for educational purposes..

---

*CS699 Software Lab Project | IIT Bombay*