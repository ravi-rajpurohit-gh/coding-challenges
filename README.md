# Geo-Shift Analysis of Monsoon Depression Events

This project analyzes and visualizes the geographical movement of monsoon depressions across India during the monsoon season. Using data from the ERA5 dataset, this project provides both interactive and static visualizations to showcase how depression events shift geographically.

## Interactive Plot

You can explore the interactive visualization of the monsoon depression events by running the plot_interactive.html file. This interactive plot allows for dynamic exploration of the depression paths over time, providing insights into their geographical shifts.

## Conclusion

In this project, I worked with **data cleaning**, **data transformation**, and **data visualization** to analyze monsoon depression shifts. Two primary methodologies were employed:
1. **Interactive visualization** with **Plotly** for dynamic, real-time exploration.
2. **Static geospatial plotting** with **GeoPandas** and **Matplotlib** for a detailed static analysis.

The analysis revealed that monsoon depressions typically originate near the Bay of Bengal and track westward and northward across the subcontinent, as seen in both interactive and static plots. These insights are valuable for understanding how these depressions evolve over time and their potential impacts on different regions.


## Directory Structure

Here is the project’s directory structure:

```
├── ERA5_LPS_JJAS_Depression.csv   # Data file containing the depression data
├── Header.dat                     # File containing header information for the data file
├── india_map_files/                # Directory containing shapefiles for plotting with GeoPandas
│   ├── india-polygon.shp
│   ├── india-polygon.shx
│   ├── india-polygon.dbf
│   ├── india-polygon.cpg
│   └── india-polygon.prj
├── plot_1.png                     # Static image of the Plotly visualization
├── plot_2.png                     # Static image of the Geopandas map loaded visualization
├── plot_interactive.html          # Interactive Plotly plot exported to HTML
├── plot_graph.ipynb                # Jupyter notebook containing the project code and visualizations
└── README.md                      # Project README file
```


## Features

- **Interactive Geo-Plot**: A dynamic plot using Plotly to visualize the movement of depression events on a map.
- **Static Geo-Plot**: A static visualization using GeoPandas that shows depression paths overlaid on a map of India.

## How to Run the Project

1. Install the required libraries using `pip install -r requirements.txt`.
2. Ensure the dataset (`ERA5_LPS_JJAS_Depression.csv`) and header file (`Header.dat`) are in the same directory as the notebook.
3. Make sure the shapefiles are in the `india_map_files/` directory.
4. Run the Jupyter notebook `plot_graph.ipynb` to generate the visualizations.
5. You can view the static and interactive plots in the files `plot_1.png` and `plot_interactive.html`, respectively.

## Results

The project highlights the geographical shift of monsoon depression events during 2018 and 2019. The interactive and static plots provide insights into how these events travel across different regions of India during the monsoon season.

## Libraries Used

- **Pandas**: For data processing
- **Numpy**: For numerical computations
- **Plotly**: For interactive visualization
- **GeoPandas**: For geospatial data analysis
- **Matplotlib & Seaborn**: For static plots
- **Shapely**: To handle geometric shapes and lines

## Contact

For any questions or feedback, feel free to contact me @
#### ravirajpurohit414@gmail.com
