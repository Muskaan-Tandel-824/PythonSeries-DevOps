resources={"EC2":"unused","s3":"used","load-balancer":"unused","security-grp":"unused"}
for name, status in resources.items():
    if status == "unused":
        print(f"Deleting {name}")

