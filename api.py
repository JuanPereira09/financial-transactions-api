from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from services import (
    get_all_transactions,
    get_balance,
    get_reports,
    add_transaction,
    delete_transaction,
    update_transaction
)

app = FastAPI(title="Financial Transactions API")


# -------- MODELS --------
class TransactionCreate(BaseModel):
    description: str
    amount: float
    category: str
    type: str


class TransactionUpdate(BaseModel):
    description: str
    amount: float
    category: str
    type: str


# -------- ENDPOINTS --------
@app.get("/transactions")
def list_transactions(
    tx_type: str | None = Query(default=None, alias="type"),
    category: str | None = Query(default=None)
):
    return get_all_transactions(
        tx_type=tx_type,
        category=category
    )


@app.post("/transactions")
def create_transaction(tx: TransactionCreate):
    try:
        add_transaction(
            tx.description,
            tx.amount,
            tx.category,
            tx.type.upper()
        )
        return {"message": "Transaction created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/transactions/{transaction_id}")
def update_transaction_api(transaction_id: int, tx: TransactionUpdate):
    try:
        update_transaction(
            transaction_id,
            tx.description,
            tx.amount,
            tx.category,
            tx.type.upper()
        )
        return {"message": "Transaction updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/transactions/{transaction_id}")
def delete_transaction_api(transaction_id: int):
    try:
        delete_transaction(transaction_id)
        return {"message": "Transaction deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/balance")
def balance():
    return {"balance": get_balance()}

@app.get("/reports")
def reports():
    return get_reports()
