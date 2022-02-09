CREATE TABLE peoplebooks (
    id BIGSERIAL NOT NULL,
    person_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    CONSTRAINT pk_key PRIMARY KEY (id)
);

CREATE INDEX performance ON peoplebooks USING btree (book_id);

SELECT count(person_id) AS have_both_books
FROM peoplebooks
WHERE book_id = 1;


WITH first AS (
    SELECT person_id, book_id AS first_book
    FROM peoplebooks
    WHERE book_id = 38
), second AS (
    SELECT person_id, book_id AS second_book
    FROM peoplebooks
    WHERE book_id = 21
)
SELECT COUNT(first.person_id)
FROM first, second
WHERE first.person_id = second.person_id;