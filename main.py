from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (replace with your actual data)
data = [
    {
        "Intensity": "High",
        "Likelihood": "Medium",
        "Relevance": "High",
        "Year": 2022,
        "Country": "USA",
        "Topics": ["Topic 1", "Topic 2"],
        "Region": "North",
        "City": "New York",
    },
    # Add more data...
]

@app.route('/api/data', methods=['GET'])
def get_filtered_data():
    # Get filter parameters from the request
    end_year = request.args.get('end_year')
    topics = request.args.getlist('topics')
    # Implement other filters...

    # Apply filters to the data
    filtered_data = [item for item in data if
                     (not end_year or item['Year'] <= int(end_year)) and
                     (not topics or any(topic in item['Topics'] for topic in topics))]
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True , port=5002)
