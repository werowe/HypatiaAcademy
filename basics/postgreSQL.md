# Create Inventory System Databases and Add Some Data


# Notes for Walker
* create database mumteha;
* create user mumteha with encrypted password 'xxxx';
* grant all privileges on database mumteha to mumteha;


# Connect to Database
psql -h paris2x -d mumteha -U xxxx




# Create Customers and Orders Table

```sql
CREATE TABLE customers
  ( 
     customernumber     varchar(100) PRIMARY KEY, 
    customername varchar(50),
    phonenumber varchar(50),
    postalcode varchar(50),
    locale varchar(10),
    datecreated date,
    email varchar(50)
  );


CREATE TABLE orders
  ( 
     customernumber    varchar(100) ,
    ordernumber varchar(100) varchar(100) PRIMARY KEY,
    comments varchar(200),
    orderdate date,
    ordertype varchar(10),
    shipdate date,
discount float,
quantity int,
    productnumber varchar(50)
);
```

# Add some Data

 

Copy and paste [this data](https://raw.githubusercontent.com/werowe/glue/master/customersOrders.sql) into PostgreSQL:



