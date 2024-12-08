# Task Management System API Documentation

## Base URL
http://localhost:8000/api

## Authentication

### Login
POST /auth/login
Request:
- email: string
- password: string

Response:

json
{
"token": "string",
"user": {
"id": "string",
"email": "string",
"name": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
}
GET /auth/me
json
{
"id": "string",
"email": "string",
"name": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
POST /auth/logout
GET /tasks
json
{
"tasks": [
{
"id": "string",
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"createdBy": "string",
"locationId": "string",
"dueDate": "string (ISO date)",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)",
"comments": [
{
"id": "string",
"taskId": "string",
"userId": "string",
"content": "string",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)"
}
]
}
]
}
GET /tasks/:taskId
json
{
"id": "string",
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"createdBy": "string",
"locationId": "string",
"dueDate": "string (ISO date)",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)",
"comments": []
}
POST /tasks
json
{
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"locationId": "string",
"dueDate": "string (ISO date)"
}
PUT /tasks/:taskId
json
{
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"locationId": "string",
"dueDate": "string (ISO date)"
}
PATCH /tasks/:taskId/status
json
{
"status": "pending" | "in-progress" | "completed"
}
DELETE /tasks/:taskId
POST /tasks/:taskId/comments
json
{
"content": "string"
}
json
{
"id": "string",
"taskId": "string",
"userId": "string",
"content": "string",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)"
}
GET /users
json
{
"users": [
{
"id": "string",
"email": "string",
"name": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
]
}
POST /users
json
{
"email": "string",
"name": "string",
"password": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string"
}
PUT /users/:userId
json
{
"name": "string",
"email": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
DELETE /users/:userId
GET /locations
json
{
"locations": [
{
"id": "string",
"name": "string",
"address": "string"
}
]
}
POST /locations
json
{
"name": "string",
"address": "string"
}
PUT /locations/:locationId
json
{
"name": "string",
"address": "string"
}
DELETE /locations/:locationId
GET /roles
json
{
"roles": [
{
"id": "string",
"name": "string",
"permissions": ["string"]
}
]
}
PUT /roles/:roleId/permissions
json
{
"permissions": ["string"]
}
json
{
"error": {
"code": "string",
"message": "string",
"details": {}
}
}
Authorization: Bearer <token>
add this documentation in api-docs.md

I'll help you create the complete api-docs.md file:
http://localhost:8000/api
http
POST /auth/login
json
{
"email": "string",
"password": "string"
}
json
{
"token": "string",
"user": {
"id": "string",
"email": "string",
"name": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
}
http
GET /auth/me
json
{
"id": "string",
"email": "string",
"name": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
http
POST /auth/logout
http
GET /tasks
json
{
"tasks": [
{
"id": "string",
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"createdBy": "string",
"locationId": "string",
"dueDate": "string (ISO date)",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)",
"comments": [
{
"id": "string",
"taskId": "string",
"userId": "string",
"content": "string",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)"
}
]
}
]
}
http
GET /tasks/:taskId
http
POST /tasks
json
{
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"locationId": "string",
"dueDate": "string (ISO date)"
}
http
PUT /tasks/:taskId
json
{
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"locationId": "string",
"dueDate": "string (ISO date)"
}
http
PATCH /tasks/:taskId/status
json
{
"status": "pending" | "in-progress" | "completed"
}
http
DELETE /tasks/:taskId
http
POST /tasks/:taskId/comments
json
{
"content": "string"
}
json
{
"id": "string",
"taskId": "string",
"userId": "string",
"content": "string",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)"
}
http
GET /users
json
{
"users": [
{
"id": "string",
"email": "string",
"name": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
]
}
http
POST /users
json
{
"email": "string",
"name": "string",
"password": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string"
}
http
PUT /users/:userId
json
{
"name": "string",
"email": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
http
DELETE /users/:userId
http
GET /locations
json
{
"locations": [
{
"id": "string",
"name": "string",
"address": "string"
}
]
}
http
POST /locations
json
{
"name": "string",
"address": "string"
}
http
PUT /locations/:locationId
json
{
"name": "string",
"address": "string"
}
http
DELETE /locations/:locationId
http
GET /roles
json
{
"roles": [
{
"id": "string",
"name": "string",
"permissions": ["string"]
}
]
}
http
PUT /roles/:roleId/permissions
json
{
"permissions": ["string"]
}
json
{
"error": {
"code": "string",
"message": "string",
"details": {}
}
}
http
Authorization: Bearer <token>
json
{
"admin": {
"email": "admin@example.com",
"password": "any"
},
"manager": {
"email": "manager@example.com",
"password": "any"
},
"supervisor": {
"email": "supervisor@example.com",
"password": "any"
},
"employee": {
"email": "employee@example.com",
"password": "any"
}
}


### Get Current User
GET /auth/me
Response:
json
{
"id": "string",
"email": "string",
"name": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}

### Logout
POST /auth/logout
Response: 204 No Content

## Tasks

### Get All Tasks
GET /tasks
Response:
son
{
"tasks": [
{
"id": "string",
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"createdBy": "string",
"locationId": "string",
"dueDate": "string (ISO date)",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)",
"comments": [
{
"id": "string",
"taskId": "string",
"userId": "string",
"content": "string",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)"
}
]
}
]
}


### Get Task by ID
GET /tasks/:taskId
Response:
json
{
"id": "string",
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"createdBy": "string",
"locationId": "string",
"dueDate": "string (ISO date)",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)",
"comments": []
}


