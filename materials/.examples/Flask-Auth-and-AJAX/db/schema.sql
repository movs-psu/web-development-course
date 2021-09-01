create table users
(
    id       integer not null
        constraint users_pk
            primary key autoincrement,
    email    text    not null,
    password text    not null
);

create table todos
(
    id      integer
        constraint todos_pk
            primary key autoincrement,
    title   text    not null,
    user_id integer not null
        references users
            on update cascade on delete cascade,
    done    integer default 0
);

create unique index users_email_uindex
    on users (email);
