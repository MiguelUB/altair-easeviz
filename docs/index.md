# Getting Started

## Overview

This Python library is dedicated to providing resources for [Vega-Altair](https://altair-viz.github.io/index.html), with
the aim of enhancing the creation of
improved
and more accessible graphs. The development of this library involved a thorough exploration of both the Altair and
Vega-Lite APIs.

For programmers, the library offers a suite of tools, including utilities for crafting new Vega-Altair themes, pre-built
accessible themes, and description generators (Powered by BrailleR).

From a user perspective, the library facilitates limited customization of the graph, allowing choices such as color
scheme selection, text size adjustment, and graph size modification.
This is due to a function that creates an HTML using a chart as a parameter.

The overarching concept behind the library mirrors that of Vega-Altair, the majority of graph configurations and details
are
seamlessly managed by the library, affording users more time to focus on their data.
It is important to note that the library does not modify any fundamental concepts, functions, or APIs of Vega-Altair;
instead, it enriches the toolkit with additional resources.

This documentation serves as a reference for the resources available post-installation and aims to provide insights into
creating accessible graphs.

## Installation

The library and its dependencies can be easily installed, using:

```
pip install altair-easeviz
```

After installation, the next built-in themes should be ready to use:

- accessible_theme
- dark_accessible_theme
- filler_pattern_theme
- print_friendly_theme

You can enable them, using:

``` py
import altair as alt

alt.themes.enable("accessible_theme")
```

## Requirements

The library was built for:

- altair==5.* -
- typing-extensions>=4.0, <5
- jinja2==3.*
- pyRserve>=1.0.*

Also, in order to use the function generate_description() is necessary to have R running in the background, and have
installed the libraries:

- BrailleR
- ggplot2

## Getting Help

You can browse this documentation via the links in the top navigation panel or by viewing the [API page](p2-api.md).
In addition to reading this documentation page, it can be helpful to also browse the source code of this project.

The code source is available in [GitHub](https://miguelub.github.io/altair-easeviz/) where you can report any bugs or
request features.

## Project Philosophy

This project has the same approach as the Vega-Altair library that is a simple user interface
that focuses most of the resources on an experience ready to use after installation, but with the possibility to still
be abel to create something more complex and complete.

