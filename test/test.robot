*** Settings ***

Library  robotmk

*** Test Cases ***

Test One
    Add Robotmk Message    WARNING    This is a warning text
    Add Checkmk Test State    CRITICAL    The test should be Critical.