


{{ config(materialized='table') }}

select survey_key,timestamp,python_skill,career,future_goal,expectations,pace,difficulty,balance
from sehar_fatima.survey