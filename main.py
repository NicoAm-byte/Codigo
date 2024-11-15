from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()
app.title="fastAPI SENA"
app.version="2.0.0"
security = HTTPBasic()
fake_db = {"1": "Alice" "alice@gmai.com" "patata", "2": "Bob"  "bob@gmai.com" "patato", "3": "Charlie"  "charlie@gmai.com" "patata"}

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if credentials.username == correct_username and credentials.password == correct_password:
        return credentials.username
    else:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


class User(BaseModel):
    username: str
    email: str
    contraseña: str

            
            
@app.get("/", tags=["casita"], response_class=HTMLResponse)
def casita():
    return """
    <html>
        <head>
            <title>Home Page</title>
        </head>
        <body>
            <h1 align="center">Hola SENA wao</h1>
        </body>
    </html>
    """


@app.post("/create", tags=["Account"])
def create_account(user: User):
    return {"message": "Cuenta creada exitosamente", "user": user}

class UserUpdate(BaseModel):
    username: str
    email: str


# Ruta PUT para actualizar la cuenta de un usuario
@app.put("/update_account/{user_id}", tags=["Account"])
def update_account(user_id: int, user: UserUpdate):
    return {
        "message": "Cuenta actualizada exitosamente",
    }



# Ruta DELETE para eliminar un usuario
@app.delete("/delete/{user_id}", tags=["Users"])
def delete_user(user_id: str):
    if user_id in fake_db:
        del fake_db[user_id]
        return {"message": f"Usuario con ID {user_id} eliminado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

#se debe cambiar el puerto por seguridad
#get, get{id}, post, put, delete