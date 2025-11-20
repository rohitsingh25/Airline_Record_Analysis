# Airline Data Analysis Dashboard

A comprehensive data analysis project for CS699 (Software Lab) under Prof. Bhaskaran Raman, focusing on airline passenger data visualization and insights.

## 📊 Project Overview

This project analyzes airline passenger data to provide insights into travel patterns, demographics, and operational efficiency. The system includes a Python-based backend for data processing and visualization generation, coupled with a web-based frontend dashboard for interactive data exploration.

## 🎯 Features

- **Comprehensive Data Analysis**: Analysis of 98,621 passenger records
- **Interactive Visualizations**: 23 different graphs and charts
- **Demographic Insights**: Gender, age, nationality, and geographic distribution analysis
- **Flight Performance Metrics**: On-time, delayed, and cancelled flight statistics
- **Web Dashboard**: User-friendly interface with 23 interactive visualization pages
- **Multi-continent Analysis**: Dedicated visualizations for each continent (Asia, Europe, North America, South America, Africa, Oceania)
- **Export Capabilities**: All graphs generated as PNG images and compiled in PDF format

## 🛠️ Tech Stack

### Backend
- **Python 3.x**
- **Pandas** (≥1.3.0) - Data manipulation and analysis
- **NumPy** (≥1.21.0) - Numerical computing
- **Matplotlib** (≥3.4.0) - Static plotting
- **Seaborn** (≥0.11.0) - Statistical data visualization
- **Plotly** (≥5.0.0) - Interactive visualizations
- **Kaleido** (≥0.2.1) - Static image export for Plotly
- **PyYAML** (≥6.0) - Configuration file parsing

### Frontend
- **HTML5** - Structure and content
- **CSS3** - Styling and responsive design
- **JavaScript** - Interactive elements

## 📁 Project Structure

```
Airline_Record_Analysis/
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
├── config.yaml             # Configuration file for paths and settings
├── venv/                   # Python virtual environment
├── backend/
│   ├── main.py             # Main data analysis script (319 lines)
│   ├── data/
│   │   └── Airline_Dataset.csv  # Raw dataset (98,621 records)
│   └── graphs/             # Generated visualization images (21 graphs)
│       ├── gender_distribution_pie.png           # Gender distribution
│       ├── top_countries_passengers_bar.png      # Top countries by passengers
│       ├── continent_country_sunburst.png        # Continent hierarchy
│       ├── age_distribution_histogram.png        # Age histogram
│       ├── age_count_distribution_bar.png        # Age count distribution
│       ├── nationality_distribution_pie.png      # Nationality analysis
│       ├── flight_status_distribution_pie.png    # Flight status overview
│       ├── flight_status_trends_line.png         # Flight trends over time
│       ├── average_age_trends_line.png           # Age trends over time
│       ├── asia_passengers_bar.png               # Asia passenger bar chart
│       ├── asia_passengers_pie.png               # Asia passenger pie chart
│       ├── europe_passengers_bar.png             # Europe passenger bar chart
│       ├── europe_passengers_pie.png             # Europe passenger pie chart
│       ├── north_america_passengers_bar.png      # North America bar chart
│       ├── north_america_passengers_pie.png      # North America pie chart
│       ├── oceania_passengers_bar.png            # Oceania passenger bar chart
│       ├── oceania_passengers_pie.png            # Oceania passenger pie chart
│       ├── africa_passengers_bar.png             # Africa passenger bar chart
│       ├── africa_passengers_pie.png             # Africa passenger pie chart
│       ├── south_america_passengers_bar.png      # South America bar chart
│       └── south_america_passengers_pie.png      # South America pie chart
└── frontend/
    ├── index.html          # Main dashboard page
    ├── style.css           # Dashboard styling
    ├── img/                # Generated graph visualizations (copied from backend/graphs)
    │   ├── gender_distribution_pie.png           # Gender distribution
    │   ├── top_countries_passengers_bar.png      # Top countries
    │   ├── continent_country_sunburst.png        # Continent hierarchy
    │   ├── age_distribution_histogram.png        # Age histogram
    │   ├── age_count_distribution_bar.png        # Age count
    │   ├── nationality_distribution_pie.png      # Nationality
    │   ├── flight_status_distribution_pie.png    # Flight status
    │   ├── flight_status_trends_line.png         # Flight trends
    │   ├── average_age_trends_line.png           # Age trends
    │   └── (Regional bar & pie charts for 6 continents)
    ├── static/             # Static assets for UI
    │   ├── dataset_img.png # Dataset preview icon
    │   └── pdf_img.png     # PDF report icon
    ├── pages/              # Individual graph pages (23 HTML files)
    │   ├── Graph1.html through Graph23.html
    │   └── Each page displays a specific visualization
    └── reports/            # Project deliverables
        ├── Airline_Dataset.csv      # Dataset copy
        ├── Generated_Graphs.pdf     # Compiled visualizations
        ├── project-proposal.pdf     # Project proposal document
        ├── project-update.pdf       # Project update document
        └── 23m0761_23m0773.tar.xz  # Compressed project archive
```

## 📈 Data Analysis Insights

