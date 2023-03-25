CREATE TABLE subsbytime AS
  SELECT
    month,
    day_of_week,
    COUNT(y) AS subscribe
FROM stream_bank_marketing
GROUP BY month, day_of_week;