from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title= "HI!",
    discription = "Again api here",
    version= "2.0"
)
@app.get("/")
def read_root():
    return("messege : HI! welcome home.")
@app.get("/HI/{name}")
def read_items(name = str):
    return{f"HI {name}"}

if __name__ == "__main__":
    uvicorn.run(messege = "HI!",host="127.0.0",port=0000,reload=True)