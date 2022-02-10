CREATE TABLE peoplebooks (
    id BIGSERIAL NOT NULL,
    person_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    CONSTRAINT pk_key PRIMARY KEY (id)
);

CREATE INDEX performance ON peoplebooks USING btree (book_id);

SELECT book_id
FROM peoplebooks
GROUP BY book_id
ORDER BY book_id
