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

## API Usage