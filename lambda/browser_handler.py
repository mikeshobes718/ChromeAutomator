import asyncio
import pyppeteer
import json

async def browse():
    browser = await pyppeteer.launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://www.example.com')
    content = await page.content()
    await browser.close()
    return content

def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    page_content = loop.run_until_complete(browse())
    return {
        'statusCode': 200,
        'body': json.dumps('Browser automation completed!')
    }
