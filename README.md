<div align="center">

# 🚀 Enterprise AI Suite

**A powerful, extensible AI platform with multi-LLM support**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

</div>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#features">Features</a> •
  <a href="#technical-stack">Technical Stack</a> •
  <a href="#installation">Installation</a> •
  <a href="#deployment">Deployment</a> •
  <a href="#community">Community</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

## 📚 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Installation](#installation)
- [Deployment](#deployment)
- [Configuration](#configuration)
- [Community](#community)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Documentation](#documentation)
- [FAQs](#faqs)
- [Security Considerations](#security-considerations)
- [Performance Tips](#performance-tips)

## 📋 Overview

Enterprise AI Suite is a robust, production-ready platform for building and deploying AI applications. It provides a flexible architecture for integrating multiple large language models (LLMs) and tools into a unified interface, enabling developers to create sophisticated AI solutions with features like conversation management, authentication, and monitoring out of the box.

| 🔑 Key Benefits | Description |
|----------------|-------------|
| 🔄 **Model Flexibility** | Switch between different AI models without changing your application code |
| 🔒 **Enterprise Security** | Built-in authentication, authorization, and data protection |
| 📈 **Scalability** | From prototype to production with the same codebase |
| 👨‍💻 **Developer Experience** | Comprehensive APIs and tools for rapid development |

## 🏗️ Architecture

Enterprise AI Suite follows a microservices architecture with three main components working together to provide a complete AI platform solution.

### 🧩 Core Components

1. **🧠 AI assistant Core Engine** (`ai-assistant-core/`): The central component that manages AI model interactions, conversation history, and tool integrations. It handles:
   - LLM provider integrations (OpenAI, Claude, Groq)
   - Conversation management and context handling
   - Thread summarization for managing context windows
   - API endpoints for client applications

2. **🔐 auth_rbac_service** (`auth_rbac_service/`): Authentication and authorization service that provides:
   - Team-based Role-Based Access Control (RBAC)
   - Integration with Clerk authentication service
   - Data source access management
   - User permission management

3. **⚙️ billing-payments-service** (`billing-payments-service/`): Feature management and subscription service that handles:
   - Feature flagging and management
   - Subscription handling via Paddle and Razorpay integration
   - User plan management
   - Feature access control

### 🔄 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Applications                     │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                        API Gateway                           │
└───────┬───────────────────┬───────────────────────┬─────────┘
        │                   │                       │
┌───────▼───────┐   ┌───────▼───────┐       ┌───────▼───────┐
│  AI assistant Core  │   │   auth_rbac_service   │       │     billing-payments-service     │
│    Engine     │   │  RBAC System  │       │  Feature Mgmt │
└───────┬───────┘   └───────────────┘       └───────────────┘
        │
┌───────▼───────────────────────────────────────────────────┐
│                    Model Connector Framework               │
└───────┬───────────────┬────────────────────┬──────────────┘
        │               │                    │
┌───────▼───────┐ ┌─────▼──────┐    ┌───────▼───────┐
│  OpenAI API   │ │ Claude API │    │   Groq API    │
└───────────────┘ └────────────┘    └───────────────┘
```

## 📁 Project Structure

### 🧠 AI assistant Core (`ai-assistant-core/`)

The core AI engine with the following structure:

```
ai-assistant-core/
├── config/          # Configuration files for different environments
├── utils/           # Utility functions and classes
├── mcp_configs/     # Multi-provider configuration management
├── wrapper/         # Model wrapper implementations
├── surface/         # Interface adapters
└── alembic/         # Database migration management
```

**Directory Details:**
- **`config/`**: Environment-specific configuration files (local, docker, production, SIT)
- **`utils/`**: Common utility functions including message transformation and custom exceptions
- **`mcp_configs/`**: MCP model definitions and API endpoints for configuration
- **`wrapper/`**: LLM model configuration and wrapper implementations
- **`surface/`**: Interface adapters and utility functions for API versions
- **`alembic/`**: Database migration scripts and environment configuration

### 🔐 auth_rbac_service (`auth_rbac_service/`)

Authentication and authorization service:

```
auth_rbac_service/
├── config/          # Environment-specific configurations
├── RBAC/            # Role-Based Access Control implementation
│   ├── teams/       # Team management
│   ├── roles/       # Role definitions and permissions
│   └── datasources/ # Data source access management
├── app/             # Application code
└── alembic/         # Database migration management
```

**Directory Details:**
- **`config/`**: Local and docker deployment configuration settings
- **`RBAC/`**: Complete Role-Based Access Control system with team, role, and data source management
- **`app/`**: FastAPI application setup and core application logic
- **`alembic/`**: Database migration scripts and environment configuration

### ⚙️ billing-payments-service (`billing-payments-service/`)

Feature and subscription management:

```
billing-payments-service/
├── config/          # Configuration files
├── features/        # Feature management
├── plans/           # Subscription plan management
├── invoices/        # Invoice management
├── app/             # Application code
└── alembic/         # Database migration management
```

**Directory Details:**
- **`config/`**: Local and docker deployment configuration settings
- **`features/`**: Feature data models and feature-specific exceptions
- **`plans/`**: Subscription plan data models and plan-related exceptions
- **`invoices/`**: Invoice data models and invoice management logic
- **`app/`**: FastAPI application setup and core application logic
- **`alembic/`**: Database migration scripts and environment configuration

## ✨ Features

### 🤖 Multi-LLM Integration
- **OpenAI Models**: Full support for GPT-4 and other OpenAI models
- **Anthropic Claude**: Integration with Claude models
- **Groq Support**: High-performance inference with Groq's LLM API
- **Model Switching**: Seamlessly switch between different models within the same application

### 💬 Conversation Management
- **Thread History**: Persistent conversation threads with full history
- **Context Management**: Sophisticated handling of context windows for different models

### 🔒 Security & Authentication
- **Clerk Integration**: Secure user authentication and management
- **API Key Management**: Secure storage and rotation of LLM provider API keys
- **Role-Based Access**: Control access to features based on user roles

### 💰 Subscription Management
- **Plan Management**: Create and manage subscription plans
- **Payment Integration**: Support for Razorpay and Paddle payment processors
- **Feature Access Control**: Control feature access based on subscription level

### 🚀 Deployment & Scaling
- **Docker Support**: Containerized deployment for consistency across environments
- **Kubernetes Ready**: Configurations for deploying on Kubernetes clusters
- **Database Integration**: PostgreSQL for persistent storage of conversations and settings
- **Redis Support**: Optional caching and rate limiting with Redis

## 🛠️ Technical Stack

Enterprise AI Suite is built on a modern technology stack designed for performance, reliability, and developer productivity:

| Category | Technologies |
|----------|-------------|
| 🐍 **Backend** | Python 3.10+, FastAPI, SQLAlchemy, Pydantic, Alembic |
| 🗄️ **Databases** | PostgreSQL, Redis |
| 🏗️ **Infrastructure** | Docker, Kubernetes, Sentry, Structlog |
| 🧠 **AI Integration** | OpenAI API, Anthropic API, Groq API |
| 🔐 **Security** | Clerk, RBAC, API Key Management |
| 💳 **Payment Processing** | Razorpay, Paddle |

## 📥 Installation

### Prerequisites

- **Python 3.10+**: Required for running the application
- **PostgreSQL**: Database for storing conversations, user data, and settings
- **Redis** (optional): For caching and rate limiting
- **Docker** (optional): For containerized deployment
- **Kubernetes** (optional): For orchestrated deployment

### Quick Start (Docker)

The fastest way to get started is with Docker Compose:

```bash
docker-compose up -d
```

This will start:
- AI assistant Core on port 8081
- auth_rbac_service on port 8082
- billing-payments-service on port 8083

Then visit `http://localhost:8081` in your browser.

### Manual Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Uttam1728/enterprise-ai-suite.git
   cd enterprise-ai-suite
   ```

2. **Install dependencies for all services**
   ```bash
   # Install AI assistant Core dependencies
   pip install -r ai-assistant-core/requirements/requirements.txt
   
   # Install auth_rbac_service dependencies
   pip install -r auth-rbac-service/requirements/requirements.txt
   
   # Install billing-payments-service dependencies
   pip install -r billing-payments-service/requirements/requirements.txt
   ```

3. **Create local configuration files**
   ```bash
   # AI assistant Core configuration
   cp ai-assistant-core/config/default.local.tmp.yaml ai-assistant-core/config/default.local.yaml
   
   # auth_rbac_service configuration
   cp auth-rbac-service/config/default.local.tmp.yaml auth-rbac-service/config/default.local.yaml
   
   # billing-payments-service configuration
   cp billing-payments-service/config/default.local.tmp.yaml billing-payments-service/config/default.local.yaml
   ```

4. **Update the configurations**
   
   Edit each configuration file with your:
   - API keys for OpenAI, Claude, and Groq
   - Database connection strings
   - Authentication settings
   - Other environment-specific configurations

5. **Database Setup for each service**

   ```bash
   # AI assistant Core setup
   cd ai-assistant-core
   python startup.py --all
   cd ..
   
   # auth_rbac_service setup
   cd auth-rbac-service
   python startup.py --all
   cd ..
   
   # billing-payments-service setup
   cd billing-payments-service
   python startup.py --all
   cd ..
   ```

6. **Start all services (in separate terminal windows)**

   ```bash
   # Terminal 1: Start AI assistant Core
   cd ai-assistant-core
   python entrypoint.py
   
   # Terminal 2: Start auth_rbac_service
   cd auth-rbac-service
   python entrypoint.py
   
   # Terminal 3: Start billing-payments-service
   cd billing-payments-service
   python entrypoint.py
   ```

   The services will be available at:
   - AI assistant Core: http://localhost:8081
   - auth_rbac_service: http://localhost:8082
   - billing-payments-service: http://localhost:8083

> **💡 Tip:** For development environments, use the `--debug` flag when starting each service to enable hot reloading and detailed error messages.

# Docker Compose Setup

This project uses Docker Compose to manage multiple services. You can control which services to start using Docker Compose profiles.

## Starting Services with Profiles

To start specific services, use the `--profile` option with `docker-compose up`. Here are some examples:

- **Start only the ai-assistant-core service:**
  ```bash
  docker-compose --profile ai-assistant-core up
  ```

- **Start the AI assistant Core and auth_rbac_service services:**
  ```bash
  docker-compose --profile ai-assistant-core --profile auth-rbac-service up
  ```

- **Start all services:**
  ```bash
  docker-compose up
  ```

## Managing Dependencies

- The `ai-assistant-core` service depends on the `auth_rbac_service` service. Ensure to include the `auth_rbac_service` profile when starting `ai-assistant-core`.

- If you encounter dependency issues, make sure all required services are included in the profiles you start.

## Configuration

Configuration for each service can be found in the `service-config.yaml` file. Update this file with specific configuration details as needed.

---
## 🚢 Deployment

### 🐳 Docker Deployment

#### Using Docker Compose

The recommended way to deploy Enterprise AI Suite is with Docker Compose:

```bash
docker-compose up -d
```

This will start all services with the proper configurations and dependencies.

#### Building Individual Images

You can also build and run individual Docker images:

```bash
# Build AI assistant Core
docker build -t ai-assistant-core ./ai-assistant-core

# Build auth_rbac_service
docker build -t auth-rbac-service ./auth-rbac-service

# Build billing-payments-service
docker build -t billing-payments-service ./billing-payments-service

# Run AI assistant Core
docker run -p 8081:8081 \
  -e ENVIRONMENT=prod \
  -e OPENAI_KEY=your_openai_key \
  -e CLAUDE_KEY=your_claude_key \
  -e DB_URL=your_database_url \
  ai-assistant-core
```

### ☸️ Kubernetes Deployment

Enterprise AI Suite includes Kubernetes deployment configurations for production environments:

1. **Apply the configuration**:
   ```bash
   kubectl apply -f k8s/deployment.yaml
   ```

2. **Set up secrets**:
   ```bash
   kubectl create secret generic enterprise-ai-secrets \
     --from-literal=OPENAI_KEY=your_openai_key \
     --from-literal=CLAUDE_KEY=your_claude_key \
     --from-literal=DB_URL=your_database_url
   ```

3. **Access the service**:
   ```bash
   kubectl port-forward svc/ai-assistant-core 8081:80
   ```

### 🔄 CI/CD Pipeline

Enterprise AI Suite includes Azure Pipelines configuration for continuous integration and deployment:

```bash
# Deploy using Azure Pipelines
git tag deploy.v1.0.0
git push origin deploy.v1.0.0
```

This will trigger the deployment pipeline defined in `ai-assistant-core/azure-pipelines.yml`.

## ⚙️ Configuration

The application uses a YAML-based configuration system with environment-specific files:

| Environment | Configuration File |
|-------------|-------------------|
| 💻 **Local Development** | `default.local.yaml` |
| 🐳 **Docker Environment** | `default.docker.yaml` |
| 🌐 **Production** | `default.prod.yaml` |
| 🧪 **System Integration Testing** | `default.sit.yaml` |

Key configuration parameters include:
- Database connection strings
- API keys for LLM providers
- Authentication settings (Clerk)
- Application ports and hosts
- Payment processor credentials (Razorpay, Paddle)

## 👥 Community

Join our community to get help, share ideas, and contribute to the project:

- 💬 [Discord Server](https://discord.gg/enterpriseai)
- 🗣️ [GitHub Discussions](https://github.com/yourusername/enterprise-ai-suite/discussions)
- 🐦 [Twitter](https://twitter.com/enterpriseai)

## 🤝 Contributing

Contributions are welcome! Please follow the standard GitHub workflow for contributing to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow the coding standards outlined in the `CONTRIBUTING.md` file.
- Ensure all new code is covered by tests.
- Adhere to the project's code of conduct.

## 📋 FAQs

- **How do I switch between different AI models?**
  - Use the configuration files to specify the desired model.

- **What should I do if I encounter a deployment issue?**
  - Check the logs for errors and consult the troubleshooting section.

## 🔒 Security Considerations

- Ensure all API keys and sensitive data are stored securely.
- Regularly update dependencies to patch security vulnerabilities.

## 🚀 Performance Tips

- Use caching strategies to improve response times.
- Optimize database queries for better performance.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📞 Contact

For support, contact [support@enterpriseaisuite.com](mailto:support@enterpriseaisuite.com).

## 📚 Documentation

- 📖 **API Reference**: Complete API documentation
- 📘 **User Guide**: How to use Enterprise AI Suite
- 📗 **Developer Guide**: How to extend Enterprise AI Suite
- 📙 **Architecture**: System design and components

---

Add more detailed instructions or configurations as necessary for your project setup.
