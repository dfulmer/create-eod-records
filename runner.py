from eodbib.eodbib import Eodbib

if __name__ == "__main__":
    with open("oomultifile.mrc", "wb") as out:
        for record in Eodbib().records(50):
            out.write(record.as_marc())
