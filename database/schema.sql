-- Hotel Database Schema
-- hotel_db
 
CREATE TABLE IF NOT EXISTS guests (
    id_guest    SERIAL PRIMARY KEY,
    first_name  VARCHAR(100)  NOT NULL,
    last_name   VARCHAR(150)  NOT NULL,
    email       VARCHAR(254)  UNIQUE,
    phone       VARCHAR(20)   NOT NULL,
    dni         VARCHAR(20)   NOT NULL UNIQUE
);
 
CREATE TABLE IF NOT EXISTS rooms (
    id_room          SERIAL PRIMARY KEY,
    room_number      INTEGER       NOT NULL UNIQUE,
    room_type        VARCHAR(20)   NOT NULL,
    price_per_night  NUMERIC(8,2)  NOT NULL,
    status           VARCHAR(20)   NOT NULL DEFAULT 'available'
);
 
CREATE TABLE IF NOT EXISTS bookings (
    id_booking      SERIAL PRIMARY KEY,
    id_guest        INTEGER       NOT NULL REFERENCES guests(id_guest) ON DELETE CASCADE,
    id_room         INTEGER       NOT NULL REFERENCES rooms(id_room) ON DELETE CASCADE,
    check_in_date   DATE          NOT NULL,
    check_out_date  DATE          NOT NULL,
    total_price     NUMERIC(10,2) NOT NULL,
    status          VARCHAR(20)   NOT NULL DEFAULT 'pending',
    CONSTRAINT chk_dates CHECK (check_out_date > check_in_date)
);