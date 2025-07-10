{{config(materialized = 'view')}}

select
  -- Add any column cleaning/renaming here
  transaction_id,
  customer_id,
  cast(amount as decimal(10,2)) as amount,
  cast(transaction_date as date) as transaction_date,

  -- Add any calculated fields
  case
    when amount > 0 then 'credit'
    else 'debit'
  end as transaction_type,

  -- Metadata
  current_timestamp as _loaded_at

from {{source('main', 'transactions')}}
