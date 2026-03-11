// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
  { "name": "Jane Austen" },
  { $set: { "birthday": "1775-12-16" } }
)

// Task 5: insert four more authors
db.authors.insertMany([
  {
    "name": "Charles Dickens",
    "nationality": "British",
    "birthday": "1812-02-07",
    "bio": {
      "short": "Victorian-era novelist known for vivid characters and social criticism.",
      "long": "Charles Dickens was an English writer and social critic who created some of the world's best-known fictional characters. His novels, including Oliver Twist, A Tale of Two Cities, and Great Expectations, highlight the struggles of the poor and the injustices of Victorian society."
    }
  },
  {
    "name": "Gabriel Garcia Marquez",
    "nationality": "Colombian",
    "birthday": "1927-03-06",
    "bio": {
      "short": "Colombian novelist and pioneer of magical realism.",
      "long": "Gabriel Garcia Marquez was a Colombian novelist, short-story writer, and journalist. He is best known for One Hundred Years of Solitude and Love in the Time of Cholera, and was awarded the Nobel Prize in Literature in 1982 for his works blending reality with myth and folklore."
    }
  },
  {
    "name": "Fyodor Dostoevsky",
    "nationality": "Russian",
    "birthday": "1821-11-11",
    "bio": {
      "short": "Russian novelist known for psychological depth and philosophical themes.",
      "long": "Fyodor Dostoevsky was a Russian novelist whose works explore human psychology, suffering, and morality. His major works include Crime and Punishment, The Brothers Karamazov, and The Idiot, which remain cornerstones of world literature and existentialist philosophy."
    }
  },
  {
    "name": "Toni Morrison",
    "nationality": "American",
    "birthday": "1931-02-18",
    "bio": {
      "short": "American novelist celebrated for her exploration of Black American experience.",
      "long": "Toni Morrison was an American novelist, essayist, and professor. Her novels, including Beloved, Song of Solomon, and The Bluest Eye, explore the African American experience with lyrical prose and emotional depth. She was awarded the Nobel Prize in Literature in 1993."
    }
  }
])

// Task 6: total count
db.authors.countDocuments()

// Task 7: British authors, sorted by name
db.authors.find({ "nationality": "British" }).sort({ "name": 1 })
