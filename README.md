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
│   └── graphs/             # Generated visualization images (23 graphs)
│       ├── Graph1.png      # Gender distribution pie chart
│       ├── Graph2.png      # Top 10 countries bar chart
│       ├── Graph3.png      # Continent-wise sunburst chart
│       ├── Graph4.png      # Age histogram
│       ├── Graph5.png      # Age distribution plot
│       ├── Graph7.png      # Nationality analysis
│       ├── Graph8.png      # Flight status overview
│       ├── Graph11.png     # Flight trends over time
│       ├── Graph_ymin6.png # Age trends visualization
│       ├── Graph_Quad9.png # Quadrant analysis
│       ├── bar_asia_pass14.png         # Asia passenger bar chart
│       ├── pie_asia_pass15.png         # Asia passenger pie chart
│       ├── bar_Europe_pass16.png       # Europe passenger bar chart
│       ├── pie_Europe_pass17.png       # Europe passenger pie chart
│       ├── bar_North_America_pass18.png    # North America bar chart
│       ├── pie_North_America_pass19.png    # North America pie chart
│       ├── bar_Oceania_pass20.png      # Oceania passenger bar chart
│       ├── bar_Africa_pass12.png       # Africa passenger bar chart
│       ├── pie_Africa_pass13.png       # Africa passenger pie chart
│       ├── bar_South_America_pass22.png    # South America bar chart
│       └── pie_South_America_pass25.png    # South America pie chart
└── frontend/
    ├── index.html          # Main dashboard page
    ├── style.css           # Dashboard styling
    ├── img/                # Image assets for frontend
    │   ├── Graph1.png through Graph11.png  # Core visualizations
    │   ├── Graph_ymin6.png & Graph_Quad9.png
    │   ├── bar_*.png       # Regional bar charts (6 files)
    │   ├── pie_*.png       # Regional pie charts (6 files)
    │   ├── dataset_img.png # Dataset preview image
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
~/Desktop/GitHub/SL_Project/Airline_Record_Analysis$ python3 backend/main.py
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