# Chanx Django Tutorial

A comprehensive tutorial demonstrating how to build real-time WebSocket applications with Django using the [Chanx](https://github.com/huynguyengl99/chanx) package. This project showcases three different real-time communication patterns with interactive UI examples.

## 🎯 What You'll Learn

This tutorial demonstrates three practical WebSocket use cases:

1. **Chat Rooms** - Multi-user real-time chat with room-based messaging
2. **Assistant Chat** - AI-powered assistant with streaming responses (requires OpenAI API key)
3. **System Background Tasks** - Background job processing with Celery and real-time notifications

Each example includes a complete implementation with Django views, WebSocket consumers, and interactive HTML/JavaScript frontends.

## 🚀 Features

- **Real-time WebSocket Communication** using Chanx
- **Multiple Chat Applications** with different use cases
- **Beautiful UI** with modern, responsive design
- **WebSocket Logging** for debugging sent/received messages
- **Connection Status Indicators**
- **Message History** with timestamps
- **Navigation Bar** for easy switching between apps

## Stack & Framework

- [Django](https://www.djangoproject.com/) - Batteries-included Python web framework
- [Chanx](https://github.com/huynguyengl99/chanx) - WebSocket package for Django
- [Django REST Framework](https://www.django-rest-framework.org/) - Powerful toolkit for building Web APIs
- [Celery](https://docs.celeryq.dev/) - Distributed task queue for background jobs
- [PostgreSQL](https://www.postgresql.org/) - Well-known open source database system
- [Redis](https://redis.io/) - In-memory data structure store and message broker

## Prerequisites

Before starting development, ensure you have the following installed:

- [UV](https://docs.astral.sh/uv/): Python version & package management
- [Docker](https://www.docker.com/products/docker-desktop/): Docker app for launching services like db, redis, etc.

## Getting Started

### Environment & Dependencies Setup

Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate
```

Install all dependencies:
```bash
uv sync
```

### Running the Application

1. **Configure environment variables**:

   First, create a `.env` file from the example:
   ```bash
   cp .env.EXAMPLE .env
   ```

   Then edit the `.env` file and add your OpenAI API credentials (required for Assistant Chat):
   ```bash
   OPENAI_API_KEY=your-openai-api-key-here
   OPENAI_ORG=your-openai-org-id-here  # Optional
   ```

2. **Start Docker services**:
```bash
docker compose up -d
```

3. **Run database migrations**:
```bash
python chanx_django/manage.py migrate
```

4. **Create a superuser** (to access admin page):
```bash
python chanx_django/manage.py createsuperuser
```

5. **Start the development environment**:

   Option A - Use the development script (starts both Django and Celery):
   ```bash
   python chanx_django/start_dev.py
   ```

   Option B - Start services separately:
   ```bash
   # Terminal 1: Start Celery worker
   cd chanx_django && celery -A config worker --loglevel=info

   # Terminal 2: Start Django server
   python chanx_django/manage.py runserver 8000
   ```

6. **Access the application**:
   - Landing page: http://localhost:8000/
   - Admin interface: http://localhost:8000/admin/
   - Chat Rooms: http://localhost:8000/chat/
   - Assistant Chat: http://localhost:8000/assistants/
   - System Chat: http://localhost:8000/system/

### Setting Up Pre-commit Hooks (Optional)

To automatically format code and check dependencies before commits:
```bash
pre-commit install
```

## 📚 Project Structure

The project is organized into separate Django apps for each use case:

- **core** - Shared templates, landing page, and common functionality
- **chat** - Multi-user chat rooms with room-based messaging
- **assistants** - AI assistant chat interface
- **system** - System notifications and administrative messaging
- **config** - Django settings and main URL configuration

## 🎨 UI Features

- **Modern Design**: Clean, gradient-based UI with smooth animations
- **Responsive Layout**: Works on desktop and mobile devices
- **Navigation Bar**: Easy switching between different chat apps
- **WebSocket Logs**: Built-in debugging modal to view all sent/received messages
- **Connection Status**: Visual indicator showing WebSocket connection state
- **Message History**: Scrollable message container with timestamps
- **Keyboard Support**: Press Enter to send messages

## 📖 Tutorial Topics Covered

1. **Setting up Django with Chanx**
2. **Creating WebSocket consumers**
3. **Building real-time chat interfaces**
4. **Handling different message types**
5. **Managing WebSocket connections**
6. **Debugging WebSocket communication**
7. **Creating reusable chat templates**
8. **Implementing room-based messaging**
9. **Integrating Celery for background tasks**
10. **Real-time task result notifications**
11. **Broadcasting messages from management commands**

## 🔧 System Background Tasks

The System app demonstrates background job processing with Celery:

### Available Tasks

- **🌍 Translate**: Simulates text translation (2s delay)
- **📊 Analyze**: Analyzes text statistics (3s delay)
- **🤖 Generate**: AI-like response generation (4s delay)
- **✅ Default**: Simple text processing (1s delay)

### Usage

1. Visit http://localhost:8000/system/
2. Select a task type using the buttons
3. Type your message and send
4. Watch real-time progress:
   - Job queued confirmation (instant)
   - Processing in background
   - Result delivered via WebSocket

### Sending Notifications

Use the management command to broadcast notifications to all connected system clients:

```bash
# Send a single notification
python chanx_django/manage.py send_notification "Server maintenance starting soon"

# Send multiple notifications with interval
python chanx_django/manage.py send_notification "Status update" --repeat 3 --interval 2
```

## 🛠️ Development

The project uses:
- **Django 5.2+** for the web framework
- **UV** for Python package management
- **Docker Compose** for PostgreSQL and Redis
- **Pre-commit hooks** for code quality

## 📝 License

This project is open source and available for educational purposes.

## 🔗 Resources

- [Chanx Documentation](https://github.com/huynguyengl99/chanx)
- [Django Documentation](https://docs.djangoproject.com/)
- [WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
