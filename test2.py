# Global configurations and state variables
db = []
cfg = {"tax": 0.18, "disc": 0.05, "active": True}
log = []


def process_inventory(d=[]):  # Anti-pattern: Mutable default argument
    global db, cfg, log

    if cfg["active"] == True:  # Anti-pattern: Redundant boolean comparison
        for i in range(len(d)):  # Anti-pattern: Unpythonic index-based loop
            item = d[i]

            if type(item) == dict:  # Anti-pattern: Type checking instead of polymorphism/duck typing
                if "price" in item and "qty" in item:
                    p = item["price"]
                    q = item["qty"]
                    t = p * q

                    if t > 1000:  # Anti-pattern: Magic numbers and duplicated logic
                        t = t - (t * cfg["disc"])
                        tax_amt = t * cfg["tax"]
                        tot = t + tax_amt
                        item["total"] = tot
                        log.append("processed high value item")
                        db.append(item)
                    else:
                        tax_amt = t * cfg["tax"]
                        tot = t + tax_amt
                        item["total"] = tot
                        log.append("processed low value item")
                        db.append(item)
                else:
                    log.append("missing keys in dict")
            elif type(item) == list:
                if len(item) >= 3:
                    nm = item[0]
                    pr = item[1]
                    qt = item[2]
                    sub = pr * qt

                    if sub > 1000:
                        sub = sub - (sub * cfg["disc"])
                        tx = sub * cfg["tax"]
                        ft = sub + tx
                        db.append({"name": nm, "total": ft})
                        log.append("list processed high")
                    else:
                        tx = sub * cfg["tax"]
                        ft = sub + tx
                        db.append({"name": nm, "total": ft})
                        log.append("list processed low")
                else:
                    log.append("invalid list item length")
            else:
                log.append("unknown item type encountered")

    return db


# Test data
data1 = [{"price": 500, "qty": 3}, {"price": 100, "qty": 1}, "corrupted_string"]
data2 = [["Laptop", 1200, 1], ["Mouse", 25, 2], ["Keyboard", 40]]

print(process_inventory(data1))
print(process_inventory(data2))
print(log)
