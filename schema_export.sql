--
-- PostgreSQL database dump
--

\restrict YO4NJBlB16hhNHZdP1IfE2M938R3N42EYNwdWyAyyeiy2xuBB4GXUaGPAHMIgON

-- Dumped from database version 16.13 (Ubuntu 16.13-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.13 (Ubuntu 16.13-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bookings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bookings (
    id_booking integer NOT NULL,
    id_guest integer NOT NULL,
    id_room integer NOT NULL,
    check_in_date date NOT NULL,
    check_out_date date NOT NULL,
    total_price numeric(10,2) NOT NULL,
    status character varying(20) DEFAULT 'pending'::character varying NOT NULL,
    CONSTRAINT chk_dates CHECK ((check_out_date > check_in_date))
);


ALTER TABLE public.bookings OWNER TO postgres;

--
-- Name: bookings_id_booking_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bookings_id_booking_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.bookings_id_booking_seq OWNER TO postgres;

--
-- Name: bookings_id_booking_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bookings_id_booking_seq OWNED BY public.bookings.id_booking;


--
-- Name: guests; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.guests (
    id_guest integer NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254),
    phone character varying(20) NOT NULL,
    dni character varying(20) NOT NULL
);


ALTER TABLE public.guests OWNER TO postgres;

--
-- Name: guests_id_guest_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.guests_id_guest_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.guests_id_guest_seq OWNER TO postgres;

--
-- Name: guests_id_guest_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.guests_id_guest_seq OWNED BY public.guests.id_guest;


--
-- Name: rooms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rooms (
    id_room integer NOT NULL,
    room_number integer NOT NULL,
    room_type character varying(20) NOT NULL,
    price_per_night numeric(8,2) NOT NULL,
    status character varying(20) DEFAULT 'available'::character varying NOT NULL
);


ALTER TABLE public.rooms OWNER TO postgres;

--
-- Name: rooms_id_room_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rooms_id_room_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.rooms_id_room_seq OWNER TO postgres;

--
-- Name: rooms_id_room_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rooms_id_room_seq OWNED BY public.rooms.id_room;


--
-- Name: bookings id_booking; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bookings ALTER COLUMN id_booking SET DEFAULT nextval('public.bookings_id_booking_seq'::regclass);


--
-- Name: guests id_guest; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guests ALTER COLUMN id_guest SET DEFAULT nextval('public.guests_id_guest_seq'::regclass);


--
-- Name: rooms id_room; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rooms ALTER COLUMN id_room SET DEFAULT nextval('public.rooms_id_room_seq'::regclass);


--
-- Name: bookings bookings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bookings
    ADD CONSTRAINT bookings_pkey PRIMARY KEY (id_booking);


--
-- Name: guests guests_dni_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guests
    ADD CONSTRAINT guests_dni_key UNIQUE (dni);


--
-- Name: guests guests_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guests
    ADD CONSTRAINT guests_email_key UNIQUE (email);


--
-- Name: guests guests_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.guests
    ADD CONSTRAINT guests_pkey PRIMARY KEY (id_guest);


--
-- Name: rooms rooms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_pkey PRIMARY KEY (id_room);


--
-- Name: rooms rooms_room_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_room_number_key UNIQUE (room_number);


--
-- Name: bookings bookings_id_guest_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bookings
    ADD CONSTRAINT bookings_id_guest_fkey FOREIGN KEY (id_guest) REFERENCES public.guests(id_guest) ON DELETE CASCADE;


--
-- Name: bookings bookings_id_room_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bookings
    ADD CONSTRAINT bookings_id_room_fkey FOREIGN KEY (id_room) REFERENCES public.rooms(id_room) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict YO4NJBlB16hhNHZdP1IfE2M938R3N42EYNwdWyAyyeiy2xuBB4GXUaGPAHMIgON

