import markdown


def render_markdown(value):
    return markdown.markdown(
        value,
        extensions=[
            'extra',
            'codehilite',
            'blog.md_converter.mdx.mdx_mathjax',
        ],
        extension_configs={
            'codehilite': [
                ('guess_lang', False),
            ]
        },
        output_format='html5',
    )
