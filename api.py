from requests import get
from requests.models import Response
from app import parks


def get_park_activities(park: str) -> dict[str, str]:
    park_activities: Response = get("https://developer.nps.gov/api/v1/parks", params={"api_key": "yciKZcC0PxNgfw0ArNOH4kwrghRj33jsJF7znKsn"})
