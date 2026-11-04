
{{ config(materialized='table') }}


select survey_key, int AS interests
from sehar_fatima.survey, unnest(SPLIT(interests,',')) AS int 