The project generates 23 comprehensive visualizations including:

1. **Demographic Analysis**
   - Gender distribution of passengers (pie chart)
   - Age distribution histogram and trends
   - Nationality breakdown

2. **Geographic Analysis**
   - Top 10 countries by passenger volume (bar chart)
   - Continent-wise passenger distribution (sunburst chart)
   - Regional travel patterns across 6 continents

3. **Flight Operations**
   - Flight status analysis (On-time, Delayed, Cancelled)
   - Temporal trends in flight performance
   - Departure date patterns

4. **Regional Deep-dives**
   - **Asia**: Passenger analysis with bar and pie charts
   - **Europe**: Travel patterns visualization
   - **North America**: Market insights
   - **South America**: Passenger distribution
   - **Africa**: Regional breakdown
   - **Oceania**: Travel statistics

5. **Advanced Analytics**
   - Quadrant analysis for multi-dimensional insights
   - Age trends with minimum threshold filtering
   - Hierarchical data representation

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- All required packages are listed in `requirements.txt`

### Configuration

The project uses a `config.yaml` file to manage all file paths and analysis settings. This centralized configuration makes it easy to modify input/output locations and analysis parameters without changing the code.

**Important**: All paths in `config.yaml` are relative to the project root directory. Always run the scripts from the project root:
```bash
Airline_Record_Analysis$ python3 backend/main.py
```

**Key Configuration Sections:**

- **Input Configuration**: Dataset path and date parsing settings
- **Output Configuration**: Directory for generated graphs and individual graph filenames
- **Figure Settings**: DPI and figure sizes for visualizations
- **Analysis Settings**: Parameters like top N countries, nationalities, and age bins

To modify paths or settings, edit the `config.yaml` file in the project root:

```yaml
input:
  dataset_path: "backend/data/Airline_Dataset.csv"
  parse_dates: ["Departure Date"]

output:
  graphs_dir: "backend/graphs"
  graphs:
    gender_distribution: "Graph1.png"
    # ... other graph names

figure_settings:
  dpi: 300
  large_figure_size: [14, 8]
  xlarge_figure_size: [18, 10]

analysis:
  top_n_countries: 10
  top_n_nationalities: 20
  age_bins: 20
```

### Running the Analysis

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rohitsingh25/Airline_Record_Analysis.git
   cd Airline_Record_Analysis
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   # On Linux/Mac:
   source venv/bin/activate
   
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend analysis** (from project root):
   ```bash
   python3 backend/main.py
   ```
   This will:
   - Read the dataset from `backend/data/Airline_Dataset.csv`
   - Generate all 23 visualizations
   - Save graphs to the `backend/graphs/` directory as PNG files

5. **View the dashboard**:
   - Open `frontend/index.html` in your web browser directly, or
   - From project root, run:
     ```bash
     # On Linux/Mac:
     xdg-open frontend/index.html
     
     # On Mac:
     open frontend/index.html
     
     # On Windows:
     start frontend/index.html
     ```
   - Navigate through 23 different visualization pages (Graph1.html through Graph23.html)
   - Explore continent-specific analyses and demographic insights
   - Access project reports from the `frontend/reports/` directory

6. **Deactivate virtual environment** (when done):
   ```bash
   deactivate
   ```

### Dataset Information

The airline dataset (`Airline_Dataset.csv`) contains:
- **98,621 passenger records**
- **Passenger demographics**: ID, Name, Gender, Age, Nationality
- **Flight details**: Departure/Arrival airports, dates, pilot information
- **Geographic data**: Country codes, continents, airport locations
- **Operational data**: Flight status (On Time, Delayed, Cancelled)

Available in two locations:
- `backend/data/Airline_Dataset.csv` - Source data for analysis
- `frontend/reports/Airline_Dataset.csv` - Reference copy for reporting

## 📊 Project Deliverables

The `frontend/reports/` directory contains:
- **Generated_Graphs.pdf** - Compilation of all 23 visualizations
- **project-proposal.pdf** - Initial project proposal document
- **project-update.pdf** - Project progress update
- **23m0761_23m0773.tar.xz** - Complete project archive

## 🔍 Key Findings

- Analysis covers 98,621 passengers from 6 continents with diverse demographics
- 23 comprehensive visualizations covering demographic, geographic, and operational aspects
- Flight performance metrics reveal operational efficiency patterns
- Temporal analysis shows seasonal and periodic travel trends
- Geographic distribution highlights major travel corridors
- Continent-specific insights for Asia, Europe, North America, South America, Africa, and Oceania
- Interactive web dashboard with individual pages for each visualization

## 👥 Contributors

- **Rohit Singh** - [LinkedIn](https://in.linkedin.com/in/rohit1225/)
- **Bharat Patidar** - [LinkedIn](https://in.linkedin.com/in/bharat-patidar-a74a8b1b0)

## 📧 Contact

For questions or collaboration opportunities, please reach out through our LinkedIn profiles or create an issue in this repository.

## 📄 License

This project is part of academic coursework for CS699 (Software Lab) and is intended for educational purposes..

---

*CS699 Software Lab Project | IIT Bombay*