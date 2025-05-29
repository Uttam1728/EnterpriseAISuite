<div align="center">

# AI assistant Core Assistant


**A powerful, extensible AI assistant platform with multi-LLM support**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

</div>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-deployment">Deployment</a> •
  <a href="#-use-cases">Use Cases</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-community">Community</a>
</p>

## Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Getting Started](#-getting-started)
- [Configuration](#-configuration)
- [Deployment](#-deployment)
- [Testing](#-testing)
- [Use Cases](#-use-cases)
- [Community](#-community)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact Information](#-contact-information)
- [Additional Resources](#-additional-resources)
- [Visuals](#-visuals)

## 📖 Overview

AI assistant Core Assistant is a robust, production-ready platform for building and deploying AI assistants. Built on FastAPI, it provides a flexible architecture for integrating multiple large language models (LLMs) and tools into a unified interface. ai_assistant_core enables developers to create sophisticated AI applications with features like conversation history management, authentication, and monitoring out of the box.

[//]: # ()
[//]: # (<div align="center">)

[//]: # (</div>)

## ❓ Why ai_assistant_core?

| Feature | ai_assistant_core | Other Solutions |
|---------|----------|-----------------|
| **Multi-LLM Support** | ✅ OpenAI, Claude, Groq | Often limited to one provider |
| **Deployment Ready** | ✅ Docker, K8s, CI/CD | Typically requires custom setup |
| **Authentication** | ✅ Built-in with Clerk | Usually requires separate integration |
| **Conversation Management** | ✅ Threads, history, summarization | Basic or non-existent |
| **Tool Integration** | ✅ MCP framework for tools | Limited or proprietary |
| **Open Source** | ✅ MIT License | Often proprietary or limited |

## ✨ Features

### 🤖 Multi-LLM Integration
- **OpenAI Models**: Full support for GPT-4o, GPT-4, and other OpenAI models
- **Anthropic Claude**: Integration with Claude 3 Opus, Claude 3.5 Sonnet, and other Claude models
- **Groq Support**: High-performance inference with Groq's LLM API
- **Model Switching**: Seamlessly switch between different models within the same application

### 💬 Conversation Management
- **Thread History**: Persistent conversation threads with full history
- **Automatic Summarization**: Smart summarization of long conversations to manage context length
- **Context Management**: Sophisticated handling of context windows for different models

### 🔒 Security & Authentication
- **Clerk Integration**: Secure user authentication and management
- **API Key Management**: Secure storage and rotation of LLM provider API keys
- **Role-Based Access**: Control access to features based on user roles

### 📊 Monitoring & Observability
- **Logging**: Comprehensive logging system for debugging and auditing
- **Sentry Integration**: Error tracking and performance monitoring
- **Usage Metrics**: Track token usage, response times, and other key metrics

### 🚀 Deployment & Scaling
- **Docker Support**: Containerized deployment for consistency across environments
- **Kubernetes Ready**: Configurations for deploying on Kubernetes clusters
- **Database Integration**: PostgreSQL for persistent storage of conversations and settings
- **Redis Support**: Optional caching and rate limiting with Redis

### 🛠️ Extensibility
- **Tool Integration**: Framework for adding custom tools and capabilities
- **MCP Client**: Multi-provider tool calling support for enhanced AI capabilities
- **Modular Architecture**: Easily extend with new models, features, and integrations

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**: Required for running the application
- **PostgreSQL**: Database for storing conversations, user data, and settings
- **Redis** (optional): For caching and rate limiting
- **Docker** (optional): For containerized deployment
- **Kubernetes** (optional): For orchestrated deployment

### Quick Start (Docker)

The fastest way to get started is with Docker:

```bash
docker run -p 8081:80 ai_assistant_core/ai_assistant_core:latest
```

Then visit `http://localhost:8081` in your browser.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai_assistant_core.git
   cd ai_assistant_core
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements/requirements.txt
   ```

3. **Create a local configuration file**
   ```bash
   cp config/default.local.tmp.yaml config/default.local.yaml
   ```

4. **Update the configuration**
   
   Edit `config/default.local.yaml` with your:
   - API keys for OpenAI, Claude, and Groq
   - Database connection strings
   - Authentication settings
   - Other environment-specific configurations

5. **Database Setup**

   ```bash
   # Run database migrations to create schema
   python startup.py --migrate

   # Seed initial model configurations
   python startup.py --seed

   # Or run both migrations and seeding at once
   python startup.py --all
   ```

6. **Start the application**

   ```bash
   python entrypoint.py
   ```

   The application will be available at http://localhost:8081

> **💡 Tip:** For development environments, use the `--debug` flag when starting the application to enable hot reloading and detailed error messages.

## 🔧 Configuration

ai_assistant_core uses a flexible configuration system based on YAML files in the `config/` directory:

| Environment | File | Purpose |
|-------------|------|---------|
| Local | `default.local.yaml` | Local development settings |
| SIT | `default.sit.yaml` | System Integration Testing environment |
| Production | `default.prod.yaml` | Production deployment settings |

### Example Configuration

```yaml
server:
  host: 0.0.0.0
  port: 8081
  debug: false

database:
  url: postgresql://user:password@localhost:5432/ai_assistant_core
  pool_size: 20
  max_overflow: 10

redis:
  url: redis://localhost:6379/0
  ttl: 3600

auth:
  clerk_api_key: your_clerk_api_key
  clerk_frontend_api: your_clerk_frontend_api

llm:
  openai_key: your_openai_key
  claude_key: your_claude_key
  groq_key: your_groq_key

monitoring:
  sentry_dsn: your_sentry_dsn
  environment: production
  log_level: INFO
```

## 🐳 Deployment

### Docker Deployment

#### Building the Image

```bash
docker build -t ai_assistant_core .
```

#### Running with Docker

```bash
docker run -p 8081:80 \
  -e ENVIRONMENT=prod \
  -e OPENAI_KEY=your_openai_key \
  -e CLAUDE_KEY=your_claude_key \
  -e DB_URL=your_database_url \
  ai_assistant_core
```

#### Using Docker Compose

A `docker-compose.yml` file is provided for easy deployment with dependencies:

```bash
docker-compose up -d
```

This will start ai_assistant_core along with PostgreSQL and other required services.

### Kubernetes Deployment

ai_assistant_core includes Kubernetes deployment configurations for production environments:

1. **Apply the configuration**:
   ```bash
   kubectl apply -f k8s/deployment.yaml
   ```

2. **Set up secrets**:
   ```bash
   kubectl create secret generic ai_assistant_core-secrets \
     --from-literal=OPENAI_KEY=your_openai_key \
     --from-literal=CLAUDE_KEY=your_claude_key \
     --from-literal=DB_URL=your_database_url
   ```

3. **Access the service**:
   ```bash
   kubectl port-forward svc/ai_assistant_core 8081:80
   ```

## 🧪 Testing

Run the test suite with:

```bash
./ci-test.sh
```

This will:
- Run unit tests
- Run integration tests
- Generate coverage reports

## 📊 Use Cases

AI assistant Core Assistant can be deployed in various scenarios:

[//]: # ()
[//]: # (### Customer Support)

[//]: # (Deploy an AI assistant that can handle customer inquiries, access knowledge bases, and escalate to human agents when needed.)

[//]: # ()
[//]: # (<div align="center">)

[//]: # (  <img src="https://via.placeholder.com/600x300?text=Customer+Support+Example" alt="Customer Support Example" width="70%"/>)

[//]: # (</div>)

### Internal Knowledge Management
Create an AI assistant that helps employees navigate internal documentation, answer questions about company policies, and assist with common tasks.

### Developer Assistant
Build a specialized assistant that can help with code reviews, documentation, and technical problem-solving.

### Research Assistant
Deploy an AI that can search through research papers, summarize findings, and assist with literature reviews.

## 👥 Community

Join our community to get help, share ideas, and contribute to the project:

- [Discord Server](https://discord.gg/ai_assistant_core)
- [GitHub Discussions](https://github.com/yourusername/ai_assistant_core/discussions)
- [Twitter](https://twitter.com/ai_assistant_coreai)

[//]: # (### Contributors)

[//]: # ()
[//]: # (<a href="https://github.com/yourusername/ai_assistant_core/graphs/contributors">)

[//]: # (  <img src="https://contrib.rocks/image?repo=yourusername/ai_assistant_core" />)

[//]: # (</a>)

## 📚 Documentation

- **[API Reference](https://docs.ai_assistant_coreai.com/api)**: Complete API documentation
- **[User Guide](https://docs.ai_assistant_coreai.com/guide)**: How to use ai_assistant_core
- **[Developer Guide](https://docs.ai_assistant_coreai.com/dev)**: How to extend ai_assistant_core
- **[Architecture](https://docs.ai_assistant_coreai.com/architecture)**: System design and components

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information
For any inquiries or support, please contact us at [support@ai_assistant_coreai.com](mailto:support@ai_assistant_coreai.com).

## Additional Resources
- **[API Reference](https://docs.ai_assistant_coreai.com/api)**: Complete API documentation
- **[User Guide](https://docs.ai_assistant_coreai.com/guide)**: How to use ai_assistant_core
- **[Developer Guide](https://docs.ai_assistant_coreai.com/dev)**: How to extend ai_assistant_core
- **[Architecture](https://docs.ai_assistant_coreai.com/architecture)**: System design and components

## Visuals
Include screenshots, diagrams, or GIFs to illustrate key features or usage.
