create table posts
(
    id        serial not null
        constraint posts_pk
            primary key,
    likes     integer,
    post_time date,
    url       text   not null
);

alter table posts
    owner to postgres;

create unique index posts_id_uindex
    on posts (id);

create unique index posts_url_uindex
    on posts (url);

INSERT INTO public.posts (id, likes, post_time, url) VALUES (14, 266905, '2021-06-10', 'https://www.instagram.com/p/CP752pFL41q/');
INSERT INTO public.posts (id, likes, post_time, url) VALUES (15, 323005, '2021-06-08', 'https://www.instagram.com/p/CP297HbLPmH/');
INSERT INTO public.posts (id, likes, post_time, url) VALUES (16, 300, '2021-06-08', 'https://www.instagram.com/p/CPasd297HbLPmwH/');
INSERT INTO public.posts (id, likes, post_time, url) VALUES (17, 10, '2021-06-08', 'https://www.instagram.com/p/CP297HbLPmwH/');