from typing import List

import altair
import pyRserve
from altair import Chart

from altair_easeviz.templates import r_code_bar_chart, r_code_pie_chart, r_code_scatter_plot, \
    r_code_line_chart


def get_theme_names(current_theme: str, size_axis):
    themes = {"categorical": f"tableu10", "sequential": f"hcl.colors({size_axis}, 'Blues')"}

    if (current_theme == "accessible_theme"):
        themes['sequential'] = f"hcl.colors({size_axis}, 'Blues')"
        themes['categorical'] = f"RColorBrewer::brewer.pal({size_axis}, Dark2)"

    if (current_theme == "dark_accessible_theme"):
        themes['sequential'] = f"hcl.colors({size_axis}, 'Blues')"
        themes['categorical'] = f"RColorBrewer::brewer.pal({size_axis}, Paired)"
    if (current_theme == "filler_pattern_theme"):
        themes['sequential'] = f"hcl.colors({size_axis}, 'Blues')"
        themes['categorical'] = f"RColorBrewer::brewer.pal({size_axis}, set1)"

    if (current_theme == "print_theme"):
        themes['sequential'] = "Blues"
        themes['categorical'] = f"RColorBrewer::brewer.pal({size_axis}, set3)"
    return themes


def generate_description(chart: Chart, type_chart: str, axis_x: List, axis_y: List):
    """
        This function will generate a descripcion of a given chart and return a dict with all the parameters.
    It will return a dict with the error in case of fail

    :param axis_y:
    :param axis_x:
    :param chart: A Chart Altair object
    :param type_chart: "bar", "scatter", "line"
    :return: Dict with a description of the Chart
    """

    response = {"error": "The function did not work or even try to connect to R"}
    type_chart = type_chart.lower()
    chart_dict = chart.to_dict()
    chart_title = chart_dict['title'] if "title" in chart_dict else "Accesible Chart"
    x_axis_title = "X axis"
    y_axis_title = "Y axis"

    if 'x' in chart_dict['encoding']:
        x_axis_title = chart_dict['encoding']['field'] if "field" in chart_dict['encoding'] else x_axis_title
    if 'y' in chart_dict['encoding']:
        y_axis_title = chart_dict['encoding']['field'] if "field" in chart_dict['encoding'] else y_axis_title

    try:
        conn = pyRserve.connect()
    except Exception as e:
        response = {"error": e}
        print(f"Error executing R code: {e}")

    # Stablish connection with pyRserve
    try:
        conn.r(
            'tableu10 <- c("#4c78a8", "#f58518", "#e45756", "#72b7b2", "#54a24b", "#eeca3b", "#b279a2", "#ff9da6", "#9d755d", "#bab0ac")')

        # Set Up R theme with thematic package
        current_theme_altair = altair.themes.active
        theme = get_theme_names(current_theme_altair, len(axis_x))

        r_code_theme = f"""
        library(thematic)
        thematic_on(bg = "#222222", fg = "white", accent = "white",qualitative ={theme['categorical']}, sequential={theme['categorical']})
        """
        conn.eval(r_code_theme)

        # Execute chart in R
        if (type_chart == "barchart"):
            r_code = r_code_bar_chart(axis_x, axis_y, chart_title, x_axis_title, y_axis_title)
            response = {"res": conn.eval(r_code)}
        if (type_chart == "scatterplot"):
            r_code = r_code_scatter_plot(axis_x, axis_y, chart_title,x_axis_title, y_axis_title)
            response = {"res": conn.eval(r_code)}

        if (type_chart == "piechart"):
            r_code = r_code_pie_chart(axis_x, axis_y, chart_title)
            response = {"res": conn.eval(r_code)}

        if (type_chart == "linechart"):
            r_code = r_code_line_chart(axis_x, axis_y, chart_title, x_axis_title, y_axis_title)
            response = {"res": conn.eval(r_code)}

        # Reformat response
        if 'res' in response:
            response['res'] = '\n'.join(response['res'])
        # Close connection
        conn.close()
    # Return results
    except Exception as e:
        response = {"error": e.__str__()}
        print(f"Error executing R code: {e}")
    finally:
        # Cierra la conexión
        return response
