create table tasks
(
    id             serial                            not null
        constraint tasks_pk
            primary key,
    quantity_posts integer,
    status         text default 'Не выполнено'::text not null,
    profile        text                              not null
);

alter table tasks
    owner to postgres;

create unique index tasks_id_uindex
    on tasks (id);

INSERT INTO public.tasks (id, quantity_posts, status, profile) VALUES (3, 2, 'Выполнено', 'instasamka');
INSERT INTO public.tasks (id, quantity_posts, status, profile) VALUES (4, 2, 'Выполнено', 'some_name');