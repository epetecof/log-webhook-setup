## Test Locally

- Select the test folder

```bash
cd test
```

- Create venv 

```bash
python -m venv venv
```

- Activate venv

```bash
source venv/bin/activate
```

- Install packages

```bash
pip install -r requirements
```

- Setup environment variables: 

    - Copy example-env.txt to .env, fill in the credentials and source

    ```bash
    source .env
    ```

- Get an example JSON log from watsonx Assistant's Log Webhook and name it params.json

- Run 

```bash
python main_test.py params.json
```