### Create Task
POST /tasks
Request:
json
{
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"locationId": "string",
"dueDate": "string (ISO date)"
}


Response: Created task object

### Update Task
PUT /tasks/:taskId
Request:
json
{
"title": "string",
"description": "string",
"status": "pending" | "in-progress" | "completed",
"priority": "low" | "medium" | "high",
"assignedTo": "string",
"locationId": "string",
"dueDate": "string (ISO date)"
}

Response: Updated task object

### Update Task Status
PATCH /tasks/:taskId/status
Request:
json
{
"status": "pending" | "in-progress" | "completed"
}

Response: Updated task object

### Delete Task
DELETE /tasks/:taskId
Response: 204 No Content

### Create Comment on Task
POST /tasks/:taskId/comments
Request:
json
{
"content": "string"
}

Response:
json
{
"id": "string",
"taskId": "string",
"userId": "string",
"content": "string",
"createdAt": "string (ISO date)",
"updatedAt": "string (ISO date)"
}


## Users

### Get All Users
GET /users
Response:
json
{
"users": [
{
"id": "string",
"email": "string",
"name": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}
]
}


### Create User
POST /users
Request:
json
{
"email": "string",
"name": "string",
"password": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string"
}

Response: Created user object

### Update User
PUT /users/:userId
Request:
json
{
"name": "string",
"email": "string",
"role": "admin" | "manager" | "supervisor" | "employee",
"locationId": "string",
"isActive": boolean
}

Response: Updated user object

### Delete User
DELETE /users/:userId
Response: 204 No Content

## Locations

### Get All Locations
GET /locations
Response:
json
{
"locations": [
{
"id": "string",
"name": "string",
"address": "string"
}
]
}


### Create Location
POST /locations
Request:
json
{
"name": "string",
"address": "string"
}

Response: Created location object

### Update Location
PUT /locations/:locationId
Request:
json
{
"name": "string",
"address": "string"
}

Response: Updated location object

### Delete Location
DELETE /locations/:locationId
Response: 204 No Content

## Roles and Permissions

### Get All Roles
GET /roles
Response:
json
{
"roles": [

{
"id": "string",
"name": "string",
"permissions": ["string"]
}
]
}


### Update Role Permissions
PUT /roles/:roleId/permissions
Request:
json
{
"permissions": ["string"]
}

Response: Updated role object

## Error Responses
All endpoints may return these error responses:
json
{
"error": {
"code": "string",
"message": "string",
"details": {}
}
}


Common HTTP Status Codes:
- 200: Success
- 201: Created
- 204: No Content
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Unprocessable Entity
- 500: Internal Server Error

## Authentication
All endpoints except `/auth/login` require a Bearer token in the Authorization header:

```
Authorization: Bearer <token>
This documentation provides:
1. All API endpoints
2. Request/response payloads
3. Authentication requirements
4. Error handling
5. Status codes
6. Data types and formats

You can save this as `api-docs.md` in your project root for reference.