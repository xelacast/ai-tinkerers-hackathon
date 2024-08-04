from twelvelabs import TwelveLabs
import os

client = TwelveLabs(api_key=os.getenv('TL_API_KEY'))

# create a video embedding need this to be a system wide variable or a getter?

def twelvelabs_generate_text_from_video(video_id):
    # video_id = "66ae779d7b2deac81dd1284c"

    text_stream = client.generate.text_stream(
        video_id=video_id, prompt="""
    Extract the ingredients and the instructions from this video.

    Make sure instructions are in sequential order from start to finish

    Use this json format as Structured Data.
    {
      "title": "title",
      "dishName": "dishName",
      "ingredients": [
        {
          "item": "item",
          "amount": "2",
          "unit": "unit"
        }
      ],
      "instructions": [
        {
          "number": "1",
          "instruction": "instruction"
        }
      ]
    }


    If there is no information leave blank.

    DO NOT RETURN ANYTHING OTHER THAN THE JSON."""
    )
    for text in text_stream:
        print(text)
    return text_stream.aggregated_text

from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import json
def add_recipe(recipe_dict):
  # db = TinyDB('../db/recipes.json', storage=CachingMiddleware(JSONStorage))
  # recipe_table = db.table('recipes')
  # recipe_table.insert(text)
  file_path = '../db/recipes.json'
  with open(file_path, 'r') as fp:
    db = json.load(fp)

  db['recipes'].append(recipe_dict)
  print(db)
  with open(file_path, 'w') as json_file:
    json.dump(db, json_file, indent=4)


add_recipe({
      "title": "Beef Stroganoff",
      "dishName": "Beef Stroganoff",
      "ingredients": [
        { "item": "vegetable oil", "amount": "2", "unit": "tablespoons" },
        {
          "item": "beef sirloin, cut into 2-by-1-by-1/8-inch strips",
          "amount": "1",
          "unit": "pound"
        },
        { "item": "kosher salt", "amount": "to taste", "unit": "" },
        {
          "item": "freshly ground black pepper",
          "amount": "to taste",
          "unit": ""
        },
        { "item": "unsalted butter", "amount": "8", "unit": "tablespoons" },
        {
          "item": "button mushrooms, quartered",
          "amount": "12",
          "unit": "ounces"
        },
        {
          "item": "medium yellow onion, thinly sliced",
          "amount": "1",
          "unit": "whole"
        },
        { "item": "tomato paste", "amount": "1", "unit": "tablespoon" },
        { "item": "all-purpose flour", "amount": "2", "unit": "tablespoons" },
        {
          "item": "beef broth, homemade or low-sodium canned",
          "amount": "2",
          "unit": "cups"
        },
        { "item": "sour cream", "amount": "1/4", "unit": "cup" },
        { "item": "Dijon mustard", "amount": "2", "unit": "teaspoons" },
        {
          "item": "freshly squeezed lemon juice",
          "amount": "2",
          "unit": "teaspoons"
        },
        {
          "item": "chopped flat-leaf parsley leaves",
          "amount": "1",
          "unit": "tablespoon"
        },
        { "item": "wide egg noodles", "amount": "12", "unit": "ounces" }
      ],
      "instructions": [
        {
          "step": "1",
          "instruction": "For the stroganoff: Preheat a large skillet over medium heat for 3 to 4 minutes. Raise the heat to high and heat 1 tablespoon oil. Season half the beef with salt and pepper, add to the skillet, arranging it in a single layer, and cook without stirring until well-browned and still pinkish inside, 1 to 2 minutes. (It is key to only partially cook the meat at this stage, since it will be finish cooking later in the sauce.) Transfer to a large plate and set aside. Repeat with the remaining oil and beef. Discard any excess oil."
        },
        {
          "step": "2",
          "instruction": "Return the skillet to medium-high heat. Melt 2 tablespoons of the butter and, when the foaming begins to subside, add the mushrooms and cook, stirring occasionally, until well-browned, about 7 minutes. Season with salt and pepper to taste. Using a slotted spoon, transfer to the plate with the beef."
        },
        {
          "step": "3",
          "instruction": "Heat the remaining 4 tablespoons butter in the skillet; when the foaming begins to subside, add the onion and cook, stirring, until lightly caramelized, about 5 minutes. Add the tomato paste and cook, stirring, until lightly browned, about 1 minute more. Whisk in the flour and cook, stirring, for 1 minute. Pour in the beef broth and, whisking constantly, bring to a full boil. Remove from the heat. Whisk in the sour cream, mustard and lemon juice and season with pepper to taste. Set the sauce aside covered."
        },
        {
          "step": "4",
          "instruction": "Meanwhile, for the noodles: Bring a large pot of water to a boil, salt generously, and cook the noodles until tender but not mushy. Drain and transfer to a large bowl. Toss with the butter and season with pepper."
        },
        {
          "step": "5",
          "instruction": "Add the beef and any juices, mushrooms and parsley to the sauce and reheat over medium heat until just hot. (Do not boil.) Divide the noodles among 4 plates and top with the stroganoff. Serve immediately."
        }
      ]
    })