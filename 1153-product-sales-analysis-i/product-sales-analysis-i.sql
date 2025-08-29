select product_name, s.year, s.price
from sales as s
left join product p
on s.product_id = p.product_id;


