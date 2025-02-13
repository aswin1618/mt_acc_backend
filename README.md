## Setup

1. **Clone Repository**
    ```sh
    git clone https://github.com/aswin1618/mt_csv_upload.git
    ```

2. **Setup virtual environment and install dependencies**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Run DB migrations**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

## API Usage Endpoints

→ List all employees.
```sh
GET /api/employees/ 
```

→ Create a new employee.
```sh
POST /api/employees/
```
Content-Type: application/json
example json
```json
{
    "name": "John Doe",
    "position": "Software Engineer",
    "salary": "75000.00",
    "age": 24
}
```

→ Retrieve an employee.
```sh
GET /api/employees/<id>/
```

→ Update an employee.
```sh
PATCH /api/employees/<id>/ 
```
example json
```json
{
    "position": "Senior Software Engineer"
}
```

→ Delete an employee.
```sh
DELETE /api/employees/<id>/
```