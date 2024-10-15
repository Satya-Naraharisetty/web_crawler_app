from flask import Blueprint, request, jsonify
from crawler import crawl_page
import os
import time
import json

# Create a blueprint for the API routes
crawl_bp = Blueprint('crawl', __name__)


@crawl_bp.route('/api/v1/crawl', methods=['POST'])
def crawl():
    data = request.get_json()

    root_url = data.get('root_url')
    max_depth = int(data.get('max_depth'))

    if not root_url or max_depth is None:
        return jsonify({"error": "Invalid input. Provide 'root_url' and 'max_depth'"}), 400

    crawled_urls = [{'url': root_url, 'depth': 0}]

    # Call the crawling function
    crawl_page(root_url, max_depth, 1, crawled_urls)

    # Prepare the response data
    response_data = {
        "root_url": root_url,
        "max_depth": max_depth,
        "crawled_urls": crawled_urls,
        "total_crawled": len(crawled_urls)
    }

    # Save the response to a JSON file (based on the domain and timestamp)
    domain = root_url.split("//")[-1].split("/")[0]
    filename = f"crawl_{domain}_{int(time.time())}.json"
    file_path = os.path.join("crawled_data", filename)

    # Ensure the directory exists
    os.makedirs("crawled_data", exist_ok=True)

    # Save to JSON file
    with open(file_path, 'w') as json_file:
        json.dump(response_data, json_file, indent=4)

    # Return the response to the client
    return jsonify(response_data)
