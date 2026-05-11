--
-- PostgreSQL database dump
--

\restrict 9YfCStOiAHgyDTZowyE1074AFYLG5dmj845pRmgt30CmpfAMoEvYVnHQGztTfpl

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

--
-- Data for Name: guests; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.guests VALUES (1, 'Laura', 'Reyero', 'laura@email.com', '600123456', '12345678A');
INSERT INTO public.guests VALUES (4, 'Ana', 'Garcia', 'ana@email.com', '600999888', '87654321B');
INSERT INTO public.guests VALUES (36, 'Sofía', 'González', 'soph@gmail.com', '627539320', '53990109B');
INSERT INTO public.guests VALUES (39, 'Sonia', 'Macas', 'macas@gmail.com', '635549210', '53848809B');
INSERT INTO public.guests VALUES (40, 'Alexia', 'Putellas', 'lareina@gmail.com', '627569230', '54980198N');


--
-- Data for Name: rooms; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.rooms VALUES (1, 101, 'single', 80.00, 'available');
INSERT INTO public.rooms VALUES (2, 102, 'double', 120.00, 'available');
INSERT INTO public.rooms VALUES (3, 201, 'suite', 250.00, 'available');
INSERT INTO public.rooms VALUES (6, 210, 'double', 180.00, 'available');
INSERT INTO public.rooms VALUES (4, 211, 'double', 180.00, 'available');


--
-- Data for Name: bookings; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Name: bookings_id_booking_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bookings_id_booking_seq', 1, false);


--
-- Name: guests_id_guest_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.guests_id_guest_seq', 40, true);


--
-- Name: rooms_id_room_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rooms_id_room_seq', 6, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 9YfCStOiAHgyDTZowyE1074AFYLG5dmj845pRmgt30CmpfAMoEvYVnHQGztTfpl

