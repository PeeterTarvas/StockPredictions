CREATE TABLE peoplebooks
(
    id BIGSERIAL NOT NULL,
    person_id NUMERIC NOT NULL,
    book_id NUMERIC NOT NULL,
    CONSTRAINT pk_key PRIMARY KEY (id)
)