from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
import pytz  # For handling timezones

@api_view(['GET'])
def get_info(request):
    slack_name = request.GET.get('slack_name', 'example_name')
    track = request.GET.get('track', 'backend')
    
    # Get the current UTC time
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": datetime.now().strftime('%A'),
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Tomilola-ng/TrackBackendTask1/blob/main/api/views.py",
        "github_repo_url": "https://github.com/Tomilola-ng/TrackBackendTask1",
        "status_code": 200
    }

    return Response(response_data)
