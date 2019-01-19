import sqlite3


def main():
    db = sqlite3.connect("dataBase/login.db")
    db.execute("create table if not exists USERS(Name text not null, PassWord text, Status text)")
    db.execute("insert into USERS (Name, PassWord, Status) values(?,?,?)", ("Admin", "saida21051986", "admin"))
    db.commit()
    db.row_factory = sqlite3.Row
    """
    db.execute("insert into Admin (Name,Age) values (?,?)", ("Otmane DAOU", 32))
    db.execute("insert into Admin (Name,Age) values (?,?)", ("Omar DAOU", 65))
    #db.commit() #execute the block of code in all
    #db.execute("delete from Admin where Name='Omar DAOU'")
    db.execute("Update Admin set Age=64 where Name='Omar DAOU'")
    cursor = db.execute("select * from Admin")
    for row in cursor:
        print("Name: {} / Age: {}".format(row["Name"], row["Age"]))
    """

    db.close()

if __name__ == '__main__':
    main()
