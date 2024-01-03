def xml_to_md(xml):
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