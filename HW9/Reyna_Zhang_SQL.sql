use sakila;
-- 1a)
select first_name, last_name from actor;

-- 1b)
select concat(first_name, " ", last_name) as "Actor Name" from actor;

-- 2a)
select actor_id,first_name,last_name from actor where first_name = "Joe";

-- 2b)
select * from actor where last_name like "%GEN%";

-- 2c)
select * from actor where last_name like "%LI%" order by last_name, first_name;

-- 2d)
select country_id,country from country where country in ("Afghanistan","Bangladesh","China");

-- 3a)
alter table actor
add column description BLOB;

-- 3b)
alter table actor
drop column description;

-- 4a)
select last_name, count(last_name) as "last_name_count" from actor
group by last_name;

-- 4b)
select last_name, count(last_name) as "last_name_count" from actor
group by last_name
having count(last_name) > 1;

-- 4c)
update actor
set first_name = "HARPO"
where first_name = "GROUCHO"
and last_name = "WILLIAMS";

-- 4d)
update actor
set first_name = "GROUCHO"
where first_name = "HARPO"
and last_name = "WILLIAMS";

-- 5a)
show create table address;

-- 6a)
select first_name,last_name,address from staff 
left join address on staff.address_id = address.address_id;

-- 6b)
select staff.first_name,staff.last_name,sum(amount) from payment 
inner join staff on payment.staff_id = staff.staff_id
where month(payment_date) = 8 and year(payment_date) = 2005
group by first_name, last_name;

-- 6c)
select title,count(*) as num_of_actors from film 
inner join film_actor on film.film_id = film_actor.film_id
group by film.film_id;

-- 6d)
select title, count(*) as num_of_copies from inventory inner join film on inventory.film_id = film.film_id
where film.title = "Hunchback Impossible";

-- 6e)
select * from customer;
select first_name,last_name,sum(amount)as tot_payment from payment 
inner join customer on payment.customer_id = customer.customer_id
group by first_name,last_name order by last_name;

-- 7a)
-- not subquery way
select film.title from film 
inner join language on film.language_id = language.language_id
where language.name = "English"
and (upper(film.title) like "K%" or upper(film.title) like "Q%");
-- subquery way
select title from film
where film.language_id in (
select language_id from language where language.name = "English"
)
and (upper(film.title) like "K%" or upper(film.title) like "Q%");



-- 7b)
-- not subquery way
select concat(first_name, " ",last_name) as actor_name,title as film_title from actor 
inner join film_actor on film_actor.actor_id = actor.actor_id
inner join film on film.film_id = film_actor.film_id
where film.title = "Alone Trip";
-- subquery way
select concat(first_name, " ",last_name) as actor_name from actor
where actor_id in (
select actor_id from film_actor where film_id in (
select film_id from film where title = "Alone Trip"
)
);

-- 7c)
select concat(first_name, " ",last_name) as customer_name,
email,country.country from customer
inner join address on customer.address_id = address.address_id
inner join city on address.city_id =  city.city_id
inner join country on city.country_id = country.country_id
where country.country = "Canada";

-- 7d)
select film.title, category.name as category from film
inner join film_category on film.film_id = film_category.film_id
inner join category on category.category_id = film_category.category_id
where category.name = "Family";

-- 7e)
select film.title,count(*)as rent_count from rental
left join inventory on rental.inventory_id = inventory.inventory_id
left join film on inventory.film_id = film.film_id
group by film.title order by rent_count desc;

-- 7f)
select store.store_id,concat("$",format(sum(amount),2)) as payment from payment
left join staff on payment.staff_id = staff.staff_id
left join store on staff.store_id = store.store_id
group by store.store_id;

-- 7g)
select store.store_id, city.city, country.country from store
left join address on store.address_id = address.address_id
left join city on address.city_id = city.city_id
left join country on city.country_id = country.country_id;

-- 7h)
select category.name as top_5_genre,
concat("$",format(sum(payment.amount),2)) as gross_revenue from payment
inner join rental on payment.rental_id = rental.rental_id
inner join inventory on rental.inventory_id = inventory.inventory_id
inner join film on inventory.film_id = film.film_id
inner join film_category on film.film_id = film_category.film_id
inner join category on film_category.category_id = category.category_id
group by top_5_genre order by gross_revenue desc limit 5;

-- 8a)
create view top_5_genre_revenue as
select category.name as top_5_genre,
concat("$",format(sum(payment.amount),2)) as gross_revenue from payment
inner join rental on payment.rental_id = rental.rental_id
inner join inventory on rental.inventory_id = inventory.inventory_id
inner join film on inventory.film_id = film.film_id
inner join film_category on film.film_id = film_category.film_id
inner join category on film_category.category_id = category.category_id
group by top_5_genre order by gross_revenue desc limit 5;

-- 8b)
select * from top_5_genre_revenue;

-- 8c)
drop view if exists top_5_genre_revenue;






































