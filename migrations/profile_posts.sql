create table profile_posts
(
    profile_id integer not null
        constraint profile_posts_tasks_id_fk
            references tasks,
    posts_id   integer not null
        constraint profile_posts_posts_id_fk
            references posts
);

alter table profile_posts
    owner to postgres;

create unique index profile_posts_posts_id_uindex
    on profile_posts (posts_id);

INSERT INTO public.profile_posts (profile_id, posts_id) VALUES (3, 14);
INSERT INTO public.profile_posts (profile_id, posts_id) VALUES (3, 15);
INSERT INTO public.profile_posts (profile_id, posts_id) VALUES (4, 16);
INSERT INTO public.profile_posts (profile_id, posts_id) VALUES (4, 17);