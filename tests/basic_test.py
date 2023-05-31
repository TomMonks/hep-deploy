import pandas as pd

from model2 import single_run, Schedule, Scenario

def test_model_can_run():
    '''
    A simple test to confirm the model can run.
    check data is returned in results object
    '''
    schedule = Schedule()
    args = Scenario(schedule)
    
    # short results collection period
    s_results = single_run(args,random_no_set=42)
    assert len(s_results[0]) > 0