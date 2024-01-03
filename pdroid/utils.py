"""Miscellaneous helper functions used throughout the application."""

def xml_to_md(xml):
    """Function for converting raw xml output into a markdown output for easy copy/paste."""
    title = xml[0]["title"].strip()
    description = xml[1]["description"].strip()
    story = xml[2]["story"].strip()
    subtask = xml[3]["subtask"].strip()
    ac = xml[4]["acceptance-criteria"].strip()
    md = f'''\
# {title}

# Description
{description}

# Story
{story}

# Subtasks
{subtask}

# Acceptance Criterias
{ac}
'''.replace('\n','<br>').replace('\t','nbsp;')
    return md