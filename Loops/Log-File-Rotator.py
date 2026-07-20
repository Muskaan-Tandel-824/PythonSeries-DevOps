import datetime
logs=("app.log","error.log","access.log")
today=datetime.date.today()

for i in logs:
    new_name=f"{i}_{today}.log"
    print(f"Renaming {i} → {new_name}")