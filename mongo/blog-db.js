db = db.getSiblingDB('blog_db');

db.createCollection("posts", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["titre", "auteur", "vues"],
         properties: {
            titre: { bsonType: "string" },
            auteur: { bsonType: "string" },
            vues: { bsonType: "int" }
         }
      }
   }
});

db.posts.insertMany([
   { titre: "Administrer une base de donnée MongoDB", auteur: "Admin", vues: NumberInt(10) },
   { titre: "Comment Pull MongoDB", auteur: "Jean", vues: NumberInt(25) },
   { titre: "Comment Run MongoDB", auteur: "Alice", vues: NumberInt(5) },
   { titre: "Apprendre a utiliser MongoDB", auteur: "Bob", vues: NumberInt(100) },
   { titre: "Tout savoir sur MongoDB", auteur: "Eve", vues: NumberInt(42) }
]);
