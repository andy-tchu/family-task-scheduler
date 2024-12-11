# Family Task Scheduler

The Family Task Scheduler is a Python-based application using MongoDB to help multiple families organize and schedule their shared and individual tasks efficiently. It supports managing events like birthdays, medical appointments, recreational outings, and major shopping trips for various families while ensuring privacy and tailored scheduling for each. The system emphasizes scalability, user-friendliness, and collaborative task management.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/andy_tchu/family-task-scheduler.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables.
4. Run the application:
   ```bash
   gunicorn 'app:start_app()'
   ```

## Usage

The API is designed to be used with an HTTP client like [Postman](https://www.postman.com/) or [curl](https://curl.se/).
Exapmles for Postman in the [file](FTS.postman_collection.json).

## API Endpoints

### Users
- **Create user**  
  `POST /users` - Creates a new user.  
  **Body**: `{ "username": "User Name", "password": "Password123!", "telegram": "Telegram_nickname", "admin": "No" }`

- **Get All Users**  
  `GET /users` - Retrieves all users.

- **Get User by ID**  
  `GET /users/:id` - Retrieves an user by ID.

- **Update User**  
  `PUT /users/:id` - Updates an user by ID.  
  **Body**: `{ "password": "New_password123!", "telegram": "telegram_nickname" }`

- **Delete user**  
  `DELETE /users/:id` - Deletes an user by ID.

### Family
- **Create Family**  
  `POST /families` - Creates a new family.  
  **Body**: `{ "name": "Family Name" }`

- **Get All Families**  
  `GET /families` - Retrieves all families.

- **Get Family by ID**  
  `GET /families/:id` - Retrieves a family by ID.

- **Update Family**  
  `PUT /families/:id` - Updates a family by ID.  
  **Body**: `{ "name": "New Family Name" }`

- **Delete Family**  
  `DELETE /families/:id` - Deletes a family by ID.

### Members
- **Create Member**  
  `POST /members` - Creates a new member.  
  **Body**: `{ "name": "Member name", "phone": "777777777", "role": "adult", userId":"ffffffffffffffffffffffff", "familyId": "000000000000000000000000" }`

- **Get Member by ID**  
  `GET /member/:id` - Retrieves a member by ID.

- **Get all Family Members**  
  `GET /members/family/:familyId` - Retrieves all members of a specific family.

- **Update Member**  
  `PUT /member/:id` - Updates a member by ID.  
  **Body**: `{ "name": "New Member name", "phone": "777-777-7777", "role": "adult" }`

- **Delete Member**  
  `DELETE /members/:id` - Deletes a member by ID.

### Tasks
- **Create Task**  
  `POST /tasks` - Creates a new task.  
  **Body**: `{ "Title": "Task title", "Description": "Description of a task", "assignedTo": ["ffffffffffffffffffffffff"], familyId: "000000000000000000000000", dateTime: "2024-12-28T12:00:00.000Z", priority: "Hight", status: "pending", notes: "Some notes about a task"}`

- **Get All Tasks by User**  
  `GET /tasks/user/:id` - Retrieves all tasks assigned to user.

- **Get Task by ID**  
  `GET /tasks/:id` - Retrieves a task by ID.

- **Update Task**  
  `PUT /tasks/:id` - Updates a task by ID.  
  **Body**: `{ "Title": "Task title", "Description": "Description of a task", dateTime: "2024-12-28T12:00:00.000Z", priority: "Hight", status: "pending", notes: "Some notes about a task"}`

- **Delete Task**  
  `DELETE /tasks/:id` - Deletes a task by ID.

## Error Handling

Standardized error handling is implemented with appropriate HTTP status codes:
- `400 Bad Request` - for validation errors.
- `401 Invalid credentials` - for invalid credentioals errors.
- `402 Error validating the user` - for user validation errors.
- `403 Invalid token` - for JWT errors.
- `404 Not Found` - for resources not found.
- `500 Internal Server Error` - for server errors.

## Environment Variables

This project uses environment variables to configure database connection, server settings, and other sensitive data. Add the following in a `.env` file:

```plaintext
DATABASE_NAME=your_database_name
CLIENT_URL=*

SECRET_KEY=your_secret_key
DEBUG=True
PORT=5000
HOST=0.0.0.0
```

## Contributing

Contributions are welcome! Please create a pull request with a clear description of changes.

## License

This project is licensed under the MIT License.
