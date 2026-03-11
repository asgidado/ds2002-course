import os
import pymongo

ATLAS_URL  = os.getenv("MONGODB_ATLAS_URL")
ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
ATLAS_PWD  = os.getenv("MONGODB_ATLAS_PWD")

def main():
    client = pymongo.MongoClient(
        ATLAS_URL,
        username=ATLAS_USER,
        password=ATLAS_PWD
    )

    db         = client["bookstore"]
    collection = db["authors"]

    total = collection.count_documents({})
    print("=" * 40)
    print(f"  BOOKSTORE AUTHOR REPORT")
    print(f"  Total authors: {total}")
    print("=" * 40)

    authors = collection.find({}, {"name": 1, "nationality": 1, "birthday": 1, "bio.short": 1, "_id": 0})

    for author in authors:
        print(f"\nName:        {author.get('name', 'N/A')}")
        print(f"Nationality: {author.get('nationality', 'N/A')}")
        print(f"Birthday:    {author.get('birthday', 'N/A')}")
        print(f"Bio:         {author.get('bio', {}).get('short', 'N/A')}")

    print("\n" + "=" * 40)
    client.close()

if __name__ == "__main__":
    main()
