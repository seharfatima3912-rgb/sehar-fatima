

{{ config(materialized='table') }}


select survey_key, pt AS python_topics
from sehar_fatima.survey, unnest(SPLIT(python_logics,',')) AS pt