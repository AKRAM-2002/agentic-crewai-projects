#!/usr/bin/env python
import sys
import warnings

from crew import Project1



warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    Project1().crew().kickoff()


run()