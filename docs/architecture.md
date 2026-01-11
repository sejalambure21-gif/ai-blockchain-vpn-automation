# System Architecture

## Overview
The AI + Blockchain Based VPN Automation System is designed to provide
secure, automated, and intelligent VPN management using modern technologies.
The system removes manual VPN configuration and traditional password-based
authentication.

---

## Architecture Flow

User  
→ Web Dashboard (Admin Panel)  
→ Blockchain Authentication (MetaMask Wallet)  
→ FastAPI Backend  
→ VPN Automation Engine  
→ WireGuard VPN Server  

---

## Core Components

### 1. Web Dashboard
- Used by admin to create and manage VPN users
- Allows downloading VPN configuration files
- Integrates with MetaMask for blockchain login

### 2. Blockchain Authentication
- Uses Ethereum smart contracts
- Stores wallet address and user role
- Enables password-less authentication using wallet signatures

### 3. Backend Server (FastAPI)
- Exposes REST APIs for VPN automation
- Communicates with blockchain for authentication
- Handles AI routing and security logic

### 4. VPN Automation Engine
- Automatically generates WireGuard keys
- Assigns IP addresses to VPN users
- Creates and manages VPN configuration files

### 5. WireGuard VPN Server
- Provides secure encrypted VPN tunnels
- Supports multiple VPN clients
- Ensures high performance and low latency

### 6. AI Routing & Security Module
- Selects best VPN server based on latency and load
- Detects abnormal traffic using threshold-based logic
- Triggers alerts for suspicious activity

### 7. Monitoring & Backup
- Monitors CPU, RAM, and VPN traffic
- Displays metrics using Grafana dashboards
- Performs automated backups using cron jobs

---

## Key Benefits
- Fully automated VPN user management
- High security using blockchain authentication
- Improved performance using AI-based routing
- Scalable and cloud-ready architecture
