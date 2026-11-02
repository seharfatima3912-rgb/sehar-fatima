
-- Use the `ref` function to select from other models

select *
from {{ ref('python_topics') }}
where id = 1
