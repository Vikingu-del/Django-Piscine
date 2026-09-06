# Django Piscine — Real-Time Chat & User Management System (d09)

A progressive, real-time web application built with **Django 5.2**, **Django Channels (ASGI/Daphne)**, **WebSockets**, and **Bootstrap 5**. This project demonstrates the step-by-step implementation of authenticated user management, real-time asynchronous communication, message persistence, user presence tracking, and UI auto-scrolling across five incremental exercises (`ex00` to `ex04`).

---

## Features Across Exercises

* **Exercise 00 (Authentication & Routing):** Full account management (login, logout, registration) routed through `account/` with root path (`/`) redirection and custom 404 error handling.
* **Exercise 01 (Real-Time WebSockets):** Live chat room communication using Django Channels, Daphne ASGI server, and WebSocket protocols (pydantic-validated event payloads).
* **Exercise 02 (Message History & Persistence):** Database persistence for chat logs (`Room` and `Message` models) returning the last **3 messages** in chronological order upon joining a room.
* **Exercise 03 (User Presence Sidebar):** Real-time connected user tracking using a thread-safe in-memory registry (`ROOM_USERS`), broadcasting join/leave alerts and maintaining an updated user list in a dedicated Bootstrap sidebar.
* **Exercise 04 (Auto-Scroll & UI Polish):** Fixed-height scrollable chat windows with enforced auto-scrolling to keep the latest messages in view.

---

## Project Structure

```text
.
├── d09/                    # Django project configuration
├── account/                # Exercise 00: User Authentication App
├── chat/                   # Exercises 01-04: Real-time Chat App
├── init_django_venv.sh     # Script to setup virtual environment & dependencies
├── init_database.sh        # Script to configure PostgreSQL user & database
├── init_rooms.sh           # Script to create default chat rooms
├── factory_reset_db.sh     # Script to wipe and reset the database completely
├── manage.py
└── requirements.txt
```


## Prerequisites & Execution Scripts

1. **Set up execution permissions:**
    ```bash
    chmod +x init_django_venv.sh init_database.sh init_rooms.sh factory_reset_db.sh
    ```

2. **Create virtual environment & install dependencies:**
    ```bash
    ./init_django_venv.sh
    ```

3. **Initialize PostgreSQL database:**
    ```bash
    ./init_database.sh
    ```

4. **Populate initial chat rooms:**
    ```bash
    ./init_rooms.sh
    ```
    Access the app at http://127.0.0.1:8000/

5. **Run the development server (Daphne/ASGI):**
    ```bash
    python manage.py runserver
    ```

6. **Reset database to blank state (optional):**
    ```bash
    ./factory_reset_db.sh
    ````


## Requirements

* Python 3.12+
* PostgreSQL
* Django 5.2.13
* chanx[channels, cli, client] == 2.7.1
* django-bootstrap5 == 26.2
* daphne == 4.2.1
* pyhumps == 3.8.0
* psycopg2-binary == 2.9.12
