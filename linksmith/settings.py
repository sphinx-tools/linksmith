import rich_click as click

help_config = click.RichHelpConfiguration(
    use_markdown=True,
    width=100,
    style_option="bold white",
    style_argument="dim cyan",
    style_command="bold yellow",
    style_errors_suggestion_command="bold magenta",
)
