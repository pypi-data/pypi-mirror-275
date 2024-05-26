# Contribution

## Development

#### Setup

1. Clone the repository
    ```shell
    git clone https://github.com/dldevinc/paper-admin-permission-field
    ```
1. Create a virtualenv
    ```shell
    cd paper-admin-permission-field
    virtualenv .venv
    ```
1. Activate virtualenv
    ```shell
    source .venv/bin/activate
    ```
1. Install dependencies as well as a local editable copy of the library

    ```shell
    pip install -r ./requirements.txt
    pip install -e .
    ```

1. Run test project

    ```shell
    python3 manage.py migrate
    python3 manage.py loaddata tests/fixtures.json
    ```

    ```shell
    python3 manage.py runserver
    ```

    > Django admin credentials: `admin` / `admin`




