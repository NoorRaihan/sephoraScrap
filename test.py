import requests as req

header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

TARGET_URL = "https://www.sephora.my/api/v2.4/products/nudestix-nudies-matte-all-over-face-color-blush/reviews?page[number]=1&page[size]=1&sort=recent&filter[rating]=5"

r = req.get(TARGET_URL, headers=header)
print(r.status_code)