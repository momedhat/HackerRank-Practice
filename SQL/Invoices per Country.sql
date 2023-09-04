-- Invoices per Country Solution

SELECT c.country_name, count(inv.invoice_number), avg(inv.total_price) as avginv
FROM 
	country c 
	join 
	city on c.id = city.country_id
	join
	customer on city.id = customer.city_id
	join
	invoice inv on inv.customer_id = customer.id

GROUP BY c.country_name
having avginv > (select avg(total_price) from invioce)