#!/usr/bin/env python
from {{folder_name}}.team import {{team_name}}Team


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    {{team_name}}Team().team().kickoff(inputs=inputs)
