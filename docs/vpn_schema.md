# VPN User Schema

Each VPN user represents a WireGuard client.

## Fields
- user_id: Unique identifier
- username: VPN username
- public_key: WireGuard public key
- private_key: WireGuard private key
- ip_address: Assigned VPN IP
- role: Admin / Client
- status: Active / Revoked
- created_at: Creation timestamp

## Purpose
This schema is used to:
- Automate VPN configuration
- Track VPN users
- Revoke or regenerate access
