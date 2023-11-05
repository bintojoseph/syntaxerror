from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset (replace with your data)
food_data = [{
  
  "Food Product": "Almond Cookies",
  "Main Ingredient": "Almonds",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Flour",
  "Allergens": "Almonds, Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
 
  "Food Product": "Chicken Noodle Soup",
  "Main Ingredient": "Chicken broth",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Salt",
  "Allergens": "Chicken, Wheat, Celery",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47759"
  },
  "Food Product": "Cheddar Cheese",
  "Main Ingredient": "Cheese",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Salt",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4775a"
  },
  "Food Product": "Ranch Dressing",
  "Main Ingredient": "Buttermilk",
  "Sweetener": "Sugar",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Garlic, herbs",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4775b"
  },
  "Food Product": "Caramel Popcorn",
  "Main Ingredient": "Popcorn",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Salt",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4775c"
  },
  "Food Product": "Caesar Salad",
  "Main Ingredient": "Romaine lettuce",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Parmesan cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4775d"
  },
  "Food Product": "Caesar Wrap",
  "Main Ingredient": "Grilled chicken",
  "Sweetener": "None",
  "Fat/Oil": "Caesar dressing",
  "Seasoning": "Lettuce, Parmesan cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4775e"
  },
  "Food Product": "Strawberry Smoothie",
  "Main Ingredient": "Strawberries",
  "Sweetener": "Honey",
  "Fat/Oil": "Yogurt (milk, cultures)",
  "Seasoning": "None",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4775f"
  },
  "Food Product": "Cheese Pizza",
  "Main Ingredient": "Cheese",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Tomato sauce",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47760"
  },
  "Food Product": "Margherita Pizza",
  "Main Ingredient": "Cheese",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Tomato sauce, basil",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47761"
  },
  "Food Product": "Mashed Potatoes",
  "Main Ingredient": "Potatoes",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Salt, Pepper",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47762"
  },
  "Food Product": "Greek Yogurt",
  "Main Ingredient": "Yogurt (milk, cultures)",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "None",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47763"
  },
  "Food Product": "Caesar Salad Wrap",
  "Main Ingredient": "Grilled chicken",
  "Sweetener": "None",
  "Fat/Oil": "Caesar dressing",
  "Seasoning": "Lettuce, Parmesan cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47764"
  },
  "Food Product": "Caprese Salad",
  "Main Ingredient": "Tomatoes",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Mozzarella cheese, basil",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47765"
  },
  "Food Product": "Berry Smoothie",
  "Main Ingredient": "Mixed berries",
  "Sweetener": "Sugar",
  "Fat/Oil": "Yogurt (milk, cultures)",
  "Seasoning": "None",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47766"
  },
  "Food Product": "Caesar Salad",
  "Main Ingredient": "Romaine lettuce",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Caesar dressing",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47767"
  },
  "Food Product": "Berry Parfait",
  "Main Ingredient": "Mixed berries",
  "Sweetener": "Sugar",
  "Fat/Oil": "Yogurt (milk, cultures)",
  "Seasoning": "Granola",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47768"
  },
  "Food Product": "Chicken Alfredo",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Cream, Parmesan cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47769"
  },
  "Food Product": "Pesto Pizza",
  "Main Ingredient": "Pesto sauce",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Mozzarella cheese, basil",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4776a"
  },
  "Food Product": "Beef Stroganoff",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Sour cream",
  "Seasoning": "Mushroom, onion",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4776b"
  },
  "Food Product": "Banana Smoothie",
  "Main Ingredient": "Bananas",
  "Sweetener": "Honey",
  "Fat/Oil": "Yogurt (milk, cultures)",
  "Seasoning": "None",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4776c"
  },
  "Food Product": "Watermelon Salad",
  "Main Ingredient": "Watermelon",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Feta cheese, mint",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4776d"
  },
  "Food Product": "Chicken Parmesan",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Bread crumbs, Parmesan cheese",
  "Seasoning": "Marinara sauce",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4776e"
  },
  "Food Product": "Mango Lassi",
  "Main Ingredient": "Mango",
  "Sweetener": "Sugar",
  "Fat/Oil": "Yogurt (milk, cultures)",
  "Seasoning": "Cardamom",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4776f"
  },
  "Food Product": "Greek Salad",
  "Main Ingredient": "Cucumbers",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Feta cheese, olives",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47770"
  },
  "Food Product": "Butternut Squash Soup",
  "Main Ingredient": "Butternut squash",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Vegetable broth",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47771"
  },
  "Food Product": "Margherita Pasta",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Fresh tomatoes, mozzarella",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47772"
  },
  "Food Product": "Greek Gyro Wrap",
  "Main Ingredient": "Lamb",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Tzatziki sauce, tomatoes, onions",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47773"
  },
  "Food Product": "Spinach and Feta Stuffed Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Spinach, feta cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47774"
  },
  "Food Product": "Chicken Fettuccine Alfredo",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Cream, Parmesan cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47775"
  },
  "Food Product": "Caprese Sandwich",
  "Main Ingredient": "Tomatoes",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Mozzarella cheese, basil",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47776"
  },
  "Food Product": "Mushroom Risotto",
  "Main Ingredient": "Mushrooms",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Arborio rice, Parmesan cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47777"
  },
  "Food Product": "Greek Yogurt Parfait",
  "Main Ingredient": "Greek yogurt",
  "Sweetener": "Honey",
  "Fat/Oil": "None",
  "Seasoning": "Granola, mixed berries",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47778"
  },
  "Food Product": "Eggplant Parmesan",
  "Main Ingredient": "Eggplant",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Marinara sauce, cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47779"
  },
  "Food Product": "Banana Pudding",
  "Main Ingredient": "Bananas",
  "Sweetener": "Sugar",
  "Fat/Oil": "Milk",
  "Seasoning": "Vanilla pudding mix, cookies",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4777a"
  },
  "Food Product": "Margherita Pizza",
  "Main Ingredient": "Pizza dough",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Mozzarella cheese, tomatoes, basil",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4777b"
  },
  "Food Product": "Chicken Caesar Wrap",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Caesar dressing",
  "Seasoning": "Romaine lettuce, Parmesan cheese",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4777c"
  },
  "Food Product": "Greek Spanakopita",
  "Main Ingredient": "Spinach",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Feta cheese, phyllo dough",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4777d"
  },
  "Food Product": "Mushroom Soup",
  "Main Ingredient": "Mushrooms",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Vegetable broth",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4777e"
  },
  "Food Product": "Greek Yogurt",
  "Main Ingredient": "Yogurt (milk, cultures)",
  "Sweetener": "Honey",
  "Fat/Oil": "None",
  "Seasoning": "None",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4777f"
  },
  "Food Product": "Spinach Artichoke Dip",
  "Main Ingredient": "Spinach",
  "Sweetener": "None",
  "Fat/Oil": "Cream cheese, sour cream",
  "Seasoning": "Parmesan cheese, garlic",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47780"
  },
  "Food Product": "Chocolate Mousse",
  "Main Ingredient": "Chocolate",
  "Sweetener": "Sugar",
  "Fat/Oil": "Heavy cream",
  "Seasoning": "Vanilla extract",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47781"
  },
  "Food Product": "Stuffed Portobello Mushrooms",
  "Main Ingredient": "Portobello mushrooms",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Cheese, breadcrumbs",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47782"
  },
  "Food Product": "Tandoori Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Yogurt",
  "Seasoning": "Tandoori spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47783"
  },
  "Food Product": "Beef Stroganoff",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Sour cream",
  "Seasoning": "Mushrooms, onions",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47784"
  },
  "Food Product": "Strawberry Smoothie",
  "Main Ingredient": "Strawberries",
  "Sweetener": "Sugar",
  "Fat/Oil": "Yogurt",
  "Seasoning": "Milk",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47785"
  },
  "Food Product": "Baked Garlic Parmesan Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Parmesan cheese, garlic",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47786"
  },
  "Food Product": "Mushroom and Goat Cheese Flatbread",
  "Main Ingredient": "Mushrooms",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Goat cheese, herbs",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47787"
  },
  "Food Product": "Margherita Pasta",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Mozzarella cheese, tomatoes, basil",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47788"
  },
  "Food Product": "Pumpkin Soup",
  "Main Ingredient": "Pumpkin",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Nutmeg, cream",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47789"
  },
  "Food Product": "Butternut Squash Soup",
  "Main Ingredient": "Butternut squash",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Nutmeg, cream",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4778a"
  },
  "Food Product": "Caprese Skewers",
  "Main Ingredient": "Tomatoes",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Mozzarella cheese, basil",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4778b"
  },
  "Food Product": "Chicken Piccata",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Lemon, capers",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4778c"
  },
  "Food Product": "Berry Parfait",
  "Main Ingredient": "Berries",
  "Sweetener": "Honey",
  "Fat/Oil": "Yogurt",
  "Seasoning": "Granola",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4778d"
  },
  "Food Product": "Stuffed Mushrooms",
  "Main Ingredient": "Mushrooms",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Cheese, breadcrumbs",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4778e"
  },
  "Food Product": "Butter Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Tomato sauce, cream",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4778f"
  },
  "Food Product": "Palak Paneer",
  "Main Ingredient": "Spinach",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Paneer, spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47790"
  },
  "Food Product": "Rogan Josh",
  "Main Ingredient": "Lamb",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Yogurt, Kashmiri red chili",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47791"
  },
  "Food Product": "Paneer Tikka",
  "Main Ingredient": "Paneer",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Tikka masala, spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47792"
  },
  "Food Product": "Dal Makhani",
  "Main Ingredient": "Lentils",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Cream, spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47793"
  },
  "Food Product": "Malai Kofta",
  "Main Ingredient": "Cottage cheese",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Creamy tomato sauce",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47794"
  },
  "Food Product": "Chicken Tikka Masala",
  "Main Ingredient": "Chicken",
  "Sweetener": "Sugar",
  "Fat/Oil": "Ghee",
  "Seasoning": "Tomato sauce, cream",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47795"
  },
  "Food Product": "Gulab Jamun",
  "Main Ingredient": "Milk solids",
  "Sweetener": "Sugar",
  "Fat/Oil": "Ghee",
  "Seasoning": "Cardamom syrup",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47796"
  },
  "Food Product": "Chicken Korma",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Creamy sauce, spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47797"
  },
  "Food Product": "Malai Chicken Tikka",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Cream",
  "Seasoning": "Spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47798"
  },
  "Food Product": "Dahi Vada",
  "Main Ingredient": "Lentil dumplings",
  "Sweetener": "None",
  "Fat/Oil": "Yogurt",
  "Seasoning": "Tamarind chutney, spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47799"
  },
  "Food Product": "Chicken Malai Tikka",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Cream",
  "Seasoning": "Spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4779a"
  },
  "Food Product": "Matar Paneer",
  "Main Ingredient": "Paneer",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Peas, spices",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4779b"
  },
  "Food Product": "Rasgulla",
  "Main Ingredient": "Paneer",
  "Sweetener": "Sugar",
  "Fat/Oil": "None",
  "Seasoning": "Rose water, syrup",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4779c"
  },
  "Food Product": "Rabri",
  "Main Ingredient": "Milk",
  "Sweetener": "Sugar",
  "Fat/Oil": "Ghee",
  "Seasoning": "Cardamom, nuts",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4779d"
  },
  "Food Product": "Kheer",
  "Main Ingredient": "Rice",
  "Sweetener": "Sugar",
  "Fat/Oil": "Ghee",
  "Seasoning": "Cardamom, nuts",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4779e"
  },
  "Food Product": "Rasmalai",
  "Main Ingredient": "Paneer",
  "Sweetener": "Sugar",
  "Fat/Oil": "Milk, Ghee",
  "Seasoning": "Cardamom, nuts",
  "Allergens": "Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4779f"
  },
  "Food Product": "Chicken Caesar Salad",
  "Main Ingredient": "Chicken breast",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Parmesan cheese",
  "Allergens": "Dairy, Anchovies",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a0"
  },
  "Food Product": "Chocolate Mousse",
  "Main Ingredient": "Chocolate",
  "Sweetener": "Sugar",
  "Fat/Oil": "Heavy cream",
  "Seasoning": "Vanilla extract",
  "Allergens": "Dairy, Cocoa",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a1"
  },
  "Food Product": "Quiche Lorraine",
  "Main Ingredient": "Bacon",
  "Sweetener": "None",
  "Fat/Oil": "Heavy cream",
  "Seasoning": "Cheese, eggs",
  "Allergens": "Dairy, Eggs",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a2"
  },
  "Food Product": "Chicken Piccata",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Lemon, capers",
  "Allergens": "Dairy, Fish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a3"
  },
  "Food Product": "Chicken Tikka Masala",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Tikka masala sauce",
  "Allergens": "Dairy, Ghee",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a4"
  },
  "Food Product": "Sweet Potato Casserole",
  "Main Ingredient": "Sweet potatoes",
  "Sweetener": "Brown sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon, nutmeg",
  "Allergens": "Dairy, Nuts",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a5"
  },
  "Food Product": "Baked Brie",
  "Main Ingredient": "Brie cheese",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Herbs, nuts",
  "Allergens": "Dairy, Nuts",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a6"
  },
  "Food Product": "French Onion Soup",
  "Main Ingredient": "Onions",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Beef broth, cheese, bread",
  "Allergens": "Dairy, Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a7"
  },
  "Food Product": "Greek Gyro",
  "Main Ingredient": "Lamb/Chicken",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Tzatziki sauce, vegetables",
  "Allergens": "Dairy, Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a8"
  },
  "Food Product": "Omelette",
  "Main Ingredient": "Eggs",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Salt, pepper",
  "Allergens": "Eggs",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477a9"
  },
  "Food Product": "Egg Salad",
  "Main Ingredient": "Eggs",
  "Sweetener": "Mayonnaise",
  "Fat/Oil": "None",
  "Seasoning": "Celery, onion",
  "Allergens": "Eggs",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477aa"
  },
  "Food Product": "Quiche",
  "Main Ingredient": "Eggs",
  "Sweetener": "None",
  "Fat/Oil": "Cheese",
  "Seasoning": "Vegetables",
  "Allergens": "Eggs, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ab"
  },
  "Food Product": "Egg Salad Sandwich",
  "Main Ingredient": "Eggs",
  "Sweetener": "Mayonnaise",
  "Fat/Oil": "None",
  "Seasoning": "Celery, mustard",
  "Allergens": "Eggs, Mustard",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ac"
  },
  "Food Product": "Egg Fried Rice",
  "Main Ingredient": "Eggs",
  "Sweetener": "None",
  "Fat/Oil": "Sesame oil",
  "Seasoning": "Soy sauce",
  "Allergens": "Eggs, Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ad"
  },
  "Food Product": "Fish Sticks",
  "Main Ingredient": "Fish fillets",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Salt",
  "Allergens": "Fish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ae"
  },
  "Food Product": "Baked Salmon",
  "Main Ingredient": "Salmon fillet",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon, herbs",
  "Allergens": "Fish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477af"
  },
  "Food Product": "Teriyaki Salmon",
  "Main Ingredient": "Salmon",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Teriyaki sauce",
  "Allergens": "Fish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b0"
  },
  "Food Product": "Baked Salmon",
  "Main Ingredient": "Salmon",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon, herbs",
  "Allergens": "Fish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b1"
  },
  "Food Product": "Lemon Dill Salmon",
  "Main Ingredient": "Salmon",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon, dill",
  "Allergens": "Fish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b2"
  },
  "Food Product": "Malabar Fish Curry",
  "Main Ingredient": "Fish",
  "Sweetener": "None",
  "Fat/Oil": "Coconut oil",
  "Seasoning": "Tamarind, spices",
  "Allergens": "Fish, Coconut",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b3"
  },
  "Food Product": "Baked Cod",
  "Main Ingredient": "Cod",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Lemon, herbs",
  "Allergens": "Fish, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b4"
  },
  "Food Product": "Tuna Sandwich",
  "Main Ingredient": "Tuna",
  "Sweetener": "Mayonnaise",
  "Fat/Oil": "None",
  "Seasoning": "Salt, Pepper",
  "Allergens": "Fish, Eggs",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b5"
  },
  "Food Product": "Tuna Salad",
  "Main Ingredient": "Tuna",
  "Sweetener": "Mayonnaise",
  "Fat/Oil": "None",
  "Seasoning": "Celery, onion",
  "Allergens": "Fish, Eggs",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b6"
  },
  "Food Product": "Sushi",
  "Main Ingredient": "Fish (salmon, tuna)",
  "Sweetener": "Rice vinegar",
  "Fat/Oil": "Sesame oil",
  "Seasoning": "Soy sauce",
  "Allergens": "Fish, Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b7"
  },
  "Food Product": "Teriyaki Salmon",
  "Main Ingredient": "Salmon fillet",
  "Sweetener": "Sugar",
  "Fat/Oil": "Soy sauce",
  "Seasoning": "Ginger, garlic",
  "Allergens": "Fish, Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b8"
  },
  "Food Product": "Sushi Bowl",
  "Main Ingredient": "Sushi rice",
  "Sweetener": "None",
  "Fat/Oil": "Soy sauce",
  "Seasoning": "Raw fish, vegetables",
  "Allergens": "Fish, Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477b9"
  },
  "Food Product": "Honey Soy Glazed Salmon",
  "Main Ingredient": "Salmon",
  "Sweetener": "Honey",
  "Fat/Oil": "Soy sauce",
  "Seasoning": "Garlic, ginger",
  "Allergens": "Fish, Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ba"
  },
  "Food Product": "Milk Chocolate",
  "Main Ingredient": "Sugar",
  "Sweetener": "Cocoa butter",
  "Fat/Oil": "Milk powder",
  "Seasoning": "Vanilla extract",
  "Allergens": "Milk",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477bb"
  },
  "Food Product": "Vanilla Ice Cream",
  "Main Ingredient": "Milk",
  "Sweetener": "Sugar",
  "Fat/Oil": "Cream",
  "Seasoning": "Vanilla extract",
  "Allergens": "Milk",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477bc"
  },
  "Food Product": "Vanilla Yogurt",
  "Main Ingredient": "Yogurt (milk, cultures)",
  "Sweetener": "Sugar",
  "Fat/Oil": "None",
  "Seasoning": "Vanilla extract",
  "Allergens": "Milk",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477bd"
  },
  "Food Product": "Strawberry Yogurt",
  "Main Ingredient": "Yogurt (milk, cultures)",
  "Sweetener": "Sugar",
  "Fat/Oil": "None",
  "Seasoning": "Pectin",
  "Allergens": "Milk, Strawberries",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477be"
  },
  "Food Product": "Tomato Soup",
  "Main Ingredient": "Tomatoes",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Salt, Sugar",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477bf"
  },
  "Food Product": "Apple",
  "Main Ingredient": "Apples",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "None",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c0"
  },
  "Food Product": "Orange Juice",
  "Main Ingredient": "Oranges",
  "Sweetener": "Sugar",
  "Fat/Oil": "None",
  "Seasoning": "None",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c1"
  },
  "Food Product": "Greek Salad",
  "Main Ingredient": "Cucumber",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c2"
  },
  "Food Product": "Spaghetti Bolognese",
  "Main Ingredient": "Ground beef",
  "Sweetener": "Sugar",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Tomato sauce",
  "Allergens": "None",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c3"
  },
  "Food Product": "Honey Mustard Chicken",
  "Main Ingredient": "Chicken breast",
  "Sweetener": "Honey",
  "Fat/Oil": "Mustard",
  "Seasoning": "Vegetable oil",
  "Allergens": "None",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c4"
  },
  "Food Product": "BBQ Ribs",
  "Main Ingredient": "Pork ribs",
  "Sweetener": "Brown sugar",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "BBQ sauce",
  "Allergens": "None",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c5"
  },
  "Food Product": "Quinoa Salad",
  "Main Ingredient": "Quinoa",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c6"
  },
  "Food Product": "Vegetable Stir-Fry",
  "Main Ingredient": "Mixed vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Soy sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c7"
  },
  "Food Product": "Beef Burger",
  "Main Ingredient": "Ground beef",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Salt, Pepper",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c8"
  },
  "Food Product": "French Fries",
  "Main Ingredient": "Potatoes",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Salt",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477c9"
  },
  "Food Product": "Lemonade",
  "Main Ingredient": "Lemon juice",
  "Sweetener": "Sugar",
  "Fat/Oil": "Water",
  "Seasoning": "None",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ca"
  },
  "Food Product": "Gazpacho",
  "Main Ingredient": "Tomatoes",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Garlic, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477cb"
  },
  "Food Product": "Beef Tacos",
  "Main Ingredient": "Ground beef",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Taco seasoning",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477cc"
  },
  "Food Product": "Lentil Soup",
  "Main Ingredient": "Lentils",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477cd"
  },
  "Food Product": "Chicken Curry",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Curry powder",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ce"
  },
  "Food Product": "Ratatouille",
  "Main Ingredient": "Eggplant",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Tomatoes",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477cf"
  },
  "Food Product": "Pesto Pasta",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Basil, garlic",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d0"
  },
  "Food Product": "Chicken Stir-Fry",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Soy sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d1"
  },
  "Food Product": "Veggie Burger",
  "Main Ingredient": "Mixed vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Seasonings",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d2"
  },
  "Food Product": "Vegetable Soup",
  "Main Ingredient": "Mixed vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Seasonings",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d3"
  },
  "Food Product": "Spinach Salad",
  "Main Ingredient": "Spinach",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Balsamic vinegar",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d4"
  },
  "Food Product": "Chicken Enchiladas",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Enchilada sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d5"
  },
  "Food Product": "Minestrone Soup",
  "Main Ingredient": "Vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Tomato broth",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d6"
  },
  "Food Product": "Salsa",
  "Main Ingredient": "Tomatoes",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Onion, cilantro",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d7"
  },
  "Food Product": "Lemon Garlic Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice, garlic",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d8"
  },
  "Food Product": "Pancetta Pasta",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Pancetta",
  "Seasoning": "Garlic, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477d9"
  },
  "Food Product": "Chicken Teriyaki",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Teriyaki sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477da"
  },
  "Food Product": "Spinach Stuffed Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Spinach, garlic",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477db"
  },
  "Food Product": "Coconut Curry",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Coconut milk",
  "Seasoning": "Curry paste",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477dc"
  },
  "Food Product": "Apple Cider",
  "Main Ingredient": "Apples",
  "Sweetener": "Sugar",
  "Fat/Oil": "None",
  "Seasoning": "Cinnamon",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477dd"
  },
  "Food Product": "Ratatouille",
  "Main Ingredient": "Eggplant",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Tomatoes, zucchini",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477de"
  },
  "Food Product": "Avocado Toast",
  "Main Ingredient": "Avocado",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Salt, pepper",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477df"
  },
  "Food Product": "Beef Stir-Fry",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Soy sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e0"
  },
  "Food Product": "Black Bean Soup",
  "Main Ingredient": "Black beans",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e1"
  },
  "Food Product": "Cucumber Salad",
  "Main Ingredient": "Cucumber",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice, dill",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e2"
  },
  "Food Product": "Fruit Salad",
  "Main Ingredient": "Mixed fruits",
  "Sweetener": "Sugar",
  "Fat/Oil": "None",
  "Seasoning": "Lemon juice",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e3"
  },
  "Food Product": "Sausage Pizza",
  "Main Ingredient": "Sausage",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Mozzarella cheese",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e4"
  },
  "Food Product": "Chicken Fajitas",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Fajita seasoning",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e5"
  },
  "Food Product": "Mango Salsa",
  "Main Ingredient": "Mango",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Red onion, lime",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e6"
  },
  "Food Product": "Lentil Curry",
  "Main Ingredient": "Lentils",
  "Sweetener": "None",
  "Fat/Oil": "Coconut milk",
  "Seasoning": "Curry powder",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e7"
  },
  "Food Product": "Green Smoothie",
  "Main Ingredient": "Spinach",
  "Sweetener": "Honey",
  "Fat/Oil": "Avocado",
  "Seasoning": "Almond milk",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e8"
  },
  "Food Product": "Stuffed Bell Peppers",
  "Main Ingredient": "Bell peppers",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Ground meat, rice",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477e9"
  },
  "Food Product": "Beef and Broccoli",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Soy sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ea"
  },
  "Food Product": "Cabbage Rolls",
  "Main Ingredient": "Cabbage",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Ground meat, rice",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477eb"
  },
  "Food Product": "Caramel Apple",
  "Main Ingredient": "Apples",
  "Sweetener": "Caramel",
  "Fat/Oil": "None",
  "Seasoning": "None",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ec"
  },
  "Food Product": "Sweet Potato Fries",
  "Main Ingredient": "Sweet potatoes",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Salt, paprika",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ed"
  },
  "Food Product": "Beef Chili",
  "Main Ingredient": "Ground beef",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Chili powder",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ee"
  },
  "Food Product": "Pesto Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Pesto sauce",
  "Seasoning": "None",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ef"
  },
  "Food Product": "Beef Burritos",
  "Main Ingredient": "Ground beef",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Taco seasoning",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f0"
  },
  "Food Product": "Chicken Shawarma",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Shawarma spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f1"
  },
  "Food Product": "Stuffed Mushrooms",
  "Main Ingredient": "Mushrooms",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Garlic, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f2"
  },
  "Food Product": "Zucchini Noodles",
  "Main Ingredient": "Zucchini",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Garlic, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f3"
  },
  "Food Product": "Sweet and Sour Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "Sugar",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Pineapple, bell peppers",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f4"
  },
  "Food Product": "Beef Kabobs",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Seasonings",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f5"
  },
  "Food Product": "Tomato Bruschetta",
  "Main Ingredient": "Tomatoes",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Garlic, basil",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f6"
  },
  "Food Product": "Quinoa Stuffed Peppers",
  "Main Ingredient": "Quinoa",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Vegetables, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f7"
  },
  "Food Product": "Veggie Omelette",
  "Main Ingredient": "Mixed vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Salt, pepper",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f8"
  },
  "Food Product": "Ratatouille",
  "Main Ingredient": "Vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Herbs, garlic",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477f9"
  },
  "Food Product": "Beef Tacos",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Taco seasoning",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477fa"
  },
  "Food Product": "Quinoa Salad",
  "Main Ingredient": "Quinoa",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice, vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477fb"
  },
  "Food Product": "Buffalo Wings",
  "Main Ingredient": "Chicken wings",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Buffalo sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477fc"
  },
  "Food Product": "Stuffed Cabbage Rolls",
  "Main Ingredient": "Cabbage",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Ground meat, rice",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477fd"
  },
  "Food Product": "Orange Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Orange sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477fe"
  },
  "Food Product": "Honey Mustard Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "Honey",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Mustard, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb477ff"
  },
  "Food Product": "Lentil Salad",
  "Main Ingredient": "Lentils",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice, vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47800"
  },
  "Food Product": "Cilantro Lime Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Cilantro, lime",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47801"
  },
  "Food Product": "Ratatouille Pizza",
  "Main Ingredient": "Pizza dough",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Ratatouille vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47802"
  },
  "Food Product": "Chicken Curry",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Coconut milk",
  "Seasoning": "Curry powder",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47803"
  },
  "Food Product": "Pesto Pasta Salad",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Pesto sauce",
  "Seasoning": "Tomatoes, vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47804"
  },
  "Food Product": "Beef and Mushroom Stir-Fry",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Soy sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47805"
  },
  "Food Product": "Tofu Curry",
  "Main Ingredient": "Tofu",
  "Sweetener": "None",
  "Fat/Oil": "Coconut milk",
  "Seasoning": "Curry paste",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47806"
  },
  "Food Product": "Greek Moussaka",
  "Main Ingredient": "Eggplant",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Ground meat, potatoes",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47807"
  },
  "Food Product": "Brussels Sprouts",
  "Main Ingredient": "Brussels sprouts",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Balsamic glaze",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47808"
  },
  "Food Product": "Baked Chicken Wings",
  "Main Ingredient": "Chicken wings",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Seasonings",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47809"
  },
  "Food Product": "Mango Coconut Popsicles",
  "Main Ingredient": "Mango",
  "Sweetener": "Sugar",
  "Fat/Oil": "Coconut milk",
  "Seasoning": "None",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4780a"
  },
  "Food Product": "Ratatouille Pasta",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Ratatouille vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4780b"
  },
  "Food Product": "Chicken Noodle Soup",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Noodles, vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4780c"
  },
  "Food Product": "Mango Salsa",
  "Main Ingredient": "Mango",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Lime juice, cilantro",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4780d"
  },
  "Food Product": "Spinach Salad",
  "Main Ingredient": "Spinach",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Balsamic vinaigrette",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4780e"
  },
  "Food Product": "Caramelized Onions",
  "Main Ingredient": "Onions",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "None",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4780f"
  },
  "Food Product": "Strawberry Spinach Salad",
  "Main Ingredient": "Spinach",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Strawberries, vinaigrette",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47810"
  },
  "Food Product": "Ratatouille Tart",
  "Main Ingredient": "Vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Puff pastry, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47811"
  },
  "Food Product": "Honey Glazed Carrots",
  "Main Ingredient": "Carrots",
  "Sweetener": "Honey",
  "Fat/Oil": "Butter",
  "Seasoning": "None",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47812"
  },
  "Food Product": "Cucumber Salad",
  "Main Ingredient": "Cucumbers",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Vinegar, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47813"
  },
  "Food Product": "Greek Lemon Potatoes",
  "Main Ingredient": "Potatoes",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47814"
  },
  "Food Product": "Stuffed Tomatoes",
  "Main Ingredient": "Tomatoes",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Herbs, breadcrumbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47815"
  },
  "Food Product": "Lemon Pepper Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon pepper seasoning",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47816"
  },
  "Food Product": "Chicken Shawarma",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Shawarma seasoning",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47817"
  },
  "Food Product": "Lemon Herb Roasted Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47818"
  },
  "Food Product": "Greek Lemon Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice, herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47819"
  },
  "Food Product": "Roasted Brussels Sprouts",
  "Main Ingredient": "Brussels sprouts",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Balsamic glaze",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4781a"
  },
  "Food Product": "Beef Burritos",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Burrito seasoning",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4781b"
  },
  "Food Product": "Raspberry Spinach Salad",
  "Main Ingredient": "Spinach",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Raspberries, vinaigrette",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4781c"
  },
  "Food Product": "Chicken and Rice Soup",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Rice, vegetables",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4781d"
  },
  "Food Product": "Vegetable Curry",
  "Main Ingredient": "Mixed vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Coconut milk",
  "Seasoning": "Curry paste",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4781e"
  },
  "Food Product": "Ratatouille",
  "Main Ingredient": "Vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Herbs",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4781f"
  },
  "Food Product": "Biryani",
  "Main Ingredient": "Rice",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Biryani masala, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47820"
  },
  "Food Product": "Chole Bhature",
  "Main Ingredient": "Chickpeas",
  "Sweetener": "Sugar",
  "Fat/Oil": "Ghee",
  "Seasoning": "Chole masala, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47821"
  },
  "Food Product": "Masala Dosa",
  "Main Ingredient": "Rice",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Potato masala, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47822"
  },
  "Food Product": "Samosa",
  "Main Ingredient": "Potatoes",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Spices",
  "Allergens": "None",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47823"
  },
  "Food Product": "Aloo Gobi",
  "Main Ingredient": "Potatoes",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Cauliflower, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47824"
  },
  "Food Product": "Chicken Biryani",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Basmati rice, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47825"
  },
  "Food Product": "Vada Pav",
  "Main Ingredient": "Potato",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Pav bun, chutney",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47826"
  },
  "Food Product": "Pani Puri",
  "Main Ingredient": "Semolina",
  "Sweetener": "Tamarind",
  "Fat/Oil": "None",
  "Seasoning": "Spiced water, chutney",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47827"
  },
  "Food Product": "Rajma Chawal",
  "Main Ingredient": "Kidney beans",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Spices",
  "Allergens": "None",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47828"
  },
  "Food Product": "Chicken Curry",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Curry spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47829"
  },
  "Food Product": "Vegetable Biryani",
  "Main Ingredient": "Mixed vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Basmati rice, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4782a"
  },
  "Food Product": "Chana Masala",
  "Main Ingredient": "Chickpeas",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Masala spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4782b"
  },
  "Food Product": "Paniyaram",
  "Main Ingredient": "Fermented batter",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Mustard seeds, curry leaves",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4782c"
  },
  "Food Product": "Pav Bhaji",
  "Main Ingredient": "Mixed vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Pav bread, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4782d"
  },
  "Food Product": "Hyderabadi Biryani",
  "Main Ingredient": "Basmati rice",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Meat/vegetables, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4782e"
  },
  "Food Product": "Dosa",
  "Main Ingredient": "Rice",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Potato masala, chutney",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4782f"
  },
  "Food Product": "Chole Kulche",
  "Main Ingredient": "Chickpeas",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Kulcha bread, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47830"
  },
  "Food Product": "Gobi Manchurian",
  "Main Ingredient": "Cauliflower",
  "Sweetener": "None",
  "Fat/Oil": "Oil",
  "Seasoning": "Manchurian sauce",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47831"
  },
  "Food Product": "Mutton Biryani",
  "Main Ingredient": "Mutton",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Basmati rice, spices",
  "Allergens": "None",
  "Prediction": "Does not contain",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47832"
  },
  "Food Product": "Oatmeal",
  "Main Ingredient": "Oats",
  "Sweetener": "Sugar",
  "Fat/Oil": "Milk",
  "Seasoning": "Cinnamon",
  "Allergens": "Oats, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47833"
  },
  "Food Product": "Chicken Satay",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Peanut butter",
  "Seasoning": "Soy sauce",
  "Allergens": "Peanuts",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47834"
  },
  "Food Product": "Peanut Butter",
  "Main Ingredient": "Peanuts",
  "Sweetener": "Sugar",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Salt",
  "Allergens": "Peanuts",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47835"
  },
  "Food Product": "Chicken Satay",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Peanut oil",
  "Seasoning": "Satay sauce, spices",
  "Allergens": "Peanuts",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47836"
  },
  "Food Product": "Pesto Chicken",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Pesto sauce",
  "Allergens": "Pine nuts, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47837"
  },
  "Food Product": "Zucchini Noodles with Pesto",
  "Main Ingredient": "Zucchini",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Pesto sauce",
  "Allergens": "Pine nuts, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47838"
  },
  "Food Product": "Rice Pudding",
  "Main Ingredient": "Rice",
  "Sweetener": "Sugar",
  "Fat/Oil": "Milk",
  "Seasoning": "Cinnamon, raisins",
  "Allergens": "Rice, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47839"
  },
  "Food Product": "Shrimp Scampi",
  "Main Ingredient": "Shrimp",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Garlic, lemon",
  "Allergens": "Shellfish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4783a"
  },
  "Food Product": "Shrimp Scampi Pasta",
  "Main Ingredient": "Shrimp",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Garlic, lemon",
  "Allergens": "Shellfish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4783b"
  },
  "Food Product": "Garlic Shrimp",
  "Main Ingredient": "Shrimp",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Garlic",
  "Allergens": "Shellfish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4783c"
  },
  "Food Product": "Lemon Garlic Shrimp",
  "Main Ingredient": "Shrimp",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Lemon juice, garlic",
  "Allergens": "Shellfish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4783d"
  },
  "Food Product": "Prawn Biryani",
  "Main Ingredient": "Prawns",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Basmati rice, spices",
  "Allergens": "Shellfish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4783e"
  },
  "Food Product": "Lobster Bisque",
  "Main Ingredient": "Lobster",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Cream, brandy",
  "Allergens": "Shellfish, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4783f"
  },
  "Food Product": "Caesar Shrimp Skewers",
  "Main Ingredient": "Shrimp",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Caesar dressing",
  "Allergens": "Shellfish, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47840"
  },
  "Food Product": "Shrimp Scampi",
  "Main Ingredient": "Shrimp",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Garlic, lemon",
  "Allergens": "Shellfish, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47841"
  },
  "Food Product": "Prawn Curry",
  "Main Ingredient": "Prawns",
  "Sweetener": "None",
  "Fat/Oil": "Coconut milk",
  "Seasoning": "Curry spices",
  "Allergens": "Shellfish, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47842"
  },
  "Food Product": "Lobster Roll",
  "Main Ingredient": "Lobster",
  "Sweetener": "None",
  "Fat/Oil": "Mayonnaise",
  "Seasoning": "Celery, lemon juice",
  "Allergens": "Shellfish, Eggs",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47843"
  },
  "Food Product": "Bacon-Wrapped Shrimp",
  "Main Ingredient": "Shrimp",
  "Sweetener": "None",
  "Fat/Oil": "Bacon",
  "Seasoning": "Seasonings",
  "Allergens": "Shellfish, Pork",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47844"
  },
  "Food Product": "Shrimp Fried Rice",
  "Main Ingredient": "Shrimp",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Soy sauce",
  "Allergens": "Shellfish, Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47845"
  },
  "Food Product": "Soy Milk",
  "Main Ingredient": "Soybeans",
  "Sweetener": "Sugar",
  "Fat/Oil": "None",
  "Seasoning": "Emulsifiers",
  "Allergens": "Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47846"
  },
  "Food Product": "Tofu Stir-Fry",
  "Main Ingredient": "Tofu",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Soy sauce",
  "Allergens": "Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47847"
  },
  "Food Product": "Miso Soup",
  "Main Ingredient": "Miso paste",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Tofu, seaweed",
  "Allergens": "Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47848"
  },
  "Food Product": "Tofu Scramble",
  "Main Ingredient": "Tofu",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Turmeric, spices",
  "Allergens": "Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47849"
  },
  "Food Product": "Chicken Teriyaki",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Soy sauce",
  "Seasoning": "Honey, ginger",
  "Allergens": "Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4784a"
  },
  "Food Product": "Teriyaki Beef",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Soy sauce",
  "Seasoning": "Teriyaki sauce, vegetables",
  "Allergens": "Soybeans",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4784b"
  },
  "Food Product": "Sushi Rolls",
  "Main Ingredient": "Sushi rice",
  "Sweetener": "None",
  "Fat/Oil": "Soy sauce",
  "Seasoning": "Nori (seaweed), fish",
  "Allergens": "Soybeans, Fish",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4784c"
  },
  "Food Product": "Wheat Bread",
  "Main Ingredient": "Wheat flour",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Salt",
  "Allergens": "Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4784d"
  },
  "Food Product": "Zucchini Bread",
  "Main Ingredient": "Zucchini",
  "Sweetener": "Sugar",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Flour",
  "Allergens": "Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4784e"
  },
  "Food Product": "Chicken Noodle Casserole",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Noodles, vegetables",
  "Allergens": "Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4784f"
  },
  "Food Product": "Onion Rings",
  "Main Ingredient": "Onions",
  "Sweetener": "None",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Flour",
  "Allergens": "Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47850"
  },
  "Food Product": "Chicken Pot Pie",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Vegetables, pastry",
  "Allergens": "Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47851"
  },
  "Food Product": "Grilled Portobello Mushroom Burger",
  "Main Ingredient": "Portobello mushrooms",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Burger bun, vegetables",
  "Allergens": "Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47852"
  },
  "Food Product": "Aloo Paratha",
  "Main Ingredient": "Potatoes",
  "Sweetener": "None",
  "Fat/Oil": "Ghee",
  "Seasoning": "Wheat flour, spices",
  "Allergens": "Wheat",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47853"
  },
  "Food Product": "Oatmeal Raisin Cookies",
  "Main Ingredient": "Oats",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Flour",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47854"
  },
  "Food Product": "Pancakes",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Baking powder",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47855"
  },
  "Food Product": "Carrot Cake",
  "Main Ingredient": "Carrots",
  "Sweetener": "Sugar",
  "Fat/Oil": "Vegetable oil",
  "Seasoning": "Cinnamon",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47856"
  },
  "Food Product": "Blueberry Muffins",
  "Main Ingredient": "Blueberries",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Flour",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47857"
  },
  "Food Product": "Chocolate Chip Cookies",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Chocolate chips",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47858"
  },
  "Food Product": "Mushroom Risotto",
  "Main Ingredient": "Arborio rice",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Mushroom",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47859"
  },
  "Food Product": "Cinnamon Rolls",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4785a"
  },
  "Food Product": "Pineapple Upside-Down Cake",
  "Main Ingredient": "Pineapple",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Flour",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4785b"
  },
  "Food Product": "Apple Pie",
  "Main Ingredient": "Apples",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4785c"
  },
  "Food Product": "Banana Bread",
  "Main Ingredient": "Bananas",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Flour",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4785d"
  },
  "Food Product": "Vanilla Cupcakes",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Vanilla extract",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4785e"
  },
  "Food Product": "Apple Crisp",
  "Main Ingredient": "Apples",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4785f"
  },
  "Food Product": "Pasta Carbonara",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Bacon",
  "Seasoning": "Egg, Parmesan cheese",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47860"
  },
  "Food Product": "Blueberry Pancakes",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Blueberries",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47861"
  },
  "Food Product": "Lemon Bars",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Lemon juice",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47862"
  },
  "Food Product": "Pumpkin Pie",
  "Main Ingredient": "Pumpkin",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon, nutmeg",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47863"
  },
  "Food Product": "Mixed Berry Pie",
  "Main Ingredient": "Mixed berries",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Flour",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47864"
  },
  "Food Product": "Garlic Bread",
  "Main Ingredient": "Bread",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Garlic",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47865"
  },
  "Food Product": "Berry Cobbler",
  "Main Ingredient": "Mixed berries",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Flour",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47866"
  },
  "Food Product": "Baked Ziti",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Cheese",
  "Seasoning": "Tomato sauce",
  "Allergens": "Wheat, Dairy",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47867"
  },
  "Food Product": "Baked Ziti",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Cheese",
  "Seasoning": "Tomato sauce",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47868"
  },
  "Food Product": "Key Lime Pie",
  "Main Ingredient": "Lime juice",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Graham cracker crust",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47869"
  },
  "Food Product": "Lemon Poppy Seed Muffins",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Lemon zest, poppy seeds",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4786a"
  },
  "Food Product": "Chicken Quesadilla",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Cheese",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4786b"
  },
  "Food Product": "Pancake Stack",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Maple syrup",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4786c"
  },
  "Food Product": "Strawberry Shortcake",
  "Main Ingredient": "Strawberries",
  "Sweetener": "Sugar",
  "Fat/Oil": "Whipped cream",
  "Seasoning": "Shortcake",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4786d"
  },
  "Food Product": "Berry Crumble",
  "Main Ingredient": "Mixed berries",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Oats, cinnamon",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4786e"
  },
  "Food Product": "Raspberry Cheesecake",
  "Main Ingredient": "Cream cheese",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Graham cracker crust, raspberries",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4786f"
  },
  "Food Product": "Oatmeal Raisin Cookies",
  "Main Ingredient": "Oats",
  "Sweetener": "Brown sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Raisins, cinnamon",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47870"
  },
  "Food Product": "Apple Crisp",
  "Main Ingredient": "Apples",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon, oats",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47871"
  },
  "Food Product": "Chicken Enchiladas",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Enchilada sauce",
  "Seasoning": "Cheese, tortillas",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47872"
  },
  "Food Product": "Caesar Salad Wrap",
  "Main Ingredient": "Romaine lettuce",
  "Sweetener": "None",
  "Fat/Oil": "Caesar dressing",
  "Seasoning": "Parmesan cheese, croutons",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47873"
  },
  "Food Product": "S'mores",
  "Main Ingredient": "Graham crackers",
  "Sweetener": "Marshmallows",
  "Fat/Oil": "Chocolate",
  "Seasoning": "None",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47874"
  },
  "Food Product": "Tiramisu",
  "Main Ingredient": "Ladyfingers",
  "Sweetener": "Sugar",
  "Fat/Oil": "Mascarpone cheese",
  "Seasoning": "Coffee, cocoa",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47875"
  },
  "Food Product": "Cinnamon Rolls",
  "Main Ingredient": "Dough",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon, icing",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47876"
  },
  "Food Product": "Chicken Caesar Salad",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Caesar dressing",
  "Seasoning": "Romaine lettuce, croutons",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47877"
  },
  "Food Product": "Vegetable Lasagna",
  "Main Ingredient": "Vegetables",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Tomato sauce, cheese",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47878"
  },
  "Food Product": "Chicken Alfredo Pizza",
  "Main Ingredient": "Pizza dough",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Chicken, Alfredo sauce",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47879"
  },
  "Food Product": "Caesar Pasta Salad",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "Caesar dressing",
  "Seasoning": "Romaine lettuce, Parmesan cheese",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4787a"
  },
  "Food Product": "Baked Apple",
  "Main Ingredient": "Apples",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon, oats",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4787b"
  },
  "Food Product": "Apple Pie",
  "Main Ingredient": "Apples",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon, pastry",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4787c"
  },
  "Food Product": "Chicken Parmesan",
  "Main Ingredient": "Chicken",
  "Sweetener": "None",
  "Fat/Oil": "Olive oil",
  "Seasoning": "Tomato sauce, cheese",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4787d"
  },
  "Food Product": "Pumpkin Pie",
  "Main Ingredient": "Pumpkin",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Pumpkin spice, pastry",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4787e"
  },
  "Food Product": "Blueberry Muffins",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Blueberries",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4787f"
  },
  "Food Product": "Sausage and Pepper Pizza",
  "Main Ingredient": "Pizza dough",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Sausage, bell peppers",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47880"
  },
  "Food Product": "Beef Wellington",
  "Main Ingredient": "Beef",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "Mushrooms, puff pastry",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47881"
  },
  "Food Product": "Baked Ziti",
  "Main Ingredient": "Pasta",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Tomato sauce, cheese",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47882"
  },
  "Food Product": "Jalebi",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Ghee",
  "Seasoning": "Saffron syrup",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47883"
  },
  "Food Product": "Butter Naan",
  "Main Ingredient": "Flour",
  "Sweetener": "None",
  "Fat/Oil": "Butter",
  "Seasoning": "None",
  "Allergens": "Wheat, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47884"
  },
  "Food Product": "Tiramisu",
  "Main Ingredient": "Ladyfingers",
  "Sweetener": "Sugar",
  "Fat/Oil": "Mascarpone cheese, coffee liqueur",
  "Seasoning": "Cocoa powder",
  "Allergens": "Wheat, Dairy, Alcohol",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47885"
  },
  "Food Product": "Chocolate Cake",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cocoa powder",
  "Allergens": "Wheat, Dairy, Cocoa",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47886"
  },
  "Food Product": "Chocolate Chip Pancakes",
  "Main Ingredient": "Flour",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Chocolate chips",
  "Allergens": "Wheat, Dairy, Cocoa",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47887"
  },
  "Food Product": "Lemon Bars",
  "Main Ingredient": "Lemon juice",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Flour, eggs",
  "Allergens": "Wheat, Dairy, Eggs",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47888"
  },
  "Food Product": "Pecan Pie",
  "Main Ingredient": "Pecans",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Corn syrup",
  "Allergens": "Wheat, Dairy, Nuts",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb47889"
  },
  "Food Product": "Zucchini Bread",
  "Main Ingredient": "Zucchini",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon, nuts",
  "Allergens": "Wheat, Dairy, Nuts",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4788a"
  },
  "Food Product": "Banana Bread",
  "Main Ingredient": "Bananas",
  "Sweetener": "Sugar",
  "Fat/Oil": "Butter",
  "Seasoning": "Cinnamon, nuts",
  "Allergens": "Wheat, Dairy, Nuts",
  "Prediction": "Contains",
  "Veg/Non veg": "Veg"
},
{
  "_id": {
    "$oid": "654629a5b4e368414fb4788b"
  },
  "Food Product": "Hawaiian Pizza",
  "Main Ingredient": "Pizza dough",
  "Sweetener": "None",
  "Fat/Oil": "None",
  "Seasoning": "Pineapple, ham",
  "Allergens": "Wheat, Pork, Dairy",
  "Prediction": "Contains",
  "Veg/Non veg": "Non veg"
}]

# User input for desired features
user_input = {
    "Sweetener": "Sugar",
    "Seasoning": "Flour",
    "Allergens": "Wheat",
    "Veg/Non veg": "Veg"
}

# Preprocess the data and user input
def preprocess(text):
    return " ".join(str(text) for text in user_input.values())

# Create TF-IDF vectors for the food products
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([preprocess(product) for product in food_data])

# Create a representation for the user input
user_input_representation = preprocess(user_input)

# Calculate cosine similarity between user input and food products
user_input_vector = tfidf_vectorizer.transform([user_input_representation])
similarity_scores = linear_kernel(user_input_vector, tfidf_matrix)

# Get the top recommendations
recommendations = sorted(enumerate(similarity_scores[0]), key=lambda x: x[1], reverse=True)


print("Top Recommended Food Products:")
for index, score in recommendations:
    print(food_data[index]["Food Product"], "-", "Similarity Score =", score)

