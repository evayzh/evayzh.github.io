from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
import time
import sys

# Unbuffered output
sys.stdout.reconfigure(line_buffering=True)

client = genai.Client(api_key="AIzaSyACbzmVs4GJiu2fqYWRTr3sQDum7uR3EGk")

# Create images directory
os.makedirs("images", exist_ok=True)

ring_prompts = {
    "trefoil": "sterling silver trefoil knot ring, mathematical topology jewelry, oxidized burnt silver patina, black recesses with polished silver highlights, organic texture, chrome hearts aesthetic, dark moody product photography, black velvet background, dramatic side lighting, macro photography",

    "figure8": "thick sterling silver figure-eight knot ring, mathematical jewelry, heavy oxidation patina, raw organic metal texture, sculptural silver band, gothic luxury aesthetic, product photography on black obsidian surface, cinematic lighting",

    "cinquefoil": "sterling silver cinquefoil torus knot ring, five-fold symmetry, mathematical topology jewelry, oxidized burnt patina, raw hammered texture, chrome hearts inspired, dark editorial product shot, dramatic chiaroscuro lighting on black background",

    "borromean": "three interlocking sterling silver rings forming borromean link, mathematical topology jewelry, oxidized silver with burnt edges, each ring slightly different texture, chrome hearts inspired, dark editorial product shot, dramatic chiaroscuro lighting",

    "solomon": "sterling silver solomon's knot ring, two interlocking squares pattern, ancient mathematical symbol, oxidized burnt silver patina, gothic luxury jewelry, dark moody product photography, black velvet background",

    "mobius": "sterling silver mobius strip ring, twisted band with single surface, mathematical infinity jewelry, oxidized burnt patina, organic texture, chrome hearts aesthetic, macro product photography, dramatic rim lighting on black"
}

print("Generating ring images with Imagen 4...")
print("=" * 50)
sys.stdout.flush()

for ring_name, prompt in ring_prompts.items():
    print(f"\nGenerating {ring_name} ring...")
    sys.stdout.flush()
    try:
        # Using Imagen 4 for image generation
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                output_mime_type="image/png"
            )
        )

        for i, image in enumerate(response.generated_images):
            image_path = f"images/{ring_name}.png"
            img = Image.open(BytesIO(image.image.image_bytes))
            img.save(image_path)
            print(f"  Saved: {image_path}")
            sys.stdout.flush()

        # Wait between requests to avoid rate limits
        print("  Waiting 10s...")
        sys.stdout.flush()
        time.sleep(10)

    except Exception as e:
        print(f"  Error: {e}")
        sys.stdout.flush()
        time.sleep(5)

print("\n" + "=" * 50)
print("Done! Images saved to /Users/evazhang/knot-rings/images/")
