

{{ config(materialized='table') }}

select survey_key, ls AS learning_style
from sehar_fatima.survey, unnest(SPLIT(learning_style,',')) AS ls