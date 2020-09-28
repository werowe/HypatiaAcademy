

pip install JayDeBeApi

 create database mumteha
expenses-# use mumteha
expenses-# create user mumteha
expenses-# ;
ERROR:  syntax error at or near "create"
LINE 3: create user mumteha
        ^
expenses=# create database mumteha;
CREATE DATABASE
expenses=# create user mumteha with encrypted password 'mumteha';
CREATE ROLE
expenses=# grant all privileges on database mumteha to mumteha;

psql -h paris2x -d mumteha -U mumteha
