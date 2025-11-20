"""
Airline Data Analysis and Visualization

This module processes airline passenger data and generates comprehensive visualizations
including demographic analysis, geographic distribution, and flight performance metrics.

Usage:
    python backend/main.py (run from project root)

Author: Rohit Singh Yadav, Bharat Patidar
Course: CS699 Software Lab, IIT Bombay
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import yaml
import shutil
import warnings
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image

# Suppress FutureWarnings for cleaner output
warnings.filterwarnings('ignore', category=FutureWarning)

# Print startup banner
print("="*80)
print("  AIRLINE DATA ANALYSIS & VISUALIZATION SYSTEM")
print("  CS699 Software Lab | IIT Bombay")
print("="*80)

# Load configuration from YAML file
print("\n[1/5] Loading configuration...")
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(project_root, 'config.yaml')
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)
print("✓ Configuration loaded successfully")

# Extract configuration values and resolve paths from project root
DATASET_PATH = os.path.join(project_root, config['input']['dataset_path'])
GRAPHS_DIR = os.path.join(project_root, config['output']['graphs_dir'])
IMG_DIR = os.path.join(project_root, 'frontend', 'img')
REPORTS_DIR = os.path.join(project_root, 'frontend', 'reports')
GRAPH_NAMES = config['output']['graphs']
DPI = config['figure_settings']['dpi']
LARGE_FIG_SIZE = tuple(config['figure_settings']['large_figure_size'])
XLARGE_FIG_SIZE = tuple(config['figure_settings']['xlarge_figure_size'])
TOP_N_COUNTRIES = config['analysis']['top_n_countries']
TOP_N_NATIONALITIES = config['analysis']['top_n_nationalities']
AGE_BINS = config['analysis']['age_bins']

# Ensure graphs and img directories exist
# GRAPHS_DIR: stores all generated visualizations
# IMG_DIR: frontend copy of graphs for web dashboard
os.makedirs(GRAPHS_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)
print(f"✓ Output directories configured")
print(f"  - Graphs: {config['output']['graphs_dir']}")
print(f"  - Frontend: frontend/img")

# ============================================================================
# DATA LOADING AND PREPROCESSING
# ============================================================================

print("\n[2/5] Loading and preprocessing dataset...")
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
print(f"✓ Loaded {len(df):,} passenger records")
df.head(11)
df.info()
df.nunique()
df.isnull().sum().sum()

# Data type conversions
df['Gender'] = df['Gender'].astype('category')
df['Gender'].unique()
df['Age'] = df['Age'].astype(int)
print("✓ Data preprocessing completed")

# ============================================================================
# DEMOGRAPHIC ANALYSIS
# ============================================================================

print("\n[3/5] Generating demographic visualizations...")

# Graph 1: Gender distribution pie chart
print("  → Creating gender distribution chart...")
count_1 = df['Gender'].value_counts()
fig = px.pie(count_1, values=count_1.values, names=count_1.index, 
             title="Distribution of passengers accross Genders")
fig.write_image(os.path.join(GRAPHS_DIR, GRAPH_NAMES['gender_distribution']))

# ============================================================================
# GEOGRAPHIC ANALYSIS
# ============================================================================

print("  → Creating geographic distribution charts...")

# Graph 2: Top countries bar chart
count_2 = df['Country Name'].value_counts()
fig = px.bar(count_2.head(TOP_N_COUNTRIES), 
             x=count_2.head(TOP_N_COUNTRIES).index, 
             y=count_2.head(TOP_N_COUNTRIES).values, 
             title='Top 10 Airport Countries with Most Passengers',
             labels={'x': 'Country', 'y': 'Passenger Count'})
fig.write_image(os.path.join(GRAPHS_DIR, GRAPH_NAMES['top_countries_bar']))

# Graph 3: Continent-wise hierarchical sunburst chart
df_c = pd.DataFrame(count_2).reset_index().rename(columns={"index": "value", 0: "count"})
con = df.loc[:, ['Country Name', 'Continents']]
con = con.drop_duplicates()
new_df = pd.merge_ordered(df_c, con, fill_method='ffill', on='Country Name')

fig = px.sunburst(new_df, path=['Continents', 'Country Name'], values='count',
                  color='count', 
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(new_df['count'], weights=new_df['count']),
                  title="Airport Country and Continent wise Passengers")
fig.write_image(os.path.join(GRAPHS_DIR, GRAPH_NAMES['continent_sunburst']))

# Graph 4: Age distribution histogram
print("  → Creating age distribution visualizations...")
fig = px.histogram(df, x='Age', nbins=20, color='Gender',
                   title='Histogram of Passengers Age',
                   labels={'Age': 'Passengers Age'})
fig.write_image(os.path.join(GRAPHS_DIR, GRAPH_NAMES['age_histogram']))

# Graph 5: Age count distribution
plt.figure(figsize=XLARGE_FIG_SIZE)
sns.countplot(data=df, x='Age')
plt.xticks(rotation=90)
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['age_count_bar']), bbox_inches='tight')

# Graph 7: Nationality distribution
print("  → Creating nationality distribution chart...")
nationality = pd.DataFrame(df['Nationality'].value_counts()).reset_index()
nationality = nationality.head(TOP_N_NATIONALITIES)
nationality.sort_values(by='Nationality', ascending=False, inplace=True)
fig = px.pie(nationality, values='count', names='Nationality', hole=0.5, 
             title='Distribution Accross Nationality')
fig.write_image(os.path.join(GRAPHS_DIR, GRAPH_NAMES['nationality_pie']))

# ============================================================================
# FLIGHT OPERATIONS ANALYSIS
# ============================================================================

print("\n[4/5] Generating flight operations visualizations...")

# Graph 8: Flight status distribution
print("  → Creating flight status charts...")
fl_stat = pd.DataFrame(df['Flight Status'].value_counts()).reset_index()
fig = px.pie(fl_stat, values='count', names='Flight Status', 
             color_discrete_sequence=px.colors.sequential.RdBu)
fig.write_image(os.path.join(GRAPHS_DIR, GRAPH_NAMES['flight_status_pie']))

# Graph 11: Flight trends over time
print("  → Creating temporal trend analyses...")
df['Departure Date'] = pd.to_datetime(df['Departure Date'])
plt.figure(figsize=LARGE_FIG_SIZE)
flight_data = df.groupby(['Departure Date', 'Flight Status']).size().reset_index(name='Count')
sns.lineplot(x='Departure Date', y='Count', hue='Flight Status', 
             data=flight_data, palette='Set2')
plt.title('Flight Status based on Departure Date')
plt.xlabel('Departure Date')
plt.ylabel('Count of Flights')
plt.legend(title='Flight Status')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['flight_trends_line']), bbox_inches='tight')

# Graph 13: Average age trends over time
average_age = df.groupby('Departure Date')['Age'].mean().reset_index()
plt.figure(figsize=(14, 8))
sns.lineplot(x='Departure Date', y='Age', data=average_age, marker='o', color='blue')
plt.title('Average Age Over Time')
plt.xlabel('Departure Date')
plt.ylabel('Average Age')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['age_trends_line']), bbox_inches='tight')

# ============================================================================
# REGIONAL ANALYSIS - ASIA
# ============================================================================

print("\n[5/5] Generating regional analysis charts...")
print("  → Asia region...")

# Bar graph: Asian countries passenger distributionribution
continent = 'Asia'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.barh([i for i, j in data], [j for i, j in data])
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['asia_bar']), dpi=DPI)

# Pie chart: Asian countries passenger distribution
continent = 'Asia'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.pie([j for i, j in data], labels=[i for i, j in data], autopct='%1.1f%%')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['asia_pie']), dpi=DPI)

# ============================================================================
# REGIONAL ANALYSIS - NORTH AMERICA
# ============================================================================

print("  → North America region...")

# Bar graph: North American countries passenger distributionribution
continent = 'North America'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.barh([i for i, j in data], [j for i, j in data])
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['north_america_bar']), dpi=DPI)

# Pie chart: North American countries passenger distribution
continent = 'North America'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.pie([j for i, j in data], labels=[i for i, j in data], autopct='%1.1f%%')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['north_america_pie']), dpi=DPI)

# ============================================================================
# REGIONAL ANALYSIS - EUROPE
# ============================================================================

print("  → Europe region...")

# Bar graph: European countries passenger distributionribution
continent = 'Europe'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.barh([i for i, j in data], [j for i, j in data])
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['europe_bar']), dpi=DPI)

# Pie chart: European countries passenger distribution
continent = 'Europe'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.pie([j for i, j in data], labels=[i for i, j in data], autopct='%1.1f%%')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['europe_pie']), dpi=DPI)

# ============================================================================
# REGIONAL ANALYSIS - SOUTH AMERICA
# ============================================================================

print("  → South America region...")

# Bar graph: South American countries passenger distributionribution
continent = 'South America'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.barh([i for i, j in data], [j for i, j in data])
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['south_america_bar']), dpi=DPI)

# Pie chart: South American countries passenger distribution
continent = 'South America'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.pie([j for i, j in data], labels=[i for i, j in data], autopct='%1.1f%%')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['south_america_pie']), dpi=DPI)

# ============================================================================
# REGIONAL ANALYSIS - OCEANIA
# ============================================================================

print("  → Oceania region...")

# Bar graph: Oceania countries passenger distributionribution
continent = 'Oceania'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.barh([i for i, j in data], [j for i, j in data])
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['oceania_bar']), dpi=DPI)

# Pie chart: Oceania countries passenger distribution
continent = 'Oceania'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.pie([j for i, j in data], labels=[i for i, j in data], autopct='%1.1f%%')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['oceania_pie']), dpi=DPI)

# ============================================================================
# REGIONAL ANALYSIS - AFRICA
# ============================================================================

print("  → Africa region...")

# Bar graph: African countries passenger distributionribution
continent = 'Africa'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.barh([i for i, j in data], [j for i, j in data])
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['africa_bar']), dpi=DPI)

# Pie chart: African countries passenger distribution
continent = 'Africa'
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])
df_continent = df[df['Continents'] == continent]

x = list(set(list(df_continent['Country Name'])))
y = [len(list(df_continent[df_continent['Country Name'] == c]['Passenger ID'])) for c in x]
data = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[1])[-10:]

plt.pie([j for i, j in data], labels=[i for i, j in data], autopct='%1.1f%%')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['africa_pie']), dpi=DPI)

# ============================================================================
# ADDITIONAL VISUALIZATIONS
# ============================================================================

# Reload data for additional analysis
df = pd.read_csv(DATASET_PATH, parse_dates=config['input']['parse_dates'])

# Age histogram (duplicate check)
fig = px.histogram(df, x='Age', nbins=AGE_BINS, color='Gender',
                   title='Histogram of Passengers Age',
                   labels={'Age': 'Passengers Age'})
fig.write_image(os.path.join(GRAPHS_DIR, GRAPH_NAMES['age_histogram']))

# Flight trends over time (duplicate check)
flight_data = df.groupby(['Departure Date', 'Flight Status']).size().reset_index(name='Count')
sns.lineplot(x='Departure Date', y='Count', hue='Flight Status', 
             data=flight_data, palette='Set2')
plt.title('Count of Flights Over Time Based on Flight Status')
plt.xlabel('Departure Date')
plt.ylabel('Count of Flights')
plt.legend(title='Flight Status')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['flight_trends_line']), bbox_inches='tight')

# Age trends over time (duplicate check)
average_age = df.groupby('Departure Date')['Age'].mean().reset_index()
plt.figure(figsize=LARGE_FIG_SIZE)
sns.lineplot(x='Departure Date', y='Age', data=average_age, marker='o', color='blue')
plt.title('Average Age Over Time')
plt.xlabel('Departure Date')
plt.ylabel('Average Age')
plt.savefig(os.path.join(GRAPHS_DIR, GRAPH_NAMES['age_trends_line']), bbox_inches='tight')

# ============================================================================
# FILE EXPORT - Copy graphs to frontend
# ============================================================================

print("\nCopying visualizations to frontend...")
copied_count = 0
for file in os.listdir(GRAPHS_DIR):
    if file.lower().endswith((".png", ".jpg", ".jpeg", ".svg")):
        src = os.path.join(GRAPHS_DIR, file)
        dst = os.path.join(IMG_DIR, file)
        try:
            shutil.copy(src, dst)
            copied_count += 1
        except Exception as e:
            print(f"  ✗ Failed to copy {file}: {e}")

print(f"✓ Copied {copied_count} files to frontend/img")

# ============================================================================
# PDF GENERATION - Merge all graphs into a single PDF
# ============================================================================

print("\nGenerating PDF compilation of all visualizations...")
pdf_path = os.path.join(REPORTS_DIR, 'generated-graphs.pdf')

# Get all PNG files from graphs directory in sorted order
graph_files = sorted([f for f in os.listdir(GRAPHS_DIR) if f.lower().endswith('.png')])

if graph_files:
    try:
        with PdfPages(pdf_path) as pdf:
            for graph_file in graph_files:
                graph_path = os.path.join(GRAPHS_DIR, graph_file)
                
                # Read image using PIL to get dimensions
                img = Image.open(graph_path)
                width, height = img.size
                
                # Create figure with appropriate size (convert pixels to inches at 100 DPI for display)
                fig = plt.figure(figsize=(width/100, height/100))
                ax = fig.add_subplot(111)
                ax.imshow(img)
                ax.axis('off')
                
                # Remove margins
                plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
                
                # Save to PDF
                pdf.savefig(fig, bbox_inches='tight', pad_inches=0)
                plt.close(fig)
        
        print(f"✓ PDF created successfully: frontend/reports/generated-graphs.pdf")
        print(f"  Included {len(graph_files)} visualizations")
    except Exception as e:
        print(f"✗ Failed to create PDF: {e}")
else:
    print("✗ No graph files found to compile into PDF")

print("\n" + "="*80)
print(f"  ANALYSIS COMPLETE!")
print(f"  Generated {len(os.listdir(GRAPHS_DIR))} visualizations")
print(f"  Graphs saved to: {config['output']['graphs_dir']}")
print(f"  Frontend copy: frontend/img")
print(f"  PDF report: frontend/reports/generated-graphs.pdf")
print("="*80)
print("\nYou can now open frontend/index.html to view the dashboard.\n")
