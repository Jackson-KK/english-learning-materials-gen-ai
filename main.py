from fastapi import FastAPI
from fastapi.responses import JSONResponse

from ai import get_generated_language_learning_materials


app = FastAPI()

mock_article = """\
NEW YORK -- San Francisco, a city in the western US state of California, has changed in recent years, with personal stories of drug addicts laid out on the streets and violent assaults frequently told by residents and business owners, reported Fox News Digital on Monday.

One resident, Seema Gokhale, who lives near the Tenderloin neighborhood of San Francisco and has been in the city for almost a decade, described life there as "post-apocalyptic."

"It honestly feels like I'm in a place that's been in a zombie apocalypse. It's like a dystopia. It really feels like a dystopian reality right now where I see boarded up storefronts. I see people defecating on the streets," Gokhale was quoted as saying.

A newly released report out of the San Francisco Controller's office found nearly half of the city's commercial sidewalks had feces on them in 2021 and into 2022.

"This is a once a very great, thriving metropolis. It's now just a wasteland. Come here and look around at the businesses. Look at the shops that are close to the small neighborhood businesses that are boarded up. Thirty percent of the office retail space downtown is now empty," Tony Hall, a former city councilman and business owner, was quoted by Fox News Digital as saying.
"""


@app.get("/")
async def root():
    materials = get_generated_language_learning_materials(mock_article, "Chinese", "Entry")
    return JSONResponse({"message": materials})