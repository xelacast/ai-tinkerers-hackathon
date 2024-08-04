from twelvelabs import TwelveLabs
import os

client = TwelveLabs(api_key=os.getenv('TL_API_KEY'))

# create a video embedding need this to be a system wide variable or a getter?

def get_twelvelabs_generate_text_from_video(video_id):
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

