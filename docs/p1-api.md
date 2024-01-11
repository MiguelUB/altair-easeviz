# Api

Within this page, you will discover comprehensive specifications and intricacies regarding the models utilized and
the functions created. It is advisable, however, to reference the "[Getting Started]" and "[Examples]" sections for a
more
streamlined comprehension of the library. These sections provide practical insights and usage scenarios that can
significantly enhance your understanding of the library's functionality and facilitate a smoother initiation process.

## Models

| Model         | Description                                                                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [ModelTheme]  | This models contains a Config model, some basic variables of color and functions to change the theme.                                |
| [ConfigModel] | A model with the main purpose is to hold and create a dict to hold all vega-lite specification, uses other models to be constructed. |
| [AxisModel]   | Model that contains some of the parameters of the 'axis' in  vega-lite specification                                                 |
| [HeaderModel] | Model that contains some of the parameters of the 'header' in  vega-lite specification                                               |
| [LegendModel] | Model that contains some of the parameters of the 'legend' in  vega-lite specification                                               |
| [MarkModel]   | Model that contains some of the parameters of the 'axis' in  vega-lite specification                                                 |
| [RangeModel]  | Model that contains 'category','diverging', 'heatmap' and 'ramp' parameters of the 'range' in  vega-lite specification               |
| [TitleModel]  | Model that contains some of the parameters of the 'title' in  vega-lite specification                                                |
| [ViewModel]   | Model that contains some of the parameters of the 'view' in  vega-lite specification                                                 |

### ModelTheme

`class altair_easeviz.models.ModelTheme(name_theme: str, text_color: str, axis_color: str, mark_color:
str,background_color: str, grid: bool)`

This model helps to create easy new themes for Altair, it is with this model that we create the 4 themes we included.

**Parameters:**

**name_theme** : str

The name that be registered in the altair.themes

