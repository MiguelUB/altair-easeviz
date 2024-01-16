# About

## Roadmap

### First approach

When starting this project, the first idea that crossed our minds was to create a completely separate branch of
Altair where we could configure the internal files of the library.
While this may seem like the logical thing to do, it is a monumental and unrealistic job for one person in a short time.

The second and more realistic idea was to be able to create a theme that had accessible parameters to be able to
visualize and improve the graphics rendered by vega-lite however, this was limited to returning altering the vega-lite
specification in a function.

### Understanding limitations

Our development process centered around two pivotal constraints. Firstly, we aimed to create a library seamlessly
integrated with Vega-Altair and its projects, ensuring no disruption to their established workflows. Secondly, we
aspired to
empower programmers by providing tools that augment the existing capabilities of Vega-Altair.

One significant limitation stems from the standard method of saving charts in Vega-Altair, which predominantly employs
the
canvas tag. While functional, the canvas tag proves more restrictive compared to the SVG tag. Unlike the canvas tag, SVG
supports diverse customization options, including fill patterns, custom JavaScript, and detailed descriptions for each
graph element.

Another notable limitation arises from our commitment to refrain from altering the source code of Vega-Altair and
Vega-Lite.
Adhering to this principle necessitates our library to gracefully adapt to the offerings of both platforms.
Consequently, certain innovative ideas,
such as navigating the chart with the keyboard and introducing sound elements to graphics,
had to be set aside.

In essence, our approach involves a nuanced understanding of these limitations, steering our development decisions
towards creating a library that aligns seamlessly with Vega-Altair's existing ecosystem.

### The final approach

So with that in mind, we make one step further, taking inspiration from
the [Feedzai theme](https://github.com/feedzai/feedzai-altair-theme/tree/master) and also applying more
organization when creating a theme.

The next step then focused on creating models to store values that the Vega-Lite specification expects, then create
tokens like color values, font sizes and others and finally typing files to ensure that what the models return to us is
what was
expected by the API.

With all these new ideas is that we created a simple and organized system of models that use correctly can create a
simple and robust theme, and with these very same models we create four accessible themes that attempt to create
graphics
more accessible.

### Graphs for everyone and beyond

The last thing we thought is that since each person is different and may have different needs or tastes, it was to give
them simple options so that they can customize the graph in their own way. From this idea came the
create_accesible_scheme() function which It is the same as altair.chart.save('test.hml'), since both create an HTML
where the chart is rendered, but our function adds options to improve its visualization.

## Vega-Lite Specification

All our models are a direct reference to the Vega-Lite specification, although we only took the parameters that we
thought were most
relevant, but that does not prevent us from adding any other attribute that we have not defined but is present in the
Vega-Lite specification.

## Licensing

The altair-easeviz is an open source project with a MIT license, you can use it to expand it or learn how you can
improve your charts.

## FAQS

### Does this library support layered, repeated, concat and facet charts?

While the theme set will have no problems with these kinds of charts, the function create_accesible_scheme() does not
fully
support this kind of chart specially the options to change the graph size or color scheme.

### Do I need to have R installed to use the library?

No, only if you want to use the function generate_description().

### Can I expand or suggest new features to the project?

Yes, is always welcome new features to keep improving.

### I made new theme with the models but does not work

Remember in order to create a theme is necessary to register then enable it .

### Registering the theme gave me a error dict is not function

The register expect altair.theme.register('name_theme', a_function()), check what you are passing.


