{{config(materialized = 'table',
  tags=['marts', 'customer'],
  indexes=[
    {'columns': ['customer_id'], 'unique':true}
  ])}}

select
  customer_id,
  count(*) as total_transactions,
  sum(amount) as total_amount,
  avg(amount) as avg_transaction_amount,
  min(transaction_date) as first_transaction_date,
  max(transaction_date) as last_transaction_date,

  -- Business metrics
  sum(case when transaction_type = 'credit' then amount else 0 end) as total_credits,
  sum(case when transaction_type = 'debit' then amount else 0 end) as total_debits,
  count(case when transaction_type = 'credit' then 1 end) as credit_count,
  count(case when transaction_type = 'debit' then 1 end) as debit_count

from {{ref('stg_transactions')}}
group by customer_id
order by total_amount desc