**text_color** : str, HexColor,
Literal['red', 'yellow', [ColorName](https://altair-viz.github.io/user_guide/generated/core/altair.ColorName.html#altair.ColorName)]

Define the color of all the text of the chart included the mark Text

**axis_color**:  str, HexColor,
Literal['red', 'yellow', [ColorName](https://altair-viz.github.io/user_guide/generated/core/altair.ColorName.html#altair.ColorName)]

Define the color of the grid, axis and mark Lines of the chart

**mark_color**: str, HexColor,
Literal['red', 'yellow', [ColorName](https://altair-viz.github.io/user_guide/generated/core/altair.ColorName.html#altair.ColorName)]

Define the color of all marks in the chart

**background_color**:str, HexColor,
Literal['red', 'yellow', [ColorName](https://altair-viz.github.io/user_guide/generated/core/altair.ColorName.html#altair.ColorName)]

Define the color of the background of the chart

**grid**: bool

Define if the chart will show its grid or not

**colors**: Colors, dict

A dict that holds all the colors used in the model
arc,axis,background,text,mark,scheme{categorical,diverging,sequential}

**font_size**: dict

Holds the three sizes we use in the graph, is used to give a hierarchy order size to the text

**spacing**: dict

Holds the three sizes we use in the graph for spacing

**config**: dict

Creates a ConfigModel and holds dict with all the configurations described below following the vega-lite specification

**axis_config**: Axis, dict

Create and holds dict of type Axis describe it in types

**header_config**: Header, dict

Create and hold dict of type Header describe it in types

**legend_config**: Legend, dict

Create and holds dict of type Legend describe it in types

**title_config**: Title, dict

Create and hold dict of type Title describe it in types

**view_config**: View, dict

Create and hold dict of type View describe it in types

**range_config**: ScaleRange, dict

Create and hold dict of type ScaleRange describe it in types

**arc_config**: Mark, dict

Create and holds dict of type Mark describe it in types

**bar_config**: Mark, dict

Create and hold dict of type Mark describe it in types

**line_config**: Mark, dict

Create and hold dict of type Mark describe it in types

**path_config**: Mark, dict

Create and hold dict of type Mark describe it in types

**point_config**: Mark, dict

Create and hold dict of type Mark describe it in types

**rect_config**: Mark, dict

Create and hold dict of type Mark describe it in types

**rule_config**: Mark, dict

Create and hold dict of type Mark describe it in types

**shape_config**: Mark, dict

Create and hold dict of type Mark describe it in types

**text_config**: Mark, dict

Create and hold dict of type Mark describe it in types

**Functions:**

| Function                                    | Description                                                                                                               |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| get_theme()                                 | It returns a dict with all the config like the parameter config in the vega-lite specification                            |
| get_name()                                  | Return the name of the theme                                                                                              |
| change_background_color()                   | Change the background color and re register the theme in altair with the same name_theme                                  |
| change_mark_color()                         | Change the mark color and re register the theme in altair with the same name_theme                                        |
| change_text_color()                         | Change the text color and re register the theme in altair with the same name_theme                                        |
| increase_font_size(number:int)              | Increases all values in font_size by the number given  and re register the theme in altair with the same name_theme       |
| decrease_font_size(number:int)              | Decreases all values in font_size by the number given  and re register the theme in altair with the same name_theme       |
| change_categorical_scheme(scheme:List[str]) | Replaces the list in colors['categorical'] by the given scheme  and re register the theme in altair                       |
| change_sequential_scheme(scheme:List[str])  | Replaces the list in colors['sequential'] by the given scheme  and re register the theme in altair                        |
| changeColorLine(color_line)                 | Replaces the value in colors['axis'] that define the color of the grid and axis lines and re register the theme in altair |

### ConfigModel

### AxisModel

### HeaderModel

### LegendModel

### MarkModel

### RangeModel

### TitleModel

### ViewModel

## Themes

The themes provided in this library are based in the model ModelTheme where the only variations are the color used. The
color schemes were inspired by the [Color Brewer] project and also check in [WAIM] contrast, so it follows the
regulations of the WCAG2.0

### accessible_theme

The theme uses a white background with dark text and axis, the palette of colors consists of colors that vary its hue,
so it can be distinguished

```python
class AccessibleTheme(ModelTheme):
    def __init__(self):
        super().__init__('accessible_theme', COLOR_PRIMITIVES["black"], COLOR_PRIMITIVES["black"],
                         COLOR_PRIMITIVES["blue"]['30'], COLOR_PRIMITIVES["white"], False)
```

### dark_accessible_theme

The theme uses a dark background with white text and axis enhancing that a light version the palette of colors uses a
variation in illumination, so it can be distinguished

```python
class DarkAccessibleTheme(ModelTheme):
    def __init__(self):
        super().__init__('dark_accessible_theme', COLOR_PRIMITIVES["white"], COLOR_PRIMITIVES["white"],
                         COLOR_PRIMITIVES["blue"]['30'], COLOR_PRIMITIVES["black"], False)
        self.change_categorical_scheme(COLORS["schemes"]['categorical']['paired'])

    def change_categorical_scheme(self, scheme: List[str]):
        super().change_categorical_scheme(scheme)
```

### filler_pattern_theme

This theme uses a white background and dark text and axis, its particularity comes in is color palette, the color
palette follows the same reason of changing its hue but also adds a filler pattern, so the marks can be more visible
between themselves
This is possible to do only with our [create_accessible_scheme()] function since it preloads svg in the HTML to be used

```python
class FillerPatternTheme(ModelTheme):
    def __init__(self):
        super().__init__('filler_pattern_theme', COLOR_PRIMITIVES["black"], COLOR_PRIMITIVES["black"],
                         COLOR_PRIMITIVES["blue"]['30'], COLOR_PRIMITIVES["white"], False)
        self.change_categorical_scheme(
            ["url(#red-heart)", "url(#blue-rain)", "url(#green-leaf)", "url(#purple-grapes)", "url(#orange-orange)",
             "url(#yellow-star)", "url(#brown-chocolate)", "url(#pink-donut)", "url(#grey-wrench)", ])

    def change_categorical_scheme(self, scheme: List[str]):
        super().change_categorical_scheme(scheme)
```

### print_friendly_theme

The theme is meant to work if the graph ever is printed and photocopied on a gray scale. Does not follow the WCAG2.0
regulations

```python
class PrintFriendlyTheme(ModelTheme):
    def __init__(self):
        super().__init__('print_theme', COLOR_PRIMITIVES["black"], COLOR_PRIMITIVES["black"],
                         COLOR_PRIMITIVES["blue"]['30'], COLOR_PRIMITIVES["white"], False)
        self.change_categorical_scheme(COLORS["schemes"]['categorical']['set3'])

    def change_categorical_scheme(self, scheme: List[str]):
        super().change_categorical_scheme(scheme)
```

## Top-Level Functions

Our library beside the themes and models offers two functions that can come handy to make accessible chart faster

### create_accesible_scheme()

This function works similar like the altair.Chart.save() function but offers more options for the user in the HTML being
able to change the color palette, increase/decrese the font size and size of the chart. Also, will show a description if
given in HTML
All this function also work with keyboard navigation so can be used for more people

```python
def create_accessible_scheme(chart: Chart, filename: str = 'test', description: str = None):
```

**Parameters**:

**chart** : altair.Chart

Any Chart object of Altair works to be rendered, but not all Charts can used the functions described in the HTML these
include LayerChart, HConcatChart, VConcatChart, FacetChart, RepeatChart

**filename**: str

The name of the HTML to create

**description**: str

A description for the chart given, if given it will be included in the aria-label of the chart and shown in the HTML in
a div

### generate_description()

This function can generate a description for a given chart, it's powered by BrailleR, so it has prerequisite to be used
and that is to have R installed with the appropriate libraries
It works recreating the chart in R, so it can only use simple charts

```python
def generate_description(chart: Chart, type_chart: str, axis_x: List, axis_y: List):
```

**Parameters**:

**chart** : altair.Chart

Any Chart object of Altair works to be used

**type_chart** : str, ['barchart','scatterplot', 'linechart','piechart']

Define the type of Chart to be sent to R

**axis_x** : List

A list that contains the values of the X axis can be either str, int or float

**axis_y** : List

A list that contains the values of the X axis can be either str, int or float

**Return**:

It returns a dict object with either of the next keys:

- 'res' It contains a string with a description of the chart
- 'error' It contains the description of the exception that occurred
## Patterns

## Tokens

## Types

[Getting Started]: index.md

[Examples]: p2-examples.md

[ModelTheme]: #modeltheme

[ConfigModel]:#configmodel

[AxisModel]:#axismodel-

[HeaderModel]:#headermodel

[LegendModel]:#legendmodel

[MarkModel]:#markmodel

[RangeModel]:#rangemodel

[TitleModel]:#titlemodel

[ViewModel]:#viewmodel

[ColorName]:https://altair-viz.github.io/user_guide/generated/core/altair.ColorName.html#altair.ColorName

[Color Brewer]:https://colorbrewer2.org/#type=qualitative&scheme=Dark2&n=3

[WAIM]:https://webaim.org/resources/contrastchecker/

