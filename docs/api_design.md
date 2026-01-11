# API Design

## POST /vpn/create-user
Creates a new VPN user.

### Input
- username
- role

### Output
- user_id
- assigned_ip
- public_key

---

## GET /vpn/generate-config/{user_id}
Generates WireGuard client configuration.

### Output
- .conf file content

---

## POST /vpn/revoke-user
Disables VPN access.

### Input
- user_id

### Output
- status
