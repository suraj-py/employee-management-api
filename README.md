
# Employee Management API

Develop an RESTfull API for managing employee records at your company.The API is build using FastAPI, SQLAlchemy and, PostgreSQL.


## API Reference

**Authentication Routes**
| Method    | Route               | Functionality                     | Access    |
| :-------- | :-------------------| :-------------------------------- |:----------|
| `POST`    | `/company/register` | Register a new user               | Admin     |
| `POST`    | `/company/login`    | User login                        | All Users |
| `GET`     | `/company/user`     | Get user details of single user   | User      |

**Managers Routes**
| Method    | Route                                    | Functionality                                                  | Access        |
| :-------- | :----------------------------------------| :--------------------------------------------------------------|:--------------|
| `POST`    | `/companies/manager`                     | Create new manager                                             | Admin         |
| `Get`     | `/companies/managers/all`                | Get list of all managers                                       | Admin         |
| `GET`     | `/companies/managers/{company_id}`       | Get detail's of single manager(*manager's company id required*)| Admin, Manager|
| `PUT`     | `/companies/managers/{manager_id}/update`| Update single manager(*manager's company id required*)         | Admin         |
| `DELETE`  | `/companies/managers/{company_id}/delete`| Delete single manager(*manager's company id required*)         | Admin         |

**Employees Routes**
| Method    | Route                                     | Functionality                                                          | Access         |
| :-------- | :-----------------------------------------| :----------------------------------------------------------------------|:---------------|
| `POST`    | `/companies/employee`                     | Create new employee                                                    | Admin, Manager |
| `Get`     | `/companies/employees/all`                | Get list of all employee's                                             | Admin, Manager |
| `GET`     | `/companies/employees/{company_id}/all`   | Get list of all employee's by manager(*managers's company id required*)| Admin, Manager |
| `GET`     | `/companies/employees/{company_id}`       | Get detail's of single employee(*employee's company id required*)      | All Users      |
| `PUT`     | `/companies/employees/{manager_id}/update`| Update single employee(*employee's company id required*)               | Admin, Manager |
| `DELETE`  | `/companies/employees/{company_id}/delete`| Delete single employee(*employee's company id required*)               | Admin, Manager |

## Run Locally

Create virtual environment

```bash
  pipenv shell
```

Clone the project

```bash
  git clone https://github.com/suraj-py/employee-management-api
```
Install dependencies

```bash
  pip install -r requirements.txt
```

Go to the project directory

```bash
  cd app
```

Create a postgres database and configure .env file

```code
DB_USER = YOUR POSTGRES USER
DB_PASS = YOUR POSTGRES PASSWORD
DB_HOST = "localhost"
DB_NAME = CREATED DATABASE NAME(example: EMPLOYEES)

SECRET_KEY = YOUR SECRET KEY
```
Generate SECRET KEY by typing below command and paste above

```bash
openssl rand -hex 32
```

Start the server

```bash
  uvicorn main:app --reload
```


## Useful resources
- (https://fastapi.tiangolo.com/)
- (https://medium.com/@kevinkoech265/jwt-authentication-in-fastapi-building-secure-apis-ce63f4164eb2)
- (https://dev.to/moadennagi/role-based-access-control-using-fastapi-h